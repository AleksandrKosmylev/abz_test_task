from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employees(MPTTModel):
    name = models.CharField(max_length=200, unique=False, verbose_name='Full name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Supervisor')
    employment_position = models.CharField(max_length=200, verbose_name='Position')
    salary = models.IntegerField(verbose_name='Salary')
    start_date = models.DateField(auto_now_add=False, verbose_name='Start_date')
    #employment_photo = models.ImageField(blank=True, upload_to='images/%Y/%m/%d', help_text='150x150px', verbose_name='employment_photo')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name', 'start_date']
