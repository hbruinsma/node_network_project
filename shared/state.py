# shared/state.py
state = {
    "progress": 0,
    "total_tasks": 1,  # Start with 1 for now
    "completed_tasks": 0,
    "nodes": {}
}

def initialize_node(node_name):
    """
    Add a new node to the state with 'Not Started' status.
    """
    state["nodes"][node_name] = "Not Started"
    state["total_tasks"] += 1

def update_node_output(node_name, output):
    """
    Store the output of a specific node in the shared state.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name] = {"status": "Completed", "output": output}

def update_progress():
    """
    Update the progress percentage based on completed tasks.
    """
    if state["total_tasks"] > 0:
        state["progress"] = int((state["completed_tasks"] / state["total_tasks"]) * 100)

def increment_completed_tasks():
    """
    Increment the count of completed tasks.
    """
    state["completed_tasks"] += 1
    update_progress()

def set_total_tasks(total):
    """
    Set the total number of tasks.
    """
    state["total_tasks"] = total

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
