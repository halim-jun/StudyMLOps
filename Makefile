install : 
    pip install --upgrade pip && \
    pip install -r requirements.txt

format:
    isort project/ && black project/

lint : 
    flake8 project/ --max-line-length=100 && pylint project/ --fail-under=7.0
test:
    python -m pytest project/tests -v

train:
    python -m project.src.training