from poetry_demo.utils.log import get_logger

logger = get_logger(__name__)


def my_function() -> str:
    """Sample function definition"""
    logger.info("status update")
    return "Hello, World!"
