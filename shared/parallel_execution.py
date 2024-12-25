# shared/parallel_execution.py
import threading

def execute_in_parallel(tasks):
    """
    Execute a list of tasks in parallel using threads.
    Each task is a function with its arguments provided as a tuple.
    """
    threads = []
    for task, args in tasks:
        thread = threading.Thread(target=task, args=args)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread i
