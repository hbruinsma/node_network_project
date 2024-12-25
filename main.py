# main.py
from tasks.example_task import example_task
from tasks.progress_estimation import progress_estimation_node
from shared.state import register_node, get_priority, state
from shared.logging import log_event
from shared.parallel_execution import execute_in_parallel
from shared.timer import start_timer, stop_timer

def main():
    log_event("Node network initialized")
    start_timer()  # Start the workflow timer

    # Dynamically register tasks with priorities
    register_node("example_task_1", priority=2)
    register_node("example_task_2", dependencies=["example_task_1"], priority=1)
    register_node("example_task_3", dependencies=["example_task_2"], priority=3)

    # Run the progress estimation node initially
    progress_estimation_node()

    # Sort tasks by priority
    tasks_to_run = sorted(
        [(node, details) for node, details in state["nodes"].items()],
        key=lambda x: x[1]["priority"],
        reverse=True  # Higher priority first
    )

    # Define tasks for parallel execution based on sorted priorities
    parallel_tasks = [
        (example_task, ("Input for " + node, node))
        for node, details in tasks_to_run
        if not details["dependencies"]  # No dependencies
    ]

    # Execute tasks in parallel
    execute_in_parallel(parallel_tasks)

    # Sequentially run dependent tasks in priority order
    for node, details in tasks_to_run:
        if details["dependencies"]:
            example_task(f"Input for {node}", node)

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
