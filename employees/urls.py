from django.urls import path
from employees.views import index, show_employees, EmployeeUpdateView

urlpatterns = [
    path('', index, name="main"),
    path('employees/', show_employees, name='employees'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employees_update'),
]
