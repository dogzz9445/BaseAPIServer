from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, response, permissions

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

