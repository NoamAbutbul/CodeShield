"""
    File to define GoogleGeminiAI.
"""


import google.generativeai as genai
from src.model.communicate_AI_interface import CommunicateAIInterface
from src.model.gemini_AI.gemini_AI_exception import GeminiAIError


class GoogleGeminiAI(CommunicateAIInterface):
    """A class to interact with the Google Gemini AI model. 
    Implements the CommunicateAIInterface
    to provide methods for configuring the model, generating content, setting the model,
    evaluating the model, and retrieving model information.
    """

    def __init__(self):
        """Initializes the GoogleGeminiAI class 
            with placeholders for the API key and model.
        """
        self.__api_key: str = None
        self.__model: genai.GenerativeModel = None

    @property
    def model(self) -> genai.GenerativeModel:
        """Gets the current AI model.

        Returns:
            genai.GenerativeModel: The current AI model.
        """
        return self.__model

    def configure(self, api_key: str):
        """Configures the AI model with the provided API key.

        Args:
            api_key (str): The API key used to authenticate and configure the AI model.
        """
        self.__api_key = api_key
        genai.configure(api_key=self.__api_key)

    def set_model(self, model_name: str):
        """Sets the AI model to be used for generating content.

        Args:
            model_name (str): The name of the AI model.
        """
        GeminiAIError.model_validate(model_name)
        self.__model = genai.GenerativeModel(model_name)

    def generate_content(self, prompt: str) -> str:
        """Generates content based on the given prompt.

        Args:
            prompt (str): The input text used to generate the content.

        Returns:
            str: The generated content.

        Raises:
            GeminiAIError: If the model is not set yet.
        """
        GeminiAIError.model_set_validate(self.__model)
        response = self.__model.generate_content(prompt)
        return response.text

    def evaluate_model(self, evaluation_data):
        """
        Evaluates the AI model using the provided evaluation data.

        Args:
            evaluation_data: The data used for evaluating the AI model.

        Raises:
            NotImplementedError: This method is not implemented yet.
        """
        raise NotImplementedError

    def get_model_info(self):
        """
        Retrieves information about the current AI model.

        Returns:
            Any: Information about the current AI model.

        Raises:
            GeminiAIError: If the model is not set yet.
        """
        GeminiAIError.model_set_validate(self.__model)
        return self.__model.get_info()
