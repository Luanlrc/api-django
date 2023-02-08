from rest_framework import serializers
from cadastrofilmes import models

class FilmeSerializer (serializers.ModelSerializer):
    class Meta:
        model=models.Filme
        fields= "__all__"

class AutorSerializer (serializers.ModelSerializer):
    class Meta:
        model=models.Autor
        fields="__all__"

