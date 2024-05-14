from django import forms
from employees.models import Employees


class EmployeesForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ['name', 'parent', 'employment_position', 'salary', 'start_date', 'photo']


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
