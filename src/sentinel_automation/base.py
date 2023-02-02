"""sentinel_automation.base.

This Base class inherits from our LoggingBase metaclass and gives us
shared logging across any class inheriting from Base.
"""
import os
import pathlib
from typing import AnyStr

from .utils.logger import LoggingBase


class Base(metaclass=LoggingBase):
    """Base class to all other classes within this project."""

    config_manager = None
    config = None

    def _get_absolute_path(self, path: str) -> AnyStr:
        """Extracts the absolute path from a given string path.

        Args:
            path (str): The path to get the absolute path from.

        Returns:
            AnyStr: The full absolute path of a value.
        """
        try:
            if pathlib.Path(path):
                return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
        except Exception as e:
            self.__logger.critical(f"We are unable to determine the absolute path provided '{path}'. {e}")
