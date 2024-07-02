"""
    File to define the logger of the project.
"""

import logging
import os


class ProjectLogger(logging.Logger):
    """Class to define the logger of the project.

    Attributes: 
        log_dir (str): name of the directory for the log file
        log_file (str): log file path
    """

    def __init__(self, name, log_dir: str = "logs", log_level: int = logging.DEBUG) -> None:
        """Initializing new instance of ProjectLogger class.

        Args:
            name (str): name of the logger.
            log_dir (str, optional): name of the directory for the log file. Defaults to 'logs'.
            log_level (int, optional): logging level for the logger. Defaults to logging.DEBUG.
        """
        super().__init__(name, log_level)
        self.__log_dir = log_dir
        os.makedirs(self.__log_dir, exist_ok=True)
        self.__log_file = os.path.join(self.__log_dir, "system_logger.log")
        self.__setup_handlers()

    def __setup_handlers(self) -> None:
        """Setting up the handlers for the logger."""

        # Create a file handler
        file_handler = logging.FileHandler(self.__log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter(
            '%(asctime)s - %(module)s: %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.addHandler(file_handler)
        self.addHandler(console_handler)

    def clear_log_file(self) -> None:
        """Clear the log file. 

        Raises:
            FileNotFoundError: if the log file does not exist
        """
        if os.path.exists(self.__log_file):
            with open(self.__log_file, 'w'):
                pass
            self.info("Log file cleared.")
        else:
            raise FileNotFoundError(f"{self.__log_file} does not exist")


# Configure logging to use ProjectLogger class
logging.setLoggerClass(ProjectLogger)
logger = logging.getLogger('project_logger')
