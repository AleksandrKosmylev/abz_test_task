from django import forms
from employees.models import Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'parent', 'employment_position', 'salary', 'start_date']
