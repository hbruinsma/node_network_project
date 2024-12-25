import threading
from shared.logging import log_event
from shared.state import are_dependencies_completed  # Import this function

def execute_in_parallel(tasks):
    """
    Execute a list of tasks in parallel using threads.
    """
    threads = []

    for task, args in tasks:
        node_name = args[1]
        log_event(f"Checking dependencies for task: {node_name}")
        if are_dependencies_completed(node_name):  # Dependency check
            log_event(f"Starting parallel task: {node_name}")
            thread = threading.Thread(target=task, args=args)
            threads.append(thread)
            thread.start()
            log_event(f"Thread started for task: {node_name}")
        else:
            log_event(f"Skipping task {node_name} due to unmet dependencies.")

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        log_event("A thread has completed.")
    log_event("All parallel tasks completed.")




