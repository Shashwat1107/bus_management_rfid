# Generated by Django 5.1.1 on 2024-09-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_bus_students_alter_student_register_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='students',
        ),
    ]
