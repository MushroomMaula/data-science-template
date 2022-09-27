{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}


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