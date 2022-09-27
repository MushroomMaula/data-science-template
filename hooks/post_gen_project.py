#!/usr/bin/env python
"""
Script that runs after the project generation phase.

Sets up tools like git, pre-commit, creates the virtual env and installs 
standard datascience packages.

Inspired by https://github.com/crmne/cookiecutter-modern-datascience/blob/master/hooks/post_gen_project.py
"""
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


print(f"Current directory is: {PROJECT_DIRECTORY}")

if "{{ cookiecutter.open_source_license }}" == "Not open source":
    print("Removing LICENSE file…")
    (PROJECT_DIRECTORY / "LICENSE").unlink()


print(f"Setting up the project at {PROJECT_DIRECTORY}…")

print("Initializing git repository…")
subprocess.run(["git", "init"], cwd=PROJECT_DIRECTORY)

print("Installing python dependencies using poetry…")
subprocess.run(["poetry", "install"], cwd=PROJECT_DIRECTORY)

print("Setting up pre-commit hooks…")
subprocess.run(["poetry", "run", "pre-commit", "install"], cwd=PROJECT_DIRECTORY)

print("Setting up nbdime as diff tool for jupyter notebooks…")
subprocess.run(["poetry", "run", "nbdime", "config-git", "--enable"], cwd=PROJECT_DIRECTORY)

print("Adding ipython kernel…")
subprocess.run(["poetry", "run", "ipython", "kernel", "install",
                "--name", "python3_{{ cookiecutter.repo_name }}", "--user"], cwd=PROJECT_DIRECTORY)

