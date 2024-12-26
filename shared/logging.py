import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a logger
logger = logging.getLogger(__name__)

def log_event(message):
    """
    Log a general event.
    """
    logger.info(message)

def log_error(error_message):
    """
    Log an error.
    """
    logger.error(error_message)

def log_task_event(node_name, message):
    """
    Log a task-specific event.
    """
    logger.info(f"[{node_name}] {message}")
