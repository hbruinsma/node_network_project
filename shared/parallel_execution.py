import threading
from shared.logging import log_event
from shared.state import are_dependencies_completed  # Import this function

def execute_in_parallel(tasks):
    threads = []

    for task, args in tasks:
        node_name = args[1]
        print(f"Preparing to execute task: {node_name}")
        if are_dependencies_completed(node_name):
            print(f"Starting task: {node_name}")
            thread = threading.Thread(target=task, args=args)
            threads.append(thread)
            thread.start()
            print(f"Task {node_name} started in a thread.")
        else:
            print(f"Skipping task: {node_name} due to unmet dependencies.")

    for thread in threads:
        thread.join()
        print("Thread completed.")
    print("All parallel tasks are completed.")
