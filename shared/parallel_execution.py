import threading
from shared.logging import log_event

def execute_in_parallel(tasks):
    """
    Execute a list of tasks in parallel using threads.
    Each task is a function with its arguments provided as a tuple.
    """
    threads = []
    for task, args in tasks:
        log_event(f"Starting parallel task: {args[1]}")  # Log task start
        thread = threading.Thread(target=task, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    log_event("All parallel tasks completed.")


