# shared/logging.py
import datetime

# shared/logging.py
import datetime

def log_event(event):
    """
    Log a workflow event with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event}")

def log_node_event(node_name, message):
    """
    Log a specific event for a given node.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{node_name}] {message}")

# shared/logging.py
def log_error(error_message):
    """
    Log an error with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] ERROR: {error_message}")
 
