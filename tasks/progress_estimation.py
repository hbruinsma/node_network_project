# tasks/progress_estimation.py
from shared.state import state

def progress_estimation_node():
    """
    Logs detailed progress information, including node statuses,
    dependencies, retries, and overall progress.
    """
    print("=== Progress Estimation Node ===")
    print(f"Overall Progress: {state['progress']}%")
    print("Node Details:")
    for node_name, details in state["nodes"].items():
        status = details.get("status", "Unknown")
        dependencies = details.get("dependencies", [])
        retries = details.get("retries", 0)
        output = details.get("output", "No Output")
        print(f"  - {node_name}:")
        print(f"      Status: {status}")
        print(f"      Dependencies: {dependencies}")
        print(f"      Retries: {retries}")
        print(f"      Output: {output}")
    print("================================")
