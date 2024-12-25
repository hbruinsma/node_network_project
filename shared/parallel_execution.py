from shared.state import are_dependencies_completed
from shared.logging import log_event
import threading

def execute_in_parallel(tasks):
    """
    Execute a list of tasks in parallel using threads.
    Only execute tasks whose dependencies are completed.
    """
    threads = []

    # Filter tasks based on dependencies
    for task, args in tasks:
        node_name = args[1]
        if are_dependencies_completed(node_name):
            log_event(f"Starting parallel task: {node_name}")
            thread = threading.Thread(target=task, args=args)
            threads.append(thread)
            thread.start()
        else:
            log_event(f"Skipping task {node_name} due to unmet dependencies.")

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    log_event("All parallel tasks completed.")
