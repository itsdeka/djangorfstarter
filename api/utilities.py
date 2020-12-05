from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from django.core.files import File
from django.conf import settings
from django.utils import timezone
from django.http import QueryDict

from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly

from dateutil import parser

from io import BytesIO; from PIL import Image 

import calendar, json, requests

class IsAdministrator(BasePermission):
   def has_permission(self, request, view):
        authenticated = IsAuthenticated().has_permission(request, view)

        if authenticated == False: 
            return False

        user = request.user

        if user.is_superuser == False or user.is_staff == False:
            return False

        return True

class IsAdministratorOrReadOnly(BasePermission):
   def has_permission(self, request, view):
        safe = request.method in SAFE_METHODS

        if safe == False: 
            return IsAdministrator().has_permission(request, view)

        return True