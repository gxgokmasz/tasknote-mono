PORT ?= 8000
BUILD ?= false
HTML ?= false

up:
ifeq ($(BUILD), true)
	docker compose down
	docker compose up --build
else
	docker compose up
endif	

dev:
	uv run manage.py runserver ${PORT}

shell:
	uv run manage.py shell

test:
ifeq ($(HTML), true)
	uv run coverage html
else
	uv run coverage run -m pytest
endif

lint:
	uv run ruff check --select I --fix --line-length 99
	uv run ruff format --line-length 99
