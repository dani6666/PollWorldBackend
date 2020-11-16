from django.contrib import admin
from django.urls import path, include 
from accounts.views import MyTokenObtainPairView, ChangeUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('rest_social_auth.urls_jwt_pair')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('modify_user/', ChangeUserView.as_view()),
    path('accounts/', include("accounts.urls")),
]
