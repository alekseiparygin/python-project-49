install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

package-reinstall:
	pipx install --force dist/*.whl
fast:
	poetry build
	poetry publish --dry-run
	pipx install --force dist/*.whl