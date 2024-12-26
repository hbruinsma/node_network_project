import threading
from shared.logging import log_node_event
from shared.state import are_dependencies_completed

import threading
from shared.logging import logger, log_event, log_error, log_task_event


from shared.logging import logger, log_task_event, log_error

def execute_in_parallel(tasks, state):
    logger.info("Starting parallel execution of tasks.")
    threads = []

    for task, args in tasks:
        node_name = args[1]
        node_status = state["nodes"].get(node_name, {}).get("status", "Not Started")

        if node_status in ["Completed", "In Progress"]:
            log_task_event(node_name, f"Task already {node_status}. Skipping.")
            continue

        if are_dependencies_completed(node_name):
            log_task_event(node_name, "Dependencies met. Starting execution.")
            state["nodes"][node_name]["status"] = "In Progress"
            thread = threading.Thread(target=task_wrapper, args=(task, args, state))
            threads.append(thread)
            thread.start()
        else:
            log_task_event(node_name, "Skipping due to unmet dependencies.")
            state["nodes"][node_name]["status"] = "Waiting for Dependencies"

    for thread in threads:
        thread.join()

    remaining_tasks = [(task, args) for task, args in tasks if state["nodes"][args[1]]["status"] != "Completed"]
    if remaining_tasks:
        logger.info("Some tasks remain incomplete. Re-executing remaining tasks.")
        execute_in_parallel(remaining_tasks, state)
    else:
        logger.info("All tasks have been executed successfully.")




def task_wrapper(task, args, state):
    node_name = args[1]
    try:
        logger.info(f"Task {node_name}: Starting execution.")
        output = task(*args)  # Call the actual task function
        state["nodes"][node_name]["status"] = "Completed"
        state["nodes"][node_name]["output"] = output
        logger.info(f"Task {node_name}: Execution completed successfully. Output: {output}")
    except Exception as e:
        logger.error(f"Task {node_name}: Execution failed with error: {e}")
        state["nodes"][node_name]["status"] = "Error"
        state["nodes"][node_name]["output"] = None



