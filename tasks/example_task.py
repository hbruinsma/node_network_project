from shared.state import (
    update_node_status,
    update_node_output,
    increment_completed_tasks,
)
from shared.logging import log_node_event

def example_task(input_data, node_name):
    """
    An example task with real-time logging and thread-safe state updates.
    """
    try:
        log_node_event(node_name, "Task execution started.")
        update_node_status(node_name, "In Progress")

        # Simulate task processing
        log_node_event(node_name, f"Processing input: {input_data}")
        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()

        log_node_event(node_name, "Task execution completed successfully.")
        log_node_event(node_name, f"Task output: {output_data}")
        update_node_status(node_name, "Completed")

    except Exception as e:
        log_node_event(node_name, f"Task encountered an error: {str(e)}")
        update_node_status(node_name, "Error")
