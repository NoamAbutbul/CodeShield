"""
    File to define GeminiAIError.
"""


from typing import Any
from src.exceptions import BaseException
from src.configuration import GEMINI_MODELS_NAMES


class GeminiAIError(BaseException):
    """class do define GeminiAIError. """

    @staticmethod
    def model_validate(model_name: str) -> None:
        """Validate model name

        Args:
            model_name (str): model name to validate

        Raises:
            GeminiAIError: if model name is invalid
        """
        if model_name not in GEMINI_MODELS_NAMES:
            raise GeminiAIError(
                f"Model name {model_name} does not exist\n -> available models: {GEMINI_MODELS_NAMES}")

    @staticmethod
    def model_set_validate(model: Any) -> None:
        """validate if model set.

        Args:
            model (Any): the model to validate

        Raises:
            GeminiAIError: if the model not set yet
        """
        if not model:
            raise GeminiAIError("Model not set. Call set_model first.")
