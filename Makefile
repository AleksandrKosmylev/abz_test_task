add_employees:
	python manage.py runscript factories
delete_employees:
	python manage.py runscript factories --script-args clean_data
run:
	python manage.py runserver
