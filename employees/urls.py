from django.urls import path
from employees.views import index, show_employees

urlpatterns = [
    path('', index, name="main"),
    path('employees/', show_employees, name='employees'),
]
