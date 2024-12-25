# tasks/example_task.py
from shared.state import update_node_status, update_node_output, increment_completed_tasks, get_dependencies, are_dependencies_completed
from shared.error_handling import handle_node_error

def example_task(input_data, node_name):
    """
    An example task that waits for dependencies to complete.
    """
    try:
        # Check dependencies
        if not are_dependencies_completed(node_name):
            print(f"{node_name} is waiting for dependencies to complete...")
            return  # Skip execution if dependencies are not ready

        update_node_status(node_name, "In Progress")
        print(f"{node_name} started with input: {input_data}")

        # Simulate task processing
        output_data = f"Processed: {input_data}"

        # Save the output and update state
        update_node_output(node_name, output_data)
        increment_completed_tasks()
        print(f"{node_name} completed. Output: {output_data}")
        return output_data

    except Exception as e:
        handle_node_error(node_name, str(e))
