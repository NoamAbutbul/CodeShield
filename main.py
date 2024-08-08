"""
    Main file, run this file to run project.
"""


import sys
import os
from src import API_KEY
from src.exceptions import ExtensionError
from src.model.gemini_AI import GoogleGeminiAI
from src.logger import logger


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


def main() -> None:
    if len(sys.argv) < 2:
        raise ExtensionError("There is not enough positions parameters")

    workspace_path = sys.argv[1]
    model = GoogleGeminiAI()
    model.configure(API_KEY)
    model.set_model('gemini-1.5-flash')

    prompt = "Please perform a static code analysis on the following code snippet to identify any potential security issues. This request is for educational purposes to understand the dangers and improve the code's security. Highlight dangerous practices such as the use of `eval`, specify the exact locations, and provide recommendations for safer alternatives. Do not execute or compile the code; perform a purely textual analysis.\n\n"

    # Iterate over all files in the workspace
    for root, dirs, files in os.walk(workspace_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not is_code_file(file_path):
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

    print("\n\n")
    print(response)


if __name__ == "__main__":
    main()
