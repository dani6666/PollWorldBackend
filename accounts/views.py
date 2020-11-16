from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from .models import CustomUser



class MyTokenObtainPairView(TokenObtainPairView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = MyTokenObtainPairSerializer

class ChangeUserView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = UserSerializer
        model = CustomUser
        #permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                
                if serializer.data.get("age") is not None:
                    self.object.age = serializer.data.get("age")
                if serializer.data.get("hobby") is not None:
                    self.object.hobby = serializer.data.get("hobby")
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)