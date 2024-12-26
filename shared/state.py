from threading import RLock
from tqdm import tqdm
from shared.logging import logger, log_event, log_error, log_task_event

# State dictionary and lock for thread-safe access
state = {
    "progress": 0,
    "total_tasks": 1,  # Start with 1 for now
    "completed_tasks": 0,
    "nodes": {}
}

# Initialize the progress bar
progress_bar = tqdm(total=state["total_tasks"], desc="Workflow Progress", unit="task")

state_lock = RLock()

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
    Register a new node in the workflow state.
    """
    if node_name not in state["nodes"]:
        state["nodes"][node_name] = {
            "status": "Not Started",
            "dependencies": dependencies if dependencies else [],
            "retries": 0,
            "output": None,
            "priority": priority,
        }
        state["total_tasks"] = len(state["nodes"])  # Update total tasks dynamically
        log_event(f"Node registered: {node_name}, Priority: {priority}, Dependencies: {dependencies}")


@thread_safe
def add_dependency(node_name, dependency):
    """
    Add a dependency for a specific node.
    """
    if node_name not in state["nodes"]:
        register_node(node_name)
    if dependency not in state["nodes"][node_name]["dependencies"]:
        state["nodes"][node_name]["dependencies"].append(dependency)
        log_node_event(node_name, f"Added dependency: {dependency}")


@thread_safe
def are_dependencies_completed(node_name):
    """
    Check if all dependencies for a specific node are completed.
    """
    dependencies = state["nodes"][node_name].get("dependencies", [])
    for dependency in dependencies:
        status = state["nodes"][dependency]["status"]
        log_node_event(node_name, f"Checking dependency {dependency}: Status = {status}")
        if status != "Completed":
            return False
    return True


@thread_safe
def update_node_output(node_name, output):
    """
    Store the output of a specific node in the shared state and mark it as completed.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["output"] = output
        update_node_status(node_name, "Completed")
        increment_completed_tasks()
        log_node_event(node_name, f"Output updated. Task marked as completed.")


@thread_safe
def update_node_status(node_name, status):
    """
    Update the status of a node and recalculate progress.
    """
    if node_name in state["nodes"]:
        state["nodes"][node_name]["status"] = status
        log_node_event(node_name, f"Status updated to {status}.")
        update_progress()


@thread_safe
def increment_completed_tasks():
    """
    Increment the count of completed tasks and update the progress bar.
    """
    state["completed_tasks"] += 1
    state["progress"] = int((state["completed_tasks"] / state["total_tasks"]) * 100)
    progress_bar.update(1)
    log_event(f"Completed tasks: {state['completed_tasks']}/{state['total_tasks']} | Progress: {state['progress']}%")


@thread_safe
def update_progress():
    """
    Update progress percentage in the state.
    """
    state["completed_tasks"] = sum(
        1 for node in state["nodes"].values() if node["status"] == "Completed"
    )
    state["progress"] = int(
        (state["completed_tasks"] / state["total_tasks"]) * 100
    )
    log_event(f"Progress updated: {state['progress']}%")


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
        log_node_event(node_name, "Node initialized.")