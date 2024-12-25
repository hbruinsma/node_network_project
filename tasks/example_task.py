from shared.state import (
    update_node_status,
    update_node_output,
    increment_completed_tasks,
    get_feedback,
    are_dependencies_completed,
)
from shared.logging import log_node_event
from shared.error_handling import handle_node_error

def example_task(input_data, node_name):
    """
    An example task with real-time logging and thread-safe state updates.
    """
    try:
        # Check dependencies
        if not are_dependencies_completed(node_name):
            log_node_event(node_name, f"Waiting for dependencies to complete...")
            update_node_status(node_name, "Waiting for Dependencies")
            return

        log_node_event(node_name, "Started execution.")
        update_node_status(node_name, "In Progress")

        # Simulate task processing
        log_node_event(node_name, f"Processing input: {input_data}")
        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()

        log_node_event(node_name, "Execution completed successfully.")
        log_node_event(node_name, f"Output: {output_data}")

    except Exception as e:
        handle_node_error(node_name, str(e))
        update_node_status(node_name, "Error")
