from unittest import mock

from django.test import TestCase

from accounts.serializers import UserSerializer
from accounts.views import UserViewSet

class UserViewSetTests(TestCase):
    def test_register(self):
        sut = UserViewSet()
        request = type('',(),{'data':{'email':'test@email.com', 'password':'pass123'}})()

        response = sut.register(request)

        self.assertEqual(response.status_code, 200)

    def test_get(self):
        sut = UserViewSet()
        request = type('',(),{'user':{'email':'test@email.com', 'password':'pass123'}})()

        response = sut.get(request)

        self.assertEqual(response.status_code, 200)

    def test_personal_update(self):
        sut = UserViewSet()
        sut.serializer_class = mock.Mock(spec=UserSerializer)

        request = type('',(),{'user':{'email':'test@email.com', 'password':'pass123'},
                              'data':{'age':'23', 'sex':'false'}})()

        response = sut.personal_update(request)

        self.assertEqual(response.status_code, 200)
