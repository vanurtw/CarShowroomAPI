from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import RecordSerializer
from rest_framework.permissions import IsAuthenticated


class RecordAPIView(GenericAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.user.user_profile.profile_records.all()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)
