# Generated by Django 5.0.4 on 2024-04-23 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employees_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='position',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='salary',
        ),
    ]
