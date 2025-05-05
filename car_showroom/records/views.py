from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import RecordSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Record
from services.services import user_record_verification
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RecordAPIView(GenericAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение списка всех записей пользователя",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен")
        }
    )
    def get(self, request):
        query = request.user.user_profile.profile_records.all()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecordDetailAPIView(GenericAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение информации о записи по id",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response("Ошибка параметра: неверный id")
        }
    )
    def get(self, request, id, *args, **kwargs):
        record = get_object_or_404(Record, id=id)
        if user_record_verification(request.user, record):
            serializer = self.serializer_class(record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'This is not your post'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Обновление информации о записи по ее id",
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
    def patch(self, request, id, *args, **kwargs):
        record = get_object_or_404(Record, id=id)
        if user_record_verification(request.user, record):
            serializer = self.serializer_class(instance=record, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'This is not your post'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Удаление записи по ее id",
        responses={
            401: openapi.Response("Пользователь не авторизован или неверный токен"),
            400: openapi.Response("Ошибка параметра: неверный id")
        }
    )
    def delete(self, request, id, *args, **kwargs):
        record = get_object_or_404(Record, id=id)
        if user_record_verification(request.user, record):
            record.delete()
            return Response({'detail': 'ok'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'This is not your post'}, status=status.HTTP_200_OK)
