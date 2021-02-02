from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, UserSerializer, RegisterSerializer
from .models import CustomUser


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    @action(detail=False)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], serializer_class=RegisterSerializer, permission_classes=[AllowAny])
    def register(self, request):
        print("Hello World !")
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

    @action(detail=False, methods=['put'])
    def personal_update(self, request):
        instance = request.user
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
