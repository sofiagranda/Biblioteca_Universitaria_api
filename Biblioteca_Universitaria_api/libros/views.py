
from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
