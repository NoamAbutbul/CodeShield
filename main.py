"""
    Main file, run this file to run project.
"""


import sys
from src.exceptions import ExtensionError
from src import SecurityCheck


def main() -> None:
    if len(sys.argv) < 2:
        raise ExtensionError("There is not enough positions parameters")
    workspace_path = sys.argv[1]
    security_check = SecurityCheck(workspace_path)
    security_check.check()


if __name__ == "__main__":
    main()
