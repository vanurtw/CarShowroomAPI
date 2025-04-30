from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from services.services import get_tokens_for_user
from .serializers import CustomerUserSerializer, ProfileUserSerializer

from .models import CustomerUser, Profile


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomerUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            return Response(tokens)


class UserAPIView(APIView):
    def get(self, request):
        user = Profile.objects.get(id=1)
        serializer = ProfileUserSerializer(user)
        return Response(serializer.data)
