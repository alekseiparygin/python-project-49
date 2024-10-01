install:
	poetry instal

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
