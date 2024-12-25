# tasks/example_task.py
from shared.state import update_node_status, get_node_status

def example_task(input_data):
    """
    An example task that updates its status in the shared state.
    """
    node_name = "example_task"
    update_node_status(node_name, "In Progress")
    print(f"{node_name} started with input: {input_data}")

    # Simulate task processing
    output_data = f"Processed: {input_data}"

    update_node_status(node_name, "Completed")
    print(f"{node_name} completed. Output: {output_data}")
    return output_data
