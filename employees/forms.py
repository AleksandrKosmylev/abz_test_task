from django import forms
from employees.models import Employees
from employees_catalog import settings


class EmployeesForm(forms.ModelForm):
    # start_date = models.DateField(auto_now_add=False, verbose_name='Start_date')
    # start_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Employees
        fields = ['name', 'parent', 'employment_position', 'salary', 'start_date']


CHOICES = {
    "name": "Full name",
    "employment_position": "Position",
    "start_date": "Start date",
    "salary": "Salary",
    "parent": "Supervisor"
}


class SimpleForm(forms.Form):
    order_choice = forms.ChoiceField(
        initial="name",
        widget=forms.RadioSelect,
        choices=CHOICES, required=True,
        label="Sort by"
    )
