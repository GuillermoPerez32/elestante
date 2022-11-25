from multiprocessing import context
from urllib import request
from rest_framework import status
from rest_framework.response import Response
from directorio.permissions import EsAdministrador, EsPlanificador, EsSecretario, ReadOnly
from directorio.serializers import ChangePasswordSerializer, UpdateUserSerializer, UserFromAdminModelSerializer, UserSignupSerializer

# Django REST Framework
from rest_framework import status, viewsets, generics, mixins
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Serializers
from directorio.serializers import UserLoginSerializer, UserModelSerializer

# Models
from directorio.models import User


class UserFromAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserFromAdminModelSerializer
    permission_classes = [EsAdministrador | (
        (EsSecretario | EsPlanificador) & ReadOnly)
    ]


class UserViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class SignupView(generics.GenericAPIView):
    #TODO: add permissions
    serializer_class = UserSignupSerializer
    # permission_classes = [EsAdministrador]

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):

    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(instance=user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.GenericAPIView):

    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, instance=request.user, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
