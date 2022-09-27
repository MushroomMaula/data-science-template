"""
Script that runs before the project generation phase.

Checks if the repo_name choosen by the user is a valid name for a directory

Inspired by https://github.com/crmne/cookiecutter-modern-datascience/blob/master/hooks/pre_gen_project.py
"""
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.repo_name }}"

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(
        f"ERROR: The project slug {MODULE_NAME} is not a valid Python module name. "
        "Please do not use a - and use _ instead."
    )

    # Exit to cancel project
    sys.exit(1)

