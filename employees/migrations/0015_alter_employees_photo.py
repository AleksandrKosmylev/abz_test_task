# Generated by Django 5.0.4 on 2024-05-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_employees_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='photo',
            field=models.ImageField(blank=True, default='media/employees_photo/jack_of_hearts.jpg', upload_to='images/%Y/%m/%d'),
        ),
    ]
