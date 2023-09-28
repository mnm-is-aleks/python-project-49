install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain_games:
	 poetry run brain-games

brain_calc:
	 poetry run python -m brain_games.scripts.brain_calc

brain_even:
	 poetry run python -m brain_games.scripts.brain_even

brain_gcd:
	 poetry run python -m brain_games.scripts.brain_gcd

brain_prime:
	 poetry run python -m brain_games.scripts.brain_prime

brain_progression:
	 poetry run python -m brain_games.scripts.brain_progression



.PHONY: install build publish lint
