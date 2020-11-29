from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Poll(models.Model):
    organization = models.ForeignKey(Organization, related_name='polls', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    time_needed = models.TimeField()
    rating = models.FloatField()
    assigned_users = models.ManyToManyField(CustomUser, related_name='assigned_polls', through='PollAssignment')

class PollAssignment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True)

class Question(models.Model):
    QUESTION_TYPES = [
        (0, 'single_choice'),
        (1, 'multi_choice'),
        (2, 'text')
    ]
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    type = models.IntegerField(choices=QUESTION_TYPES)
    text = models.TextField(max_length=500)

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option = models.CharField(max_length=100)

class Answer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    option = models.ForeignKey(QuestionOption, null=True, on_delete=models.CASCADE)
    text_answer = models.TextField(max_length=500, null=True)
    