from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi
from .views import ChangePersonalDataView, ChangeUserView

urlpatterns = [
      path('api/register/', RegisterApi.as_view()),
      path('api/update/', ChangeUserView.as_view()),
      path('api/change-pass/', ChangePersonalDataView.as_view()),
]