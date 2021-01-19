from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import random
from datetime import timedelta

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from polls.models import *
from accounts.views import CustomUser

# Create your views here.

#create polls for testing
def create_polls(user: CustomUser):
    def get_organizations():
        orgs = Company.objects.all()
        count = orgs.count()
        while count < 5:
            Company.objects.create(name="Firma nr " + str(count))
            count += 1
        orgs = Company.objects.all()
        return orgs[0:5]

    def get_categories():
        categories = Category.objects.all()
        count = categories.count()
        while count < 5:
            Category.objects.create(name="Kategoria nr " + str(count))
            count += 1
        categories = Category.objects.all()
        return categories[0:5]

    orgs = get_organizations()
    categories = get_categories()
    for i in range(5):
        poll = Poll.objects.create(name="Ankieta nr: " + str(i), company=orgs[i], price=random.randint(10, 50) * 10, category=categories[i], short_description="Krótki opis", description="Długi opis ankiety", time_needed=timedelta(minutes=random.randint(5, 15)), rating=random.uniform(1, 5))

        option = QuestionOption.objects.create(option="Opcja 1")

        option2 = QuestionOption.objects.create(option="Opcja 2")

        question = Question.objects.create(poll=poll, type=0, text="Pytanie jednokrotnego wyboru")

        question.options.add(option)
        question.options.add(option2)

        question = Question.objects.create(poll=poll, type=1, text="Pytanie wielokrotnego wyboru")

        question.options.add(option)
        question.options.add(option2)

        question = Question.objects.create(poll=poll, type=2, text="Pytanie otwarte")

        assignment = PollAssignment.objects.create(user=user, poll=poll, completed_date=None)


class GetUserPolls(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        polls = user.assigned_polls.filter(pollassignment__completed_date__isnull=True)
        if polls.count() == 0: #TODO return "no polls available for user"
            create_polls(user)
            polls = user.assigned_polls.filter(pollassignment__completed_date__isnull=True)

        response = []

        for poll in polls:
            response.append({
                'id': poll.pk,
                'company': poll.company.name,
                'name': poll.name,
                'price': poll.price,
                'category': poll.category.name,
                'short-descripption': poll.short_description,
                'description': poll.description,
                'time': str(poll.time_needed),
                'rate': poll.rating
            })

        return Response(response)


class GetPoll(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)

        if not self.request.user in poll.assigned_users.all():
            return HttpResponse("Poll is not available for current user") #TODO change
    
        questions = []

        for q in poll.questions.all():
            options = []
            for o in q.options.all():
                options.append({
                    'id': o.pk,
                    'option': o.option
                })
            questions.append({
                'id': q.pk,
                'type': q.get_type_display(),
                'text': q.text,
                'options': options
            })

        response = {
            'id': poll.pk,
            'company': poll.company.name,
            'name': poll.name,
            'price': poll.price,
            'category': poll.category.name,
            'short-descripption': poll.short_description,
            'description': poll.description,
            'time': str(poll.time_needed),
            'rate': poll.rating,
            'questions': questions
        }

        return Response(response)
