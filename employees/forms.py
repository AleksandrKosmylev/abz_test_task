from django import forms
from employees.models import Employees
from employees_catalog import settings


class EmployeesForm(forms.ModelForm):
    #start_date= forms.DateField(required=False, input_formats=['%d.%m.%Y'])
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    photo=forms.ImageField(label="photo")
    """
    date_of_birth = forms.DateField(
            label="Date of Birth",
            required=True,
            widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            input_formats=["%Y-%m-%d"]
        )
    """
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
