"""
    File to define SecurityCheck tool.
"""


import os
from src import API_KEY
from src.configuration import PROMPT
from src.model.gemini_AI import GoogleGeminiAI
from src.logger import logger


class SecurityCheck:
    """Class to define the SecurityCheck tool of the project.

    Attributes: 
        workspace_path (list[str]): client workspace path
    """

    def __init__(self, workspace_path: list[str]) -> None:
        """Initializing new instance of SecurityCheck class.

        Args:
            workspace_path (list[str]): client workspace path
        """
        self.__workspace_path: list[str] = workspace_path

    def check(self) -> None:
        """Check security issues for client code. """
        model = GoogleGeminiAI()
        model.configure(API_KEY)
        model.set_model('gemini-1.5-flash')
        prompt = PROMPT

        # Iterate over all files in the workspace
        for root, _, files in os.walk(self.__workspace_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not SecurityCheck.is_code_file(file_path):
                    logger.debug(f"im here with: {file_path}")
                    continue
                try:
                    with open(file_path, 'r') as f:
                        file_content = f.read()
                        prompt += f"This is {file_path}:\n{file_content}"
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

        logger.debug(f"The prompt:\n{prompt}")
        response = model.generate_content(prompt)
        logger.debug(f"The response:\n{response}")
        print(response)

    @staticmethod
    def is_code_file(file_path: str) -> bool:
        """checking if the file is code file.

        Args:
            file_path (str): file to check

        Returns:
            bool: True - if code file, else False
        """
        text_file_extensions = {'.py', '.txt', '.md',
                                '.java', '.cpp', '.js', '.html', '.css'}
        _, ext = os.path.splitext(file_path)
        return ext in text_file_extensions
