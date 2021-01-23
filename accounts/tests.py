from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory

from accounts.views import UserViewSet

class UserViewSetTests(TestCase):
    def test_register(self):
        sut = UserViewSet()
        request = type('',(),{'data':{'email':'test@email.com', 'password':'pass123'}})()

        response = sut.register(request)

        self.assertEqual(response.status_code, 200)
