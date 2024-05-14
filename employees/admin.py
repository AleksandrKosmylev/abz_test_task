from django.contrib import admin
from .models import Employees


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'employment_position', 'salary', 'start_date')


admin.site.register(Employees, SettingAdmin)
