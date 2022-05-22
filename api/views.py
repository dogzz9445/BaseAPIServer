import os
from django.conf import settings
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser

from api.common.file import *

from api.user.viewset import *
from api.sentence.viewset import *

# Create your views here.

@permission_classes((permissions.AllowAny,))
class UploadViewSet(viewsets.ViewSet):
    parser_classes = [FileUploadParser]
    media_root = settings.MEDIA_ROOT

    def list(self, request):
        filelist = os.listdir(self.media_root)
        return response.Response(filelist)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        handle_uploaded_file(self.media_root + '/' + filename, file_obj)

        return response.Response(status=204)
