from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Employees
from .forms import SimpleForm, EmployeesForm


def index(request):
    return render(request, 'index.html', {'workers': Employees.objects.all()})


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter_employee(request):
    # qs = Employees.objects.all().order_by('id')
    qs = Employees.objects.all()
    name_contains_query = request.GET.get('name_contains')
    employment_position_query = request.GET.get('employment_position_query')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    salary_min = request.GET.get('salary_min')
    salary_max = request.GET.get('salary_max')

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    if is_valid_queryparam(employment_position_query):
        qs = qs.filter(Q(employment_position__icontains=employment_position_query))

    if is_valid_queryparam(date_min):
        qs = qs.filter(start_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(start_date__lt=date_max)

    if is_valid_queryparam(salary_min):
        qs = qs.filter(salary__gte=salary_min)

    if is_valid_queryparam(salary_max):
        qs = qs.filter(salary__lt=salary_max)

    return qs


@login_required(login_url="/users/login/")
def show_employees(request):

    form = SimpleForm()
    context = {'form': form}
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            choice = list(form.cleaned_data.values())[0]
            context = {'form': form}
            qs = filter_employee(request).order_by(choice)
        else:
            raise Http404
    else:
        qs = filter_employee(request).order_by('id')

    current_page = Paginator(list(qs), 50)
    page = request.GET.get('page')
    try:
        context['queryset'] = current_page.page(page)
    except PageNotAnInteger:
        context['queryset'] = current_page.page(1)
    except EmptyPage:
        context['queryset'] = current_page.page(current_page.num_pages)

    return render(request, "employees_list.html", context)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    form_class = EmployeesForm
    login_url = reverse_lazy('login')
    extra_context = {
        'title': 'Edit employee',
        'btn_text': 'Update',
        'btn_class': 'btn-primary'}
    template_name = 'edit_form.html'
    success_url = reverse_lazy('employees')
