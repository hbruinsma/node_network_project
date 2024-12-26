# tasks/progress_estimation.py
from shared.state import state
from tqdm import tqdm
from shared.logging import logger, log_event, log_error, log_task_event

# Global progress bar
progress_bar = None

def initialize_progress_bar(total_tasks=None):
    """
    Initialize a progress bar.
    If total_tasks is not provided, use the total tasks from the state.
    """
    global progress_bar
    if total_tasks is None:
        total_tasks = state.get("total_tasks", 0)
    
    progress_bar = tqdm(total=total_tasks, desc="Workflow Progress", unit="task")

def update_progress_bar():
    """
    Update the progress bar based on the number of completed tasks.
    """
    global progress_bar
    if progress_bar:
        completed_tasks = sum(1 for node in state["nodes"].values() if node.get("status") == "Completed")
        progress_bar.n = completed_tasks  # Update progress bar position
        progress_bar.refresh()

def finalize_progress_bar():
    global progress_bar
    if progress_bar is not None:
        progress_bar.close()
        progress_bar = None

def progress_estimation_node():
    """
    Display a simplified progress report with overall progress and task statuses.
    """
    print("\n=== Progress Estimation ===")
    print(f"Overall Progress: {state['progress']}%")
    for node_name, details in state["nodes"].items():
        status = details.get("status", "Unknown")
        print(f"  - {node_name}: {status}")
    print("================================")

    # Update the progress bar after logging
    update_progress_bar()