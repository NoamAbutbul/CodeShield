"""
    File to define ExtensionError.
"""

from src.exceptions import BaseException


class ExtensionError(BaseException):
    """class to define ExtensionError. """

    def __init__(self, message: str) -> None:
        """Initializes the ExtensionError with message.

        Args:
            message (str): message for the exception
        """
        message = f"[Extension]: {message}"
        super().__init__(message)
