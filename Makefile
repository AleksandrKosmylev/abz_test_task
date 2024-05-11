add_employees:
	python manage.py runscript factories
delete_employees:
	python manage.py runscript factories --script-args clean_data
photo_employees:
	python manage.py runscript factories --script-args add_photo
run:
	python manage.py runserver
migration:
	python manage.py makemigrations
	python manage.py migrate
flush_database:
	python manage.py flush
migration_zero:
	python manage.py migrate employees zero
install:
	poetry install --no-root
shell:
	poetry shell
full_install:
	poetry install --no-root
	poetry shell
	python manage.py migrate