from django.core.exceptions import PermissionDenied, ValidationError
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.cache import cache_page

from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

from api.models import *; from api.serializers import *

from api.utilities import IsAdministrator, IsAdministratorOrReadOnly

from api import utilities

@api_view(['GET'])
@permission_classes([IsAdministrator])
def user(request: Request, user: int = None) -> Response:
    user = get_object_or_404(User, id=user)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['HEAD'])
@permission_classes([AllowAny])
def tmp(request: Request) -> Response:
    pass

class Users(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request: Request) -> Response:
        serializer = UserSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request) -> Response:
        serializer = UserSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request) -> Response:
        request.user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
