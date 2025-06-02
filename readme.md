# Example Project

A Python project for MLOps study.

## Project Structure

```
example-project/
├── pyproject.toml    # Poetry configuration
├── setup.py          # Setuptools configuration
└── project
    ├── data
    │   ├── raw/          # Raw downloaded data
    │   └── get_data.py   # Data download script
    └── src
        └── example.py
```

## Setup

This project can be set up using either Poetry or setup.py.

### Setup.py Alternative

If you prefer using setup.py instead of Poetry:

Install the package in development mode:
   ```bash
   pip install -e .
   ```

### Poetry Setup (Recommended)

1. Install poetry
   ``` bash
   pip install poetry
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Data Management

To download the dataset:

1. Make sure you have kagglehub installed:
   ```bash
   pip install kagglehub
   ```

2. Run the data download script:
   ```bash
   python project/data/get_data.py
   ```

The data will be downloaded to `project/data/raw/` directory.

## Dependencies

- Python >= 3.10
- pandas >= 2.2.3
- matplotlib >= 3.10.3
- kagglehub (for data download)