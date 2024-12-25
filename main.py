# main.py
from tasks.example_task import example_task
from tasks.progress_estimation import progress_estimation_node
from shared.state import initialize_node, generate_task_name, state
from shared.logging import log_event

def main():
    log_event("Node network initialized")

    # Dynamically create and run tasks
    task_inputs = ["Input for task 1", "FAIL", "Retry this task"]

    for input_data in task_inputs:
        task_name = generate_task_name("example_task")
        initialize_node(task_name)
        log_event(f"Task initialized: {task_name}")
        example_task(input_data)

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
