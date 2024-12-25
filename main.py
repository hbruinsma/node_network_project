from tasks.example_task import example_task
from tasks.progress_estimation import progress_estimation_node
from shared.state import register_node, update_node_status, state
from shared.logging import log_event
from shared.parallel_execution import execute_in_parallel
from shared.timer import start_timer, stop_timer

def main():
    log_event("Node network initialized")
    start_timer()  # Start the workflow timer

    # Dynamically register tasks
    register_node("example_task_1", priority=2)
    register_node("example_task_2", dependencies=["example_task_1"], priority=1)
    register_node("example_task_3", dependencies=["example_task_2"], priority=3)

    # Run the progress estimation node initially
    progress_estimation_node()

    # Define tasks for parallel execution
    tasks_to_run = [
        (example_task, ("Input for Task 1", "example_task_1")),
        (example_task, ("Input for Task 3", "example_task_3")),  # This will wait for dependencies
    ]

    log_event("Executing parallel tasks...")
    execute_in_parallel(tasks_to_run)

    log_event("Executing sequential tasks...")
    example_task("Input for Task 2", "example_task_2")

    # Run the progress estimation node after all tasks
    progress_estimation_node()

    # Stop the workflow timer
    stop_timer()

    # Display final outputs
    log_event("Final Outputs:")
    for node_name, details in state["nodes"].items():
        output = details.get("output", "No Output")
        log_event(f"{node_name}: {output}")


    # Run the progress estimation node initially
    progress_estimation_node()

    # Define tasks for parallel execution
    tasks_to_run = [
        (example_task, ("Input for Task 1", "example_task_1")),
        (example_task, ("Input for Task 3", "example_task_3")),  # This will wait for dependencies
    ]

    # Execute tasks in parallel
    execute_in_parallel(tasks_to_run)

    # Sequentially run dependent tasks
    example_task("Input for Task 2", "example_task_2")

    # Run the progress estimation node after all tasks
    progress_estimation_node()

    # Stop the workflow timer
    stop_timer()

    # Display final outputs
    log_event("Final Outputs:")
    for node_name, details in state["nodes"].items():
        output = details.get("output", "No Output")
        log_event(f"{node_name}: {output}")

if __name__ == "__main__":
    main()
