"""
    File to load consts.yaml file
"""


import yaml

consts_file_path = r'src/configuration/consts.yaml'


with open(consts_file_path, 'r') as file:
    consts = yaml.safe_load(file)


GEMINI_MODELS_NAMES = consts['GEMINI_MODELS_NAMES']
