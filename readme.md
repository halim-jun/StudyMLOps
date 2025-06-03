# Example Project (성격 분류)

A Python project for MLOps study.

## Project Structure

```
FIRST_ROUND/
├── pyproject.toml    # Poetry configuration
├── setup.py          # Setuptools configuration
└── project
    ├── data
    │   ├── personality_dataset          # Raw downloaded data
    │   └── test_data.csv   # Data download script
    │   └── train_data.csv   # Data download script
    └── src
        └── main.py
        └── pipeline.py
```

- pipeline.py : 데이터 전처리 및 머신러닝
   - 데이터 형변환
   - train test split (2:8)
   - logistic regression 
   - 결과 출력

## Setup/설정

This project can be set up using either Poetry or setup.py.
이 프로젝트는 Poetry 또는 setup.py를 사용하여 설정할 수 있습니다.



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
### Setup.py Alternative

poetry 가 더 추천되나 setup.py 도 가능

Install the package in development mode:
   ```bash
   pip install -e .
   ```

# Running the code / 코드 실행

   ```
   python project/src/main.py
   ```


