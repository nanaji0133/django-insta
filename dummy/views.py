from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class DummyGetAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "dummy get"}, status=status.HTTP_200_OK)
