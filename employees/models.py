from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employees(MPTTModel):
    name = models.CharField(max_length=200, unique=False, verbose_name='ФИО')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Руководитель')
    employment_position = models.CharField(max_length=200, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Размер заработной платы')
    start_date = models.DateField(auto_now_add=False, verbose_name='Дата приема на работу')

    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by = ['name']
