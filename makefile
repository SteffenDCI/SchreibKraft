run:
	python manage.py runserver

dev-makemigrations:
	python manage.py makemigrations

dev-migrate:
	python manage.py migrate

showmigrations:
	python manage.py showmigrations

shell:
	python manage.py shell

activate:
	source .venv/bin/activate
