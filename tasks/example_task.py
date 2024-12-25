# tasks/example_task.py
from shared.state import update_node_status, update_node_output, increment_completed_tasks, get_feedback
from shared.error_handling import handle_node_error

def example_task(input_data):
    """
    An example task that checks for feedback and handles revisions.
    """
    node_name = "example_task"
    try:
        feedback = get_feedback(node_name)

        # Handle feedback and perform revisions if needed
        if feedback:
            print(f"{node_name} received feedback: {feedback}")
            input_data += " [Revised]"

        update_node_status(node_name, "In Progress")
        print(f"{node_name} started with input: {input_data}")

        # Simulate task processing
        if input_data == "FAIL":
            raise ValueError("Simulated failure for testing")

        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()
        print(f"{node_name} completed. Output: {output_data}")
        return output_data

    except Exception as e:
        handle_node_error(node_name, str(e))
