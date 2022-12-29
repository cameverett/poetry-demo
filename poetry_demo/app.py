from poetry_demo.log import get_logger
from poetry_demo.jo import jojojo
from poetry_demo.yo import yoyoyo


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Application startup")

    yoyoyo()
    jojojo()
    yoyoyo()

    try:
        raise ValueError
    except ValueError:
        logger.exception("value error")

    logger.info("Application shutdown")
