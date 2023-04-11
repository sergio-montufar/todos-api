from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Todo
    fields = ['id', 'subject', 'details']