"""
    Main file, run this file to run project.
"""


import sys
import os
from src import API_KEY
from src.model.gemini_AI import GoogleGeminiAI
from src.logger import logger


def is_text_file(file_path):
    # Define file extensions considered as text files
    text_file_extensions = {'.py', '.txt', '.md',
                            '.java', '.cpp', '.js', '.html', '.css'}
    _, ext = os.path.splitext(file_path)
    return ext in text_file_extensions


def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <workspace_path>")
        sys.exit(1)

    workspace_path = sys.argv[1]
    # print(f"Workspace path: {workspace_path}")

    model = GoogleGeminiAI()
    model.configure(API_KEY)
    model.set_model('gemini-1.5-flash')

    prompt = "Please check security issues for this code:\n"

    # Iterate over all files in the workspace
    for root, dirs, files in os.walk(workspace_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not is_text_file(file_path):
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
