install : 
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint : 
	pylint project/src/pipeline.py
test:
	python -m pytest project/tests -v