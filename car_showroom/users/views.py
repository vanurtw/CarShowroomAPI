from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from services.services import get_tokens_for_user
from .serializers import CustomerUserSerializer, CustomerUserProfileSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CustomerUser, Profile


class RegistrationAPIView(GenericAPIView):
    serializer_class = CustomerUserSerializer

    @swagger_auto_schema(
        operation_description="Регистрация пользователя на сайте",
        responses={
            200: openapi.Response('Успешный ответ', CustomerUserSerializer),
            400: openapi.Response(
                description="Ошибка валидации",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'field': openapi.Schema(type=openapi.TYPE_STRING, description="Описание ошибок")})),
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            serializer_user_info = CustomerUserProfileSerializer(user.user_profile)
            data = tokens
            data["user_info"] = serializer_user_info.data
            return Response(data)


class UserAPIView(GenericAPIView):
    serializer_class = CustomerUserProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение полной информации о пользователе, только для авторизованных",
        responses={
            200: openapi.Response('Успешный ответ', CustomerUserProfileSerializer),
            401: openapi.Response('Пользователь не авторизован')
        }

    )
    def get(self, request):
        serializer = self.serializer_class(request.user.user_profile)
        return Response(serializer.data)


class ProfileAPIView(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение информации из профиля прользователя",
        responses={
            401:openapi.Response("Пользователь не авторизован или неверный токен")
        }
    )
    def get(self, request):
        serializer = self.serializer_class(request.user.user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Изменение данных профиля",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400:openapi.Response(
                description="Оштбка валидации",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'field':openapi.Schema(type=openapi.TYPE_STRING, description="Описание ошибки")}
                )
            )
        }
    )
    def patch(self, request):
        profile = request.user.user_profile
        serializer = self.serializer_class(instance=profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


