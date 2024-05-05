from django.urls import path
from employees.views import index, show_employees

urlpatterns = [
    path('', index),
    path('employees/', show_employees, name='employees'),
    # path('employees/', EmployeesView.as_view(), name='employees'),
]
