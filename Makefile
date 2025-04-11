clean:
	rm -rf __pycache__ .pytest_cache .venv *.pyc *.pyo *.egg-info

format:
	poetry run black .

test:
	PYTHONPATH=src poetry run pytest

build: clean format test
