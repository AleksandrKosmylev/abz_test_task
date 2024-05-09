from django.urls import path
from employees.views import index, show_employees, EmployeeUpdateView, EmployeeCreateView, EmployeeDeleteView

urlpatterns = [
    path('', index, name="main"),
    path('employees/', show_employees, name='employees'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete')
]
