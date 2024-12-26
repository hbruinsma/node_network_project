import unittest
from shared.state import state, update_node_status, update_node_output
from shared.parallel_execution import execute_in_parallel
from tasks.task import example_task
from tasks.progress_estimation import initialize_progress_bar, finalize_progress_bar
from shared.logging import logger, log_event, log_error, log_task_event


class TestNodeNetwork(unittest.TestCase):
    def setUp(self):
        state["nodes"] = {
            "example_task_1": {"status": "Not Started", "dependencies": [], "retries": 0, "output": None},
            "example_task_2": {"status": "Not Started", "dependencies": ["example_task_1"], "retries": 0, "output": None},
            "example_task_3": {"status": "Not Started", "dependencies": ["example_task_2"], "retries": 0, "output": None},
        }
        state["total_tasks"] = len(state["nodes"])
        state["progress"] = 0

    def test_task_execution(self):
        example_task("Input for Task 1", "example_task_1")
        self.assertEqual(state["nodes"]["example_task_1"]["status"], "Completed")
        self.assertEqual(state["nodes"]["example_task_1"]["output"], "Processed: Input for Task 1")

    def test_dependency_management(self):
        tasks = [
            (example_task, ("Input for Task 1", "example_task_1")),
            (example_task, ("Input for Task 2", "example_task_2")),
            (example_task, ("Input for Task 3", "example_task_3")),
        ]
        execute_in_parallel(tasks, state)
        self.assertEqual(state["nodes"]["example_task_1"]["status"], "Completed")
        self.assertEqual(state["nodes"]["example_task_2"]["status"], "Completed")
        self.assertEqual(state["nodes"]["example_task_3"]["status"], "Completed")

    def test_progress_tracking(self):
        """
        Test that progress updates correctly during task execution.
        """
        initialize_progress_bar(total_tasks=len(state["nodes"]))  # Pass total_tasks explicitly for testing
        example_task("Input for Task 1", "example_task_1")
        self.assertGreater(state["progress"], 0)
        self.assertEqual(state["nodes"]["example_task_1"]["status"], "Completed")
        finalize_progress_bar()


    def test_parallel_execution(self):
        tasks = [
            (example_task, ["Input for Task 1", "example_task_1"]),
            (example_task, ["Input for Task 2", "example_task_2"]),
            (example_task, ["Input for Task 3", "example_task_3"]),
        ]
        execute_in_parallel(tasks, state)
        self.assertEqual(state["progress"], 100)
        self.assertEqual(state["nodes"]["example_task_1"]["status"], "Completed")
        self.assertEqual(state["nodes"]["example_task_2"]["status"], "Completed")
        self.assertEqual(state["nodes"]["example_task_3"]["status"], "Completed")

    def test_error_handling(self):
        def faulty_task(*args):
            raise ValueError("Simulated task error")

        state["nodes"]["faulty_task"] = {"status": "Not Started", "dependencies": [], "retries": 0, "output": None}

        try:
            faulty_task()
        except ValueError as e:
            update_node_status("faulty_task", "Error")
            self.assertEqual(str(e), "Simulated task error")
            self.assertEqual(state["nodes"]["faulty_task"]["status"], "Error")

    def tearDown(self):
        state.clear()
        state["nodes"] = {}
        state["progress"] = 0
        state["total_tasks"] = 0
        state["completed_tasks"] = 0

if __name__ == "__main__":
    unittest.main()
