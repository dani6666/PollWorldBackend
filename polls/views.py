from django.views import View
from django.http import HttpResponse

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
        orgs = Organization.objects.all()
        count = orgs.count()
        if count < 5:
            while count < 5:
                org = Organization(name="sample org" + str(count))
                org.save()
                count += 1
            orgs = Organization.objects.all()
        return orgs[0:5]

    orgs = get_organizations()
    for i in range(5):
        poll = Poll(name="sample poll" + str(i), organization=orgs[i], description="description", time_needed=datetime.time(0, 5 + i, 0), rating=3.6)
        poll.save()

        question = Question(poll=poll, type=0, text="single choice question")
        question.save()

        option = QuestionOption(question=question, option="option1")
        option.save()

        option = QuestionOption(question=question, option="option2")
        option.save()

        question = Question(poll=poll, type=1, text="multi choice question")
        question.save()

        option = QuestionOption(question=question, option="option1")
        option.save()

        option = QuestionOption(question=question, option="option2")
        option.save()

        question = Question(poll=poll, type=2, text="open question")
        question.save()

        assignment = PollAssignment(user=user, poll=poll, assigned_date=datetime.datetime.now(), completed_date=None)
        assignment.save()


class GetUserPolls(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        print(user)
        if not user.is_authenticated:
            return HttpResponse("User not logged in") #TODO change

        polls = user.assigned_polls.filter(pollassignment__completed_date__isnull=True)
        if polls.count() == 0: #TODO return "no polls available for user"
            create_polls(user)
            polls = user.assigned_polls.all()

        response = []

        for poll in polls:
            response.append({
                'id': poll.pk,
                'organization': poll.organization.name,
                'name': poll.name,
                'time_needed': str(poll.time_needed),
                'description': poll.description,
                'rating': poll.rating
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
            'organization': poll.organization.name,
            'name': poll.name,
            'time_needed': str(poll.time_needed),
            'description': poll.description,
            'rating': poll.rating,
            'questions': questions
        }

        return Response(response)
