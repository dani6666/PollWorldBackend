from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Poll(models.Model):
    company = models.ForeignKey(Company, related_name='polls', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    short_description = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    time_needed = models.DurationField()
    rating = models.FloatField()
    assigned_users = models.ManyToManyField(CustomUser, related_name='assigned_polls', through='PollAssignment')

class PollAssignment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True)

class QuestionOption(models.Model):
    option = models.CharField(max_length=100)

class Question(models.Model):
    QUESTION_TYPES = [
        (0, 'single_choice'),
        (1, 'multi_choice'),
        (2, 'text')
    ]
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    type = models.IntegerField(choices=QUESTION_TYPES)
    text = models.TextField(max_length=500)
    options = models.ManyToManyField(QuestionOption)

class Answer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    option = models.ForeignKey(QuestionOption, null=True, on_delete=models.CASCADE)
    text_answer = models.TextField(max_length=500, null=True)
    