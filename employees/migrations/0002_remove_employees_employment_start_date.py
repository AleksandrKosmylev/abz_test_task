# Generated by Django 5.0.4 on 2024-04-23 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='employment_start_date',
        ),
    ]
