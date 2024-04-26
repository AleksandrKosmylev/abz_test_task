# Generated by Django 5.0.4 on 2024-04-26 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='position',
            new_name='employment_position',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='date_added',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='employment_start_date',
        ),
    ]