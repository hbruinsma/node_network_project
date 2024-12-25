# main.py
from tasks.example_task import example_task
from shared.state import get_node_status, get_progress, update_progress

def main():
    print("Node network initialized")

    # Example input data
    input_data = "Task input data"

    # Call the example task
    output = example_task(input_data)

    # Update and display progress
    update_progress(50)
    progress = get_progress()
    node_status = get_node_status("example_task")

    print(f"Progress: {progress}%")
    print(f"Example Task Status: {node_status}")
    print(f"Example Task Output: {output}")

if __name__ == "__main__":
    main()


