# Generated by Django 3.1.3 on 2020-12-08 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('short_description', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('time_needed', models.TimeField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'single_choice'), (1, 'multi_choice'), (2, 'text')])),
                ('text', models.TextField(max_length=500)),
                ('options', models.ManyToManyField(to='polls.QuestionOption')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='PollAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(null=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='assigned_users',
            field=models.ManyToManyField(related_name='assigned_polls', through='polls.PollAssignment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poll',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.category'),
        ),
        migrations.AddField(
            model_name='poll',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='polls.company'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(max_length=500, null=True)),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.questionoption')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
