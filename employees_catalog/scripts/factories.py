from faker import Faker
from employees.models import Employees
import random


fake = Faker()
Faker.seed(4321)

"""
import factory
# factory.random.reseed_random(SEED)
class EmployeesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employees

    name = '3rd_Vasya'
    parent = Employees.objects.get(name='Harold')
    print(name)
"""


def run(*args):
    if 'clean_data' in args:
        Employees.objects.all().delete()
        print("Employees database successfully cleaned")
    else:
        random.seed(1234)
        head_of_depertment = []
        deputy_head_of_depertment = []
        group_head = []
        chief_specialist = []
        for tier_1 in range(2):
            name = fake.name()
            head_of_depertment.append(name)
            Employees.objects.create(name=name)
        for tier_2 in range(4):
            name = fake.name()
            deputy_head_of_depertment.append(name)
            random_parent = random.choice(head_of_depertment)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent)
        for tier_3 in range(8):
            name = fake.name()
            group_head.append(name)
            random_parent = random.choice(deputy_head_of_depertment)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent)
        for tier_4 in range(16):
            name = fake.name()
            chief_specialist.append(name)
            random_parent = random.choice(group_head)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent)
        for tier_5 in range(32):
            name = fake.name()
            random_parent = random.choice(chief_specialist)
            parent = Employees.objects.get(name=random_parent)
            Employees.objects.create(name=name, parent=parent)
        print('Employees database successfully created')
