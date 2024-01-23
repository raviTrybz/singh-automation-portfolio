#Makefile
.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m webportal.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m webportal.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m webportal.manage runserver

.PHONY: run-daphne
run-daphne:
	poetry run python -m webportal.manage collectstatic --no-input
	poetry run daphne webportal.project.asgi:application -p 8000 -b 127.0.0.1

.PHONY: shell
shell:
	poetry run python -m webportal.manage shell

.PHONY: superuser
superuser:
	poetry run python -m webportal.manage createsuperuser

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
