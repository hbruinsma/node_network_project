# main.py
from tasks.example_task import example_task
from tasks.progress_estimation import progress_estimation_node
from shared.state import initialize_node, add_dependency, generate_task_name, state
from shared.logging import log_event

def main():
    log_event("Node network initialized")

    # Initialize tasks
    task_1 = generate_task_name("example_task")
    task_2 = generate_task_name("example_task")
    task_3 = generate_task_name("example_task")

    initialize_node(task_1)
    initialize_node(task_2)
    initialize_node(task_3)

    # Set dependencies
    add_dependency(task_2, task_1)  # Task 2 depends on Task 1
    add_dependency(task_3, task_2)  # Task 3 depends on Task 2

    # Execute tasks
    example_task("Input for Task 1", task_1)
    example_task("Input for Task 2", task_2)
    example_task("Input for Task 3", task_3)

    # Call the progress estimation node
    log_event("Calling Progress Estimation Node")
    progress_estimation_node()

    # Display final outputs
    log_event("Final Outputs:")
    for node_name, details in state["nodes"].items():
        output = details.get("output", "No Output")
        log_event(f"{node_name}: {output}")

if __name__ == "__main__":
    main()
