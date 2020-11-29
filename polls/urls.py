from django.conf.urls import url
from django.urls import path, include

from .views import GetPollsSummary, GetPoll

urlpatterns = [
      path('summary/', GetPollsSummary.as_view()),
      path('poll/', GetPoll.as_view())
]