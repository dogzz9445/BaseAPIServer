from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.response import Response, status
from rest_framework.views import APIView

from user.viewset import *

# Create your views here.

class AudioRecognition(APIView):
    recognition_model = None

    def get(self, request, format=None):

        return Response()
        
    def post(self, request, format=None):

        return Response()
