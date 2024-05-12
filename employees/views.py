import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView

from .models import Employees
from .forms import SimpleForm, EmployeesForm
from django.core.files.storage import FileSystemStorage


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


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employees
    form_class = EmployeesForm
    template_name = 'edit_form.html'
    login_url = reverse_lazy('login')
    extra_context = {
        'title': 'New Employee',
        'btn_text': 'Add employee',
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('employees')

"""
def update_employee(request, pk=None):
    employee = Employees.objects.get(pk=pk)
    if request.method != 'POST':
        form = EmployeesForm(instance=employee)

        """
"""
        # photo = request.FILES['photo']
        photo = request.FILES
        print(photo, 'photo')
        # file_name = request.FILES['photo'].name
        file_name = request.FILES.name
        fs = FileSystemStorage()
        file = fs.save(photo.name, photo)
        file_url = fs.url(file)
        report = file_name
        """
"""
    else:
        instance = get_object_or_404(Employees, pk=pk)
        form = EmployeesForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "name": instance.name,
            "instance": instance,
            "form": form
        }
    context = {'form': form}
    # redirect("employees_list.html")
    return render(request, "edit_form.html",context)
"""
"""
def update_employee(request, pk):
    employee = Employees.objects.get(id=pk)

    if request.method != 'POST':
        form = EmployeesForm(instance=employee, prefix='form')
        # request.session['return_path'] = request.META.get('HTTP_REFERER','/')
    else:
        form = EmployeesForm(request.POST, instance=employee, prefix='form')
        if form.is_valid():
            print(form.cleaned_data, 'cleaned data')
            employee = form.save(commit=False)
            image_path = employee.photo.url
            if os.path.exists(image_path):
                print('curwa')
                os.remove(image_path)
            employee.save()
            ##
            
            image_path = employee.photo.url
            print(image_path, 'image_path')


            my_field_value = form.cleaned_data
            print(my_field_value, 'myfield value')
            ##
        else:
            print('doesnt work')
        return HttpResponseRedirect(request.session['return_path'])
    context = {'form': form}
    return render(request, 'edit_form.html', context)
"""



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



class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employees
    extra_context = {
        'description': 'Are you sure you want to delete',
        'title': 'Delete employee',
        'btn_text': 'Yes, delete',
        'btn_class': 'btn-danger'}
    template_name = 'edit_form.html'
    success_url = reverse_lazy('employees')
