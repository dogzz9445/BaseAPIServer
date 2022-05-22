import json
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser

from api.common.file import *

class SentenceRecognition():
    def __init__(self):
        self.model = None
    
    def recognition(filename):
        
        return "dummy"

@csrf_exempt
@permission_classes((permissions.AllowAny,))
class AudioRecognitionViewSet(viewsets.ViewSet):
    parser_classes = [FileUploadParser]
    media_root = settings.MEDIA_ROOT
    recognizer = SentenceRecognition()

    def list(self, request):
        filelist = os.listdir(self.media_root)
        return Response(filelist)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        
        filepath = os.path.join(self.media_root, 'recognition', filename)
        if handle_uploaded_file(filepath, file_obj):
            contents = {'contents': self.recognizer.recognition(filepath)}            
            return Response(json.dumps(contents), status=200)    

        contents = {'contents': None}
        return Response(json.dumps(contents), status=204)
