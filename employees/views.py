from django.shortcuts import render
from .models import Employees
from django_filters.views import FilterView
from employees.filter import EmployeesFilter


def index(request):
    return render(request, 'index.html', {'workers': Employees.objects.all()})


class EmployeesView(FilterView):
    model = Employees
    filterset_class = EmployeesFilter
    ordering = ['id']
    template_name = 'employees_list.html'
