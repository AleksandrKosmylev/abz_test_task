from faker import Faker
from employees.models import Employees
import random
from datetime import datetime
from django.core.files import File

from employees_catalog.settings import MEDIA_ROOT

fake = Faker(['ru_RU', 'en_US', 'de_DE', 'it_IT', 'fr_FR'])
Faker.seed(1234)


import os
import random
# directory = 'media/employees_photo'
directory = os.path.join(MEDIA_ROOT, 'employees_photo')
files = os.listdir(directory)
file = random.choice(files)
# with open(os.path.join(directory, file), 'r') as f:
    


def run(*args):
    if 'clean_data' in args:
        Employees.objects.all().delete()
        print("Employees database successfully cleaned")
    elif 'add_photo' in args:

        for employee in Employees.objects.all():
            # print(employee.values('name'))
            print(employee.id)
        x = Employees.objects.get(id=703)
        with open(os.path.join(directory, file), 'rb') as f:
            x.photo.save("1.jpg", File(f), save=True)
        x.save()
        print(x.name)
    else:
        positions = [
            'head of depertment',
            'deputy head of depertment',
            'group head',
            'chief specialist',
            'specialist'
        ]
        salaries = [
            250000,
            200000,
            150000,
            100000,
            80000
        ]
        # random.seed(1234)
        head_of_depertment = []
        deputy_head_of_depertment = []
        group_head = []
        chief_specialist = []
        for tier_1 in range(2):
            f_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2023, 12,  31))
            name = fake.name()
            head_of_depertment.append(name)
            Employees.objects.create(name=name, employment_position=positions[0], salary=salaries[0], start_date=f_date)
        for tier_2 in range(4):
            f_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2023, 12, 31))
            name = fake.name()
            deputy_head_of_depertment.append(name)
            random_parent = random.choice(head_of_depertment)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent, employment_position=positions[1], salary=salaries[1], start_date=f_date)
        for tier_3 in range(8):
            f_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2023, 12, 31))
            name = fake.name()
            group_head.append(name)
            random_parent = random.choice(deputy_head_of_depertment)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent, employment_position=positions[2], salary=salaries[2], start_date=f_date)
        for tier_4 in range(16):
            f_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2023, 12, 31))
            name = fake.name()
            chief_specialist.append(name)
            random_parent = random.choice(group_head)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent, employment_position=positions[3], salary=salaries[3], start_date=f_date)
        for tier_5 in range(50000):
            f_date = fake.date_between_dates(date_start=datetime(2000, 1, 1), date_end=datetime(2023, 12, 31))
            name = fake.name()
            random_parent = random.choice(chief_specialist)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent, employment_position=positions[4], salary=salaries[4], start_date=f_date)
        print('Employees database successfully created')
