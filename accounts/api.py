from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser
#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
