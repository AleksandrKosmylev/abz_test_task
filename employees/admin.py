from django.contrib import admin
from .models import Employees


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'employment_position', 'salary', 'start_date')
    # list_display = [field.name for field in Employees._meta.get_fields()]

admin.site.register(Employees, SettingAdmin)
