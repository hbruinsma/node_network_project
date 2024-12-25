# tasks/example_task.py
from shared.state import update_node_status, update_node_output, increment_completed_tasks, get_feedback, increment_retry_count, get_retry_count
from shared.error_handling import handle_node_error
from shared.config import NODE_TIMEOUT_SECONDS

MAX_RETRIES = 3  # Define the maximum number of retries

def example_task(input_data):
    """
    An example task with retry logic for failures and timeouts.
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
            if time.time() - start_time > NODE_TIMEOUT_SECONDS:
                raise TimeoutError(f"{node_name} exceeded timeout of {NODE_TIMEOUT_SECONDS} seconds")
            break  # End the loop early for testing purposes

        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()
        print(f"{node_name} completed. Output: {output_data}")
        return output_data

    except (TimeoutError, Exception) as e:
        increment_retry_count(node_name)
        retries = get_retry_count(node_name)
        if retries <= MAX_RETRIES:
            print(f"{node_name} retrying ({retries}/{MAX_RETRIES})...")
            return example_task(input_data)  # Retry the task
        else:
            handle_node_error(node_name, f"{str(e)} (Max retries reached)")
