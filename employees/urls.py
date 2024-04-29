from django.urls import path
from employees.views import index, EmployeesView

urlpatterns = [
    path('', index),
    path('employees/', EmployeesView.as_view(), name='employees'),
]
