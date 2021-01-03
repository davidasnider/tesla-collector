SHELL := /bin/zsh

setup-dev:
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip3 install -r src/requirements.txt && \
	pip3 install -r src/test-requirements.txt
