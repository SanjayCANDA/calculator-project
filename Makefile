install:
	pip install .

install-dev:
	pip install -e .[dev]

lint:
	black --check .
	flake8 .

test:
	pytest

# Utilisé par ton job 'metrics'
metrics-all:
	pip install radon
	radon cc . -a -na
	radon mi .

# Utilisé par ton job 'build'
build:
	pip install build
	python -m build