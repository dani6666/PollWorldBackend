# Generated by Django 3.1.3 on 2021-01-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='time_needed',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='pollassignment',
            name='assigned_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
