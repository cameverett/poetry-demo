from functools import cache
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings


class AppConfig(BaseSettings):
    """Contains environment variable config settings"""

    logger_enabled: Optional[bool] = True
    logger_message_format: Optional[str] = ""
    logger_message_level: Optional[str] = ""

    class Config:
        """Additional configuration parameters for finding and extracting environment variable
        config settings
        """

        env_prefix = "poetry_demo_"


@cache
def get_config(dotenv_path: str | None = None) -> AppConfig:
    """Load environment configuration and instantiates a cached instance :class:`AppConfig`.
    Makes use of `dotenv` package to load parameters from file or environment variables.

    :param dotenv_path: Path to .env file to load parameters, defaults to None
    :type dotenv_path: str | None, optional
    :return: A cached :class:`AppConfig` containing loaded environment variables based on
        ``dotenv_path``
    :rtype: AppConfig
    """
    load_dotenv(dotenv_path=dotenv_path)
    return AppConfig()
