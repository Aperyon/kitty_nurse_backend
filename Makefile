dotenv:
	cp .env.example .env

test:
	pytest

makemigrations:
	src/manage.py makemigrations

migrate:
	src/manage.py migrate
