pwd := $(cat admin)

all: serve

serve:
	@echo "Serving..."
	python manage.py runserver

rm:
	cp db.sqlite3 db.sqlite3~
	@echo "Delete database"
	rm -i db.sqlite3

migrate:
	@echo "Migrate"
	python manage.py migrate

messages:
	django-admin makemessages
	django-admin compilemessages

reset_all: rm migrate
