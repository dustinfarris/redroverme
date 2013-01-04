test: lint test-python

develop:
	pip install "flake8>=1.7" --use-mirrors
	pip install ipdb --use-mirrors
	pip install -r requirements-development.txt --use-mirrors
	pip install -r requirements-test.txt --use-mirrors
	pip install -r requirements.txt --use-mirrors
	easy_install readline
	touch redroverme/settings/__init__.py

test-python:
	@echo "Running Python tests"
	python manage.py test || exit 1
	@echo ""

lint: lint-python

lint-python:
	@echo "Linting Python files"
	flake8 --ignore=E111,E121,W404 --exclude=./env/*,migrations,.git . || exit 1
	@echo ""
