from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.db.models import Q
from .models import Employees


def index(request):
    return render(request, 'index.html', {'workers': Employees.objects.all()})


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Employees.objects.all().order_by('id')
    name_contains_query = request.GET.get('name_contains')
    employment_position_query = request.GET.get('employment_position_query')

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(name__icontains=name_contains_query)

    if is_valid_queryparam(employment_position_query):
        qs = qs.filter(Q(employment_position__icontains=employment_position_query))

    return qs


def show_employees(request):
    qs = filter(request)
    context = {}
    current_page = Paginator(list(qs), 50)
    page = request.GET.get('page')
    try:
        context['queryset'] = current_page.page(page)
    except PageNotAnInteger:
        context['queryset'] = current_page.page(1)
    except EmptyPage:
        context['queryset'] = current_page.page(current_page.num_pages)

    return render(request, "employees_list.html", context)
