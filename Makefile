dotenv:
	cp .env.example .env

test:
	pytest

makemigrations:
	src/manage.py makemigrations

migrate:
	src/manage.py migrate

drop_db:
	rm -rf src/db.sqlite3

reset_db: drop_db migrate