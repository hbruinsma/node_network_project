# main.py
from tasks.example_task import example_task
from tasks.progress_estimation import progress_estimation_node
from shared.state import initialize_node, add_feedback, state

def main():
    print("Node network initialized")

    # Initialize tasks
    initialize_node("example_task_1")
    initialize_node("example_task_2")

    # Run the first task
    input_data_1 = "Input for task 1"
    example_task(input_data_1)

    # Add feedback for task 1 and rerun
    add_feedback("example_task_1", "Input was too generic")
    example_task(input_data_1)

    # Run the second task
    input_data_2 = "Input for task 2"
    example_task(input_data_2)

    # Call the progress estimation node
    progress_estimation_node()

    # Display final outputs
    print("Final Outputs:")
    for node_name, details in state["nodes"].items():
        output = details.get("output", "No Output")
        print(f"{node_name}: {output}")

if __name__ == "__main__":
    main()
