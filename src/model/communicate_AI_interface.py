"""
    File to define CommunicateAIInterface
"""


from abc import ABC, abstractmethod


class CommunicateAIInterface(ABC):
    """An abstract base class for communicating with AI models. 
        This interface defines the essential methods 
        that any AI communication implementation should provide.
    """

    @abstractmethod
    def configure(self, api_key: str):
        """Configures the AI model with the provided API key.

        Args:
            api_key (str): The API key used to authenticate and configure the AI model.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_content(self, prompt: str) -> str:
        """Generates content based on the given prompt.

        Args:
            prompt (str): The input text used to generate the content.

        Returns:
            str: The generated content.
        """
        raise NotImplementedError

    @abstractmethod
    def set_model(self, model_name: str):
        """Sets the AI model to be used for generating content.

        Args:
            model_name (str): The name of the AI model.
        """
        raise NotImplementedError

    @abstractmethod
    def evaluate_model(self, evaluation_data):
        """Evaluates the AI model using the provided evaluation data.

        Args:
            evaluation_data: The data used for evaluating the AI model.
        """
        raise NotImplementedError

    @abstractmethod
    def get_model_info(self):
        """Retrieves information about the current AI model.

        Returns:
            Any: Information about the current AI model.
        """
        raise NotImplementedError
