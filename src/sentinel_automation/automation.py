"""Main class / entrypoint for this project."""
from typing import Dict

from .base import Base
from .configuration import ConfigurationManager


class Automation(Base):
    """Main automation class."""

    def __init__(self) -> None:
        """Main entry point, including pre-flight checks.

        We check to ensure Docker is installed before continuing.
        If it is not, we provide guidance and exit.
        """
        # First check for configuration file
        Base.config_manager = ConfigurationManager()
        if not Base.config:
            self.get_config()

    def get_config(self) -> Dict[str, str]:
        """Returns the current configuration file values.

        Returns:
            Dict[str, str]: Returns a dictionary of keys and values.
        """
        Base.config = Base.config_manager._read_from_disk(path=Base.config_manager.config_path)
        return Base.config

    def update_config(self) -> Dict[str, str]:
        """Returns the updated config, once updated.

        Returns:
            Dict[str, str]: Returns a dictionary of keys and values.
        """
        Base.config_manager._save_to_disk(path=Base.config_manager.config_path, data=Base.config_manager._prompt())
        return self.get_config()
