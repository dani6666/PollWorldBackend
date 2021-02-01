from django.conf.urls import url
from django.urls import path, include

from .views import GetUserCopouns, GetCopoun, GetCopouns

urlpatterns = [
      # wszystkie kupony
      path('all/', GetCopouns.as_view()),
      # wszystkie kupony uzytkownika
      path('allOwned/', GetUserCopouns.as_view()),
      # GET zwraca kupon
      # POST przypisuje kupon do uzytkownika
      path('<int:copoun_id>/', GetCopoun.as_view())
]