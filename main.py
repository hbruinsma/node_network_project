# main.py
from tasks.example_task import example_task
from shared.state import initialize_node, get_progress, get_node_status, state

def main():
    print("Node network initialized")

    # Initialize tasks
    initialize_node("example_task_1")
    initialize_node("example_task_2")

    # Run the first task
    input_data_1 = "Input for task 1"
    example_task(input_data_1)

    # Run the second task
    input_data_2 = "Input for task 2"
    example_task(input_data_2)

    # Display progress and status
    progress = get_progress()
    print(f"Progress: {progress}%")
    print(f"Task 1 Output: {state['nodes']['example_task_1']['output']}")
    print(f"Task 2 Output: {state['nodes']['example_task_2']['output']}")

if __name__ == "__main__":
    main()
