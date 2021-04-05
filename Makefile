start:
	src/manage.py runserver 0.0.0.0:8000

dotenv:
	cp .env.example .env

test:
	pytest

shell:
	src/manage.py shell_plus

makemigrations:
	src/manage.py makemigrations

migrate:
	src/manage.py migrate

drop_db:
	rm -rf src/db.sqlite3

reset_db: drop_db migrate