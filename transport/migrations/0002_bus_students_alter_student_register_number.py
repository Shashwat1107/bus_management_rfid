# Generated by Django 5.1.1 on 2024-09-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='buses', to='transport.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='register_number',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
