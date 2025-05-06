from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from services.services import user_machine_verification
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CarAPIView(GenericAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение списка всех машин пользователя",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен")
        }
    )
    def get(self, request):
        car = request.user.user_profile.profile_cars.all()
        serializer = self.serializer_class(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Добавление машины",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response("Ошибка валидации")
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile_user=request.user.user_profile)
        return Response(serializer.data)


class CarDetailAPIView(GenericAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение информации о машине по id",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response("Ошибка параметра: неверный id")
        }
    )
    def get(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            serializer = self.serializer_class(car, many=False)
            return Response(serializer.data)
        return Response({'detail': 'No access to this machine'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Обновление информации о машине по ее id",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response(
                description="Ошибка параметра или валидации данных",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'field': openapi.Schema(type=openapi.TYPE_STRING, description="Описание ошибки")}
                )
            )

        }
    )
    def patch(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            serializer = self.serializer_class(instance=car, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({'detail': 'No access to this machine'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удаление машины по ее id",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response("Ошибка параметра: неверный id")
        }
    )
    def delete(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            car.delete()
            return Response({"detail": "ok"}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'No access to this machine'}, status=status.HTTP_400_BAD_REQUEST)
