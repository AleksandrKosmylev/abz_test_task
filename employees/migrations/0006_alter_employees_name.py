# Generated by Django 5.0.4 on 2024-04-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employees_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ФИО'),
        ),
    ]
