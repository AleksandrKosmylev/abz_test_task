from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from PIL import Image


class Employees(MPTTModel):
    name = models.CharField(max_length=200, unique=False, verbose_name='Full name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Supervisor')
    employment_position = models.CharField(max_length=200, verbose_name='Position')
    salary = models.IntegerField(verbose_name='Salary')
    start_date = models.DateField(auto_now_add=False, verbose_name='Start_date')
    photo = models.ImageField(blank=True, upload_to='images/%Y/%m/%d')

    """
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.photo.path) # Open image using self

        if img.height > 50 or img.width > 50:
            new_img = (50, 50)
            img.thumbnail(new_img)
            img.save(self.photo.path)  # saving image at the same path
    """

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name', 'start_date']
