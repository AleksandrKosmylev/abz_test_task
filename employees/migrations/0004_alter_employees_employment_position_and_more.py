# Generated by Django 5.0.4 on 2024-04-29 13:48

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employees_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employment_position',
            field=models.CharField(max_length=200, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='employees.employees', verbose_name='Руководитель'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(verbose_name='Размер заработной платы'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='start_date',
            field=models.DateField(verbose_name='Дата приема на работу'),
        ),
    ]
