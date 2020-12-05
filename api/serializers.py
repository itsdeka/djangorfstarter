from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError, PermissionDenied

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import *

class JWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = { 'password': attrs.get('password') }

        identifier = attrs.get('username').lower()

        user = User.objects.filter(email=identifier).first() or User.objects.filter(username=identifier).first()
            
        if user is not None: credentials['username'] = user.username

        return super().validate(credentials)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def validate_password(self, value):
        validate_password(value)

        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        read_only_fields = ['points']

    class Preview(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'email']