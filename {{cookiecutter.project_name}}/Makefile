clean-pyc:
	find . -name '*.pyc' -exec rm {} +
	find . -name '*.pyo' -exec rm {} +
	find . -name '*~' -exec rm {} +

# This command assumes that you have python3 installed which comes with the venv command
venv:
	python3 -m venv .venv && \
			source .venv/bin/activate && \
			pip install -r requirements.txt

# If you have pyenv installed and configured you can run this to create a virtualenv
pyenv:
	pyenv virtualenv {{cookiecutter.python_version }} {{cookiecutter.project_name}} && \
			pyenv local {{cookiecutter.project_name}}
			pip install -r requirements.txt
