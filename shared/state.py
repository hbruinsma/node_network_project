from threading import Lock

# State dictionary and lock for thread-safe access
state = {
    "progress": 0,
    "total_tasks": 1,  # Start with 1 for now
    "completed_tasks": 0,
    "nodes": {}
}

state_lock = Lock()

def thread_safe(func):
    """
    Decorator to make state-modifying functions thread-safe.
    """
    def wrapper(*args, **kwargs):
        with state_lock:
            return func(*args, **kwargs)
    return wrapper

@thread_safe
def register_node(node_name, dependencies=None, priority=0):
    """
    Dynamically register a new node with optional dependencies and priority.
    """
    if node_name not in state["nodes"]:
        state["nodes"][node_name] = {
            "status": "Not Started",
            "dependencies": dependencies or [],
            "retries": 0,
            "output": None,
            "priority": priority
        }

@thread_safe
def get_priority(node_name):
    """
    Retrieve the priority of a specific node.
    """
    if node_name in state["nodes"]:
        return state["nodes"][node_name].get("priority")
    return None

@thread_safe
def add_dependency(node_name, dependency):
    """
    Add a dependency for a specific node.
    """
    if node_name not in state["nodes"]:
        initialize_node(node_name)
    state["nodes"][node_name]["dependencies"] = state["nodes"][node_name].get("dependencies", []) + [dependency]

@thread_safe
def get_dependencies(node_name):
    """
    Retrieve the dependencies for a specific node.
    """
    if node_name in state["nodes"]:
        return state["nodes"][node_name].get("dependencies", [])
    return []

@thread_safe
def are_dependencies_completed(node_name):
    """
    Check if all dependencies for a specific node are completed.
    """
    dependencies = get_dependencies(node_name)

    # Check if the node itself is already completed
    node_status = state["nodes"].get(node_name, {}).get("status", "Not Started")
    if node_status == "Completed":
        print(f"Node {node_name} is already completed.")
        return False  # Avoid re-execution of completed tasks

    # Handle nodes with no dependencies
    if not dependencies:  # No dependencies
        if node_status == "Not Started":
            print(f"Node {node_name} has no dependencies and is ready to execute.")
            return True
        else:
            print(f"Node {node_name} is not ready to execute. Current status: {node_status}")
            return False

    # Handle nodes with dependencies
    for dependency in dependencies:
        dep_status = state["nodes"].get(dependency, {}).get("status", "Not Started")
        if dep_status != "Completed":
            print(f"Dependency {dependency} for node {node_name} is not completed. Current status: {dep_status}")
            return False

    # All dependencies are completed
    print(f"All dependencies for node {node_name} are completed.")
    return True

@thread_safe
def increment_retry_count(node_name):
    """
    Increment the retry count for a specific node.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["retries"] += 1

@thread_safe
def get_retry_count(node_name):
    """
    Get the retry count for a specific node.
    """
    if node_name in state["nodes"]:
        return state["nodes"][node_name].get("retries", 0)
    return 0

@thread_safe
def add_feedback(node_name, feedback):
    """
    Add feedback for a node to trigger revisions.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["feedback"] = feedback

@thread_safe
def get_feedback(node_name):
    """
    Retrieve feedback for a specific node.
    """
    if node_name in state["nodes"]:
        return state["nodes"][node_name].get("feedback", None)
    return None

@thread_safe
def initialize_node(node_name):
    """
    Add a new node to the state with 'Not Started' status.
    """
    if node_name not in state["nodes"]:
        state["nodes"][node_name] = {
            "status": "Not Started",
            "dependencies": [],
            "retries": 0,
            "output": None,
            "priority": 0
        }
        state["total_tasks"] += 1

@thread_safe
def update_node_output(node_name, output):
    """
    Store the output of a specific node in the shared state.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["output"] = output
        state["nodes"][node_name]["status"] = "Completed"
        increment_completed_tasks()

@thread_safe
def update_progress():
    """
    Update the progress percentage based on completed tasks.
    """
    if state["total_tasks"] > 0:
        state["progress"] = int((state["completed_tasks"] / state["total_tasks"]) * 100)

@thread_safe
def increment_completed_tasks():
    """
    Increment the count of completed tasks.
    """
    state["completed_tasks"] += 1
    update_progress()

@thread_safe
def set_total_tasks(total):
    """
    Set the total number of tasks.
    """
    state["total_tasks"] = total

@thread_safe
def update_node_status(node_name, status):
    """
    Update the status of a specific node in the shared state.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["status"] = status

@thread_safe
def get_node_status(node_name):
    """
    Retrieve the status of a specific node from the shared state.
    """
    return state["nodes"].get(node_name, {}).get("status", "Not Started")

@thread_safe
def progress_estimation_node():
    """
    Logs the current progress and displays the status of all nodes.
    """
    print("=== Progress Estimation Node ===")
    print(f"Overall Progress: {state['progress']}%")
    print("Node Details:")
    for node_name, details in state["nodes"].items():
        print(f"  - {node_name}:")
        print(f"      Status: {details.get('status', 'Unknown')}")
        print(f"      Dependencies: {details.get('dependencies', [])}")
        print(f"      Retries: {details.get('retries', 0)}")
        print(f"      Output: {details.get('output', 'No Output')}")
    print("================================")

@thread_safe
def get_progress():
    """
    Retrieve the overall progress of the workflow.
    """
    return state["progress"]


