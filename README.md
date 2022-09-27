Data Science Template
=====================

A simple [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating a modern (python) data science project.

## Features
- [Poetry](https://python-poetry.org) for dependency management
- [nbdime](https://nbdime.readthedocs.io) to easily version jupyter notebooks using git
- Commonly used packages like pandas, matplotlib, numpy and many more already included
- [pre-commit](https://pre-commit.com) hooks such as [isort](https://github.com/PyCQA/isort) and [black](https://github.com/psf/black) for consistent, PEP8 conform code style


## Getting started
Assuming you have [cookiecutter](https://github.com/audreyr/cookiecutter) and [poetry](https://python-poetry.org) already installed the setup is as simple as running the following line in your terminal:

```
cookiecutter gh:MushroomMaula/data-science-template
```

## Project structure
```
├─ LICENSE
├─ pyproject.toml       🠔 Configuration for poetry and other tools like black
├─ README.md            🠔 Information about your project
│
├── data
│   ├── interim         🠔 Intermediate data after some transformations have been 
│   │                     applied
│   ├── processed       🠔 Data after processing, ready to be used in your models
│   └── raw             🠔 The orginial data
│
├── docs                🠔 A folder to keep all your documentation about the project
│   └── references      🠔 Other reading material
│
├── models              🠔 Trained models, e.g. as serialized objects
│
├── notebooks           🠔 Jupyter notebooks
│   ├── exploratory     🠔 Notebooks that explore the data
│   └── reports         🠔 More polished notebooks ready to be exported
│
└── src
    ├── data            🠔 Scripts to generate/process your data
    ├── models          🠔 Scripts to train/create your models
    └── utils           🠔 Other utilities e.g. visualizations
```