# main.py
from tasks.example_task import example_task
from shared.state import initialize_node, get_progress, get_node_status

def main():
    print("Node network initialized")

    # Initialize tasks
    initialize_node("example_task_1")
    initialize_node("example_task_2")

    # Run the first task
    input_data = "Input for task 1"
    output_1 = example_task(input_data)

    # Run the second task
    input_data = "Input for task 2"
    output_2 = example_task(input_data)

    # Display progress and status
    progress = get_progress()
    print(f"Progress: {progress}%")
    print(f"Task 1 Status: {get_node_status('example_task_1')}")
    print(f"Task 2 Status: {get_node_status('example_task_2')}")

if __name__ == "__main__":
    main()



