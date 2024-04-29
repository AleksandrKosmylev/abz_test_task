from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employees(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    employment_position = models.CharField(max_length=200)
    salary = models.IntegerField()
    start_date = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.name
        # return self.name + "Position: " + self.employment_position

    class MPTTMeta:
        order_insertion_by = ['name']
