all:
	echo "test 	  - Run tests"
	echo "clean   - Delete generated files"
	echo "dist    - Build distribution artifacts"
	echo "release - Build distribution and release to PyPI."
	echo "dev     - Install development dependencies"


test:
	python -m pytest

clean:
	rm -rf build dist src/*.egg-info
	find src -name '__pycache__' | xargs rm -rf
	find tests -name '__pycache__' | xargs rm -rf

dev:
	python -m pip install -e .[dev]

dist: clean
	git diff --exit-code			# Check for unstaged changes
	git diff --exit-code --cached	# Check for uncommitted changes
	check-manifest
	python setup.py bdist_wheel sdist

release: dist
	twine upload dist/*.*

.PHONY: all clean dev dist test