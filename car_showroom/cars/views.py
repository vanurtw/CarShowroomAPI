from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from services.services import user_machine_verification
from rest_framework import status


class CarAPIView(GenericAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        car = request.user.user_profile.profile_cars.all()
        serializer = self.serializer_class(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarDetailAPIView(GenericAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            serializer = self.serializer_class(car, many=False)
            return Response(serializer.data)
        return Response({'detail': 'No access to this machine'}, status=status.HTTP_200_OK)

    def patch(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            serializer = self.serializer_class(instance=car, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({'detail': 'No access to this machine'}, status=status.HTTP_200_OK)

    def delete(self, request, id: int):
        car = get_object_or_404(Car, id=id)
        if user_machine_verification(request.user, car):
            car.delete()
            return Response({"detail": "ok"}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'No access to this machine'})
