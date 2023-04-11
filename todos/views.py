from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  # optional permission class set permission level
  permission_classes = [permissions.AllowAny] # Could be [permissions.IsAuthenticated]
  
