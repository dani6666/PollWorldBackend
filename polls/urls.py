from django.conf.urls import url
from django.urls import path, include

from .views import GetUserPolls, GetPoll

urlpatterns = [
      path('all/', GetUserPolls.as_view()),
      path('<int:poll_id>/', GetPoll.as_view())
]