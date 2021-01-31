from django.conf.urls import url
from django.urls import path, include

from .views import GetUserCopouns, GetCopoun

urlpatterns = [
      path('all/', GetUserCopouns.as_view()),
      path('<int:copoun_id>/', GetCopoun.as_view())
]