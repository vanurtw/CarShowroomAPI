from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, Record
from .serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated


class CarAPIView(GenericAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        car = request.user.user_profile.profile_cars.all()
        serializer = self.serializer_class(car, many=True)
        return Response(serializer.data)
