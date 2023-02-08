from rest_framework import viewsets
from cadastrofilmes import models
from cadastrofilmes import serializers
from rest_framework.permissions import IsAuthenticated

class FilmeViewset (viewsets.ModelViewSet):
    queryset=models.Filme.objects.all()
    serializer_class=serializers.FilmeSerializer
    permission_classes=[IsAuthenticated]

class AutorViewset (viewsets.ModelViewSet):
    queryset=models.Autor.objects.all()
    serializer_class=serializers.AutorSerializer
    permission_classes=[IsAuthenticated]


# Create your views here.
