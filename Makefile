SHELL := /bin/bash

.PHONY: install
install:
	python -m venv venv && source venv/bin/activate && pip --quiet install --upgrade pip && pip install -r requirements.txt

.PHONY: activate
activate:
	source venv/bin/activate

.PHONY: test
test:
	source venv/bin/activate && pytest -vvv
