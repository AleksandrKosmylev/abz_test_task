from django.shortcuts import render
from .models import Employees
# Create your views here.


def index(request):
    # return render(request, 'index.html', {'workers': Employees.objects.all()})
    return render(request, 'index.html', {'workers': Employees.objects.all()})
