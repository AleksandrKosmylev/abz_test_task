# Generated by Django 5.0.4 on 2024-05-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_alter_employees_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='photo',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='Media/images/%Y/%m/%d'),
        ),
    ]
