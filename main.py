from tasks.progress_estimation import initialize_progress_bar, finalize_progress_bar, progress_estimation_node
from shared.state import state
from shared.parallel_execution import execute_tasks
from shared.logging import logger, log_event, log_error, log_task_event

def main():
    """
    Main entry point for running the node network program.
    Initializes progress bar, executes tasks, and finalizes progress.
    """
    initialize_progress_bar()

    try:
        # Execute tasks in parallel
        execute_tasks()
        # Show final progress estimation
        progress_estimation_node()
    finally:
        # Finalize the progress bar
        finalize_progress_bar()
        print("Workflow completed successfully!")

if __name__ == "__main__":
    # Initialize state
    state["total_tasks"] = len(state["nodes"])
    main()
