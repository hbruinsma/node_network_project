# shared/state.py
state = {
    "progress": 0,
    "nodes": {}
}

def update_node_status(node_name, status):
    """
    Update the status of a specific node in the shared state.
    """
    state["nodes"][node_name] = status

def get_node_status(node_name):
    """
    Retrieve the status of a specific node from the shared state.
    """
    return state["nodes"].get(node_name, "Not Started")

def update_progress(progress):
    """
    Update the overall progress of the workflow.
    """
    state["progress"] = progress

def get_progress():
    """
    Retrieve the overall progress of the workflow.
    """
    return state["progress"]
