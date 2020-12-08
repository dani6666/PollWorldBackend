from django.views import View
from django.http import HttpResponse

import random
import datetime

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
            org = Company(name="Firma nr " + str(count))
            org.save()
            count += 1
        orgs = Company.objects.all()
        return orgs[0:5]

    def get_categories():
        categories = Category.objects.all()
        count = categories.count()
        while count < 5:
            cat = Category(name="Kategoria nr " + str(count))
            cat.save()
            count += 1
        categories = Category.objects.all()
        return categories[0:5]

    orgs = get_organizations()
    categories = get_categories()
    for i in range(5):
        poll = Poll(name="Ankieta nr: " + str(i), company=orgs[i], price=random.randint(10, 50) * 10, category=categories[i], short_description="Krótki opis", description="Długi opis ankiety", time_needed=datetime.time(0, random.randint(5, 15), 0), rating=random.uniform(1, 5))
        poll.save()

        option = QuestionOption(option="Opcja 1")
        option.save()

        option2 = QuestionOption(option="Opcja 2")
        option2.save()

        question = Question(poll=poll, type=0, text="Pytanie jednokrotnego wyboru")
        question.save()

        question.options.add(option)
        question.options.add(option2)

        question = Question(poll=poll, type=1, text="Pytanie wielokrotnego wyboru")
        question.save()

        question.options.add(option)
        question.options.add(option2)

        question = Question(poll=poll, type=2, text="Pytanie otwarte")
        question.save()

        assignment = PollAssignment(user=user, poll=poll, assigned_date=datetime.datetime.now(), completed_date=None)
        assignment.save()


class GetUserPolls(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        polls = user.assigned_polls.filter(pollassignment__completed_date__isnull=True)
        if polls.count() == 0: #TODO return "no polls available for user"
            create_polls(user)
            polls = user.assigned_polls.all()

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
        try:
            poll = Poll.objects.get(pk=poll_id)
        except:
            return HttpResponse("No poll with specified id") #TODO change

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
