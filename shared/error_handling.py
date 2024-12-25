from shared.logging import log_error

def handle_node_error(node_name, error_message):
    """
    Handle errors for a specific node and log the details.
    """
    log_error(f"Node {node_name} encountered an error: {error_message}")
