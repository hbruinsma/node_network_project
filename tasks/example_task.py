# tasks/example_task.py
import time
from shared.state import update_node_status, update_node_output, increment_completed_tasks, get_feedback
from shared.error_handling import handle_node_error
from shared.config import NODE_TIMEOUT_SECONDS

def example_task(input_data):
    """
    An example task with simulated timeout handling.
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

        # Simulate task processing with a potential delay
        start_time = time.time()
        while True:
            # Simulate work
            if time.time() - start_time > NODE_TIMEOUT_SECONDS:
                raise TimeoutError(f"{node_name} exceeded timeout of {NODE_TIMEOUT_SECONDS} seconds")
            break  # End the loop early for testing purposes

        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()
        print(f"{node_name} completed. Output: {output_data}")
        return output_data

    except TimeoutError as e:
        handle_node_error(node_name, str(e))
    except Exception as e:
        handle_node_error(node_name, str(e))
