from poetry_demo.utils.log import get_logger
from poetry_demo.example import my_function


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Application startup")

    my_function()

    try:
        raise ValueError
    except ValueError:
        logger.exception("value error")

    logger.info("Application shutdown")
