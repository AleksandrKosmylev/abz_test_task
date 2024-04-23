from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employees(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    position = models.CharField(max_length=200)
    employment_start_date = models.DateTimeField(auto_now_add=False)
    salary = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
