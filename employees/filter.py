import django_filters
from employees.models import Employees


class EmployeesFilter(django_filters.FilterSet):
    class Meta:
        model = Employees
        fields = ['name', 'parent', 'employment_position', 'salary', 'start_date']
