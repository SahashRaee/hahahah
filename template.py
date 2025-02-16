import os 
from pathlib import Path
import logging

project_name="my_project"


List_of_files=[".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
 ]

for filepath_str in List_of_files:
    filepath = Path(filepath_str)
    filedir = filepath.parent
    filename = filepath.name


    if filedir and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Creating an empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")