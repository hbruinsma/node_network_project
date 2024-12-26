import threading
from shared.logging import log_event
from shared.state import are_dependencies_completed

def execute_in_parallel(tasks, state):
    threads = []

    for task, args in tasks:
        node_name = args[1]

        # Access node details once to reduce redundant lookups
        node_details = state["nodes"].get(node_name, {})
        node_status = node_details.get("status", "Not Started")

        # Skip completed tasks
        if node_status == "Completed":
            print(f"Task {node_name} already completed. Skipping.")
            continue

        # Skip tasks already in progress
        if node_status == "In Progress":
            print(f"Task {node_name} is already in progress. Skipping.")
            continue

        # Check dependencies before starting
        if are_dependencies_completed(node_name):
            # Mark task as "In Progress"
            state["nodes"][node_name]["status"] = "In Progress"

            # Start task in a thread
            thread = threading.Thread(target=task_wrapper, args=(task, args, state))
            threads.append(thread)
            thread.start()
            print(f"Task {node_name} started in a thread.")
        else:
            # Mark as waiting if dependencies are not met
            state["nodes"][node_name]["status"] = "Waiting for Dependencies"
            print(f"Skipping task: {node_name} due to unmet dependencies.")

    for thread in threads:
        thread.join()

    print("All parallel tasks are completed.")

# Task wrapper to mark tasks as completed and set outputs
def task_wrapper(task, args, state):
    try:
        task(*args)
        node_name = args[1]
        # Mark task as completed
        state["nodes"][node_name]["status"] = "Completed"
        state["nodes"][node_name]["output"] = f"Processed: {args[0]}"  # Example output
    except Exception as e:
        log_event(f"Task {args[1]} failed with error: {e}")
