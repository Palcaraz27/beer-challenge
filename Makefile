# Extract arguments of the subcommand
.PHONY: _run_args
_run_args:
  # use the rest as arguments for the subcommand
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)

build:
	docker compose build

down:
	docker compose down

up: build migrate
	docker compose up -d

restart: _run_args
	docker compose restart $(RUN_ARGS)

migrate:
	docker compose run --rm api python manage.py migrate

deps:
	docker compose run --rm api poetry install

bash:
	docker compose run --rm api /bin/sh

test: build migrate
	docker compose run --rm api python manage.py test

coverage: build migrate
	docker compose run --rm api coverage run --source='api' --omit='api/tests/*' manage.py test
	docker compose run --rm api coverage report
	docker compose run --rm api coverage xml

logs: _run_args
	docker compose logs --tail=100 $(RUN_ARGS)
