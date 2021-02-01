from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import random
from datetime import timedelta
from datetime import datetime

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from copouns.models import *
from accounts.views import CustomUser

# Create your views here.

#create polls for testing
def create_copouns(user: CustomUser):
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
        copoun = Copoun.objects.create(name="Kupon nr: " + str(i), company=orgs[i], price=random.randint(10, 50) * 10, category=categories[i], description="Długi opis ankiety")

        assignment = CopounAssignment.objects.create(user=user, copoun=coupon, assigned_date=None)


class GetCopouns(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        copouns = Copoun.objects.all()
        if copouns.count() == 0:
            create_copouns(user)
            copouns = user.assigned_copouns.all()

        response = []

        for copoun in copouns:
            response.append({
                'id': copoun.pk,
                'company': copoun.company.name,
                'name': copoun.name,
                'price': copoun.price,
                'category': copoun.category.name,
                'description': copoun.description,
            })

        return Response(response)


class GetUserCopouns(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user

        copouns = user.assigned_copouns.all()
        if copouns.count() == 0:
            create_copouns(user)
            copouns = user.assigned_copouns.all()

        response = []

        for copoun in copouns:
            response.append({
                'id': copoun.pk,
                'company': copoun.company.name,
                'name': copoun.name,
                'price': copoun.price,
                'category': copoun.category.name,
                'description': copoun.description,
            })

        return Response(response)


class GetCopoun(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, copoun_id):
        copoun = get_object_or_404(Copoun, pk=copoun_id)

        if not self.request.user in copoun.assigned_users.filter(pollassignment__completed_date__isnull=True):
            return Response("Copoun is not available for current user", status=status.HTTP_403_FORBIDDEN)
    
        response = {
            'id': copoun.pk,
            'company': copoun.company.name,
            'name': copoun.name,
            'price': copoun.price,
            'category': copoun.category.name,
            'description': copoun.description,
        }

        return Response(response)

    def post(self, request, copoun_id):
        copoun = get_object_or_404(Copoun, pk=copoun_id)

        if not self.request.user in copoun.assigned_users.filter(pollassignment__completed_date__isnull=True):
            return Response("Copoun is not available for current user", status=status.HTTP_403_FORBIDDEN)
        
        try:
            copoun_assingnment = CopounAssignment(user=request.user, copoun=copoun)
            copoun_assingnment.assigned_date = datetime.now()
            copoun_assingnment.save()

            request.user.points -= copoun.price
            request.user.save()
        except:
            return Response("Wrong request format", status=status.HTTP_400_BAD_REQUEST)

        return Response("Poll assigned", status=status.HTTP_200_OK)