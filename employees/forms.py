from django import forms
from employees.models import Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'parent', 'employment_position', 'salary', 'start_date']


CHOICES = {
    "name": "ФИО",
    "employment_position": "Должность",
    "start_date": "Дата приема на работу",
    "salary": "Зарплата",
    "parent": "Руководитель"
}


class SimpleForm(forms.Form):
    order_choice = forms.ChoiceField(
        initial="name",
        widget=forms.RadioSelect,
        choices=CHOICES, required=True,
        label="Сортировка"
    )
