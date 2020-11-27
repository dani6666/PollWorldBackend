from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from .views import ChangePersonalDataView, ChangeUserView, GetPersonalDataView

urlpatterns = [
      path('api/register/', RegisterApi.as_view()),
      path('api/update/', ChangePersonalDataView.as_view()),
      path('api/get/', GetPersonalDataView.as_view()),
      path('api/change-pass/', ChangeUserView.as_view()),
]