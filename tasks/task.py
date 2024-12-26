from shared import state
from shared.state import (
    update_node_status,
    update_node_output,
    increment_completed_tasks,
)
from shared.logging import logger, log_event, log_error, log_task_event



def summarizer_task(input_text, node_name):
    """
    Summarizer GPT function.
    """
    logger.info(f"{node_name}: Task execution started.")
    summary = f"Summary of: {input_text}"  # Replace with actual GPT summarization logic.
    state["nodes"][node_name]["output"] = summary
    state["nodes"][node_name]["status"] = "Completed"
    logger.info(f"{node_name}: Task completed with output: {summary}")

def analyzer_task(input_text, node_name):
    """
    Analyzer GPT function.
    """
    logger.info(f"{node_name}: Task execution started.")
    analysis = f"Analysis result for: {input_text}"  # Replace with GPT analysis logic.
    state["nodes"][node_name]["output"] = analysis
    state["nodes"][node_name]["status"] = "Completed"
    logger.info(f"{node_name}: Task completed with output: {analysis}")
