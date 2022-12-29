# Logging
from functools import lru_cache
import logging

from poetry_demo.config import get_config


if get_config().logger_enabled:
    logging.basicConfig(
        format=get_config().logger_message_format or "",
        level=get_config().logger_message_level or "",
    )


@lru_cache()
def get_logger_noop() -> logging.Logger:
    """Creates :class:`logging.Logger` that does not display log records useful for testing or
     debugging

    :return: :class:`logging.Logger` object with specified name as the current module's `__name__`
    :rtype: :class:`logging.Logger`
    """
    logger = logging.getLogger(__name__)
    logger.addHandler(logging.NullHandler())
    return logger


def get_logger(logger_category: str) -> logging.Logger:
    """Retrieves named logger object if logging is enabled in :class:`AppConfig`, otherwise returns
        a noop logger

    :param logger_category: specified name to associate with :class:`logging.Logger`
    :type logger_category: str
    :return: A :class:`logging.Logger` with specified associated with the provided
        ``logger_category`` value
    :rtype: :class:`logging.Logger`
    """
    if not get_config().logger_enabled:
        return get_logger_noop()
    return logging.getLogger(logger_category)
