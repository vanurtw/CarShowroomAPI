from functools import partial

from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from services.services import get_tokens_for_user
from .serializers import CustomerUserSerializer, CustomerUserProfileSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated

from .models import CustomerUser, Profile


class RegistrationAPIView(GenericAPIView):
    serializer_class = CustomerUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            return Response(tokens)


class UserAPIView(GenericAPIView):
    serializer_class = CustomerUserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user.user_profile)
        return Response(serializer.data)


class ProfileAPIView(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user.user_profile)
        return Response(serializer.data)

    def patch(self, request):
        profile = request.user.user_profile
        serializer = self.serializer_class(instance=profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)