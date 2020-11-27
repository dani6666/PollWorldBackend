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
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePersonalDataView(generics.UpdateAPIView):
    """
    An endpoint for changing personal user data.
    """
    serializer_class = UserSerializer
    model = CustomUser

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.data.get("name") is not None:
            self.object.name = serializer.data.get("name")
        if serializer.data.get("age") is not None:
            self.object.age = serializer.data.get("age")
        if serializer.data.get("sex") is not None:
            self.object.sex = serializer.data.get("sex")
        if serializer.data.get("profession") is not None:
            self.object.profession = serializer.data.get("profession")
        if serializer.data.get("place_of_residence") is not None:
            self.object.place_of_residence = serializer.data.get("place_of_residence")
        if serializer.data.get("growth") is not None:
            self.object.growth = serializer.data.get("growth")
        if serializer.data.get("weight") is not None:
            self.object.weight = serializer.data.get("weight")
        if serializer.data.get("level_of_fitness") is not None:
            self.object.level_of_fitness = serializer.data.get("level_of_fitness")

        self.object.save()
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Personal data updated successfully',
            'data': []
        }

        return Response(response)


class GetPersonalDataView(generics.RetrieveAPIView):
    """
    An endpoint for changing personal user data.
    """
    serializer_class = UserSerializer
    model = CustomUser

    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Personal data updated successfully',
            'data': self.object.to_json()
        }

        return Response(response)
