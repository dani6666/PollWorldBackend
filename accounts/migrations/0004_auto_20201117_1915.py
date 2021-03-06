# Generated by Django 3.1.3 on 2020-11-17 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201112_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='hobby',
        ),
        migrations.AddField(
            model_name='customuser',
            name='growth',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='level_of_fitness',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='place_of_residence',
            field=models.IntegerField(choices=[(1, 'Village'), (2, 'City'), (3, 'Metropolis')], null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profession',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
