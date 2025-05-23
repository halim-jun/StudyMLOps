# Example Project

A Python project for MLOps study.

## Project Structure

```
example-project/
├── pyproject.toml    # Poetry configuration
├── setup.py          # Setuptools configuration
└── project
    └──src
        └──example.py
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

2. Activate the virtual environment:
   ```bash
   poetry env activate
   ```