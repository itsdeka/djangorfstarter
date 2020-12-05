from django.utils.deprecation import MiddlewareMixin
from django.http import QueryDict

from rest_framework.request import Request
from rest_framework.response import Response

from api.models import *; from api.serializers import *

from dateutil import parser

from datetime import datetime

import json, urllib

class QueryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        parameters = request.GET

        data = { 
            parameter: parameters[parameter]
            for parameter in parameters 
        }

        if 'seconds' in data: data['seconds'] = int(data['seconds'])

        if 'initial' in data:
            initial = data['initial']
            
            if initial.isdigit() == True:
                decode = int(initial)

                initial = datetime.utcfromtimestamp(decode)
            else:
                decode = urllib.parse.unquote(initial)

                initial = parser.parse(decode)

            data['initial'] = timezone.make_aware(initial)

        if 'final' in data:
            final = data['final']
            
            if final.isdigit() == True:
                decode = int(final)

                final = datetime.utcfromtimestamp(decode)
            else:
                decode = urllib.parse.unquote(final)

                final = parser.parse(decode)

            data['final'] = timezone.make_aware(final)

        if 'skip' in data: data['skip'] = int(data['skip'])

        if 'limit' in data: data['limit'] = int(data['limit'])

        if 'points' in data: data['points'] = int(data['points'])

        query = QueryDict(str(), mutable=True); query.update(data)

        request.GET = query