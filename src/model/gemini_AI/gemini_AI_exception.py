"""
    File to define GeminiAIError.
"""


from typing import Any
from src.exceptions import BaseException


class GeminiAIError(BaseException):
    """class to define GeminiAIError. """

    def __init__(self, message: str) -> None:
        """Initializes the GeminiAIError with message.

        Args:
            message (str): message for the exception
        """
        message = f"[GeminiAI]: {message}"
        super().__init__(message)


class ModelNameError(GeminiAIError):
    """class to define ModelNameError. """

    def __init__(self, message: str) -> None:
        """Initializes the ModelNameError with message.

        Args:
            message (str): message for the exception
        """
        message = f"[ModelName]: {message}"
        super().__init__(message)


class ModelSetError(GeminiAIError):
    """class to define ModelSetError. """

    def __init__(self, message: str) -> None:
        """Initializes the ModelSetError with message.

        Args:
            message (str): message for the exception
        """
        message = f"[ModelSet]: {message}"
        super().__init__(message)
