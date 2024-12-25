# shared/timer.py
import time

workflow_timer = {"start_time": None, "end_time": None}

def start_timer():
    """
    Start the workflow timer.
    """
    workflow_timer["start_time"] = time.time()
    print("Workflow timer started.")

def stop_timer():
    """
    Stop the workflow timer and calculate the elapsed time.
    """
    workflow_timer["end_time"] = time.time()
    elapsed_time = workflow_timer["end_time"] - workflow_timer["start_time"]
    print(f"Workflow completed in {elapsed_time:.2f} seconds.")
