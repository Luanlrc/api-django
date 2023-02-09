from rest_framework import viewsets
from cadastrofilmes import models
from cadastrofilmes import serializers
from rest_framework.permissions import IsAuthenticated

class FilmeViewset (viewsets.ModelViewSet):
    queryset=models.Filme.objects.all()
    serializer_class=serializers.FilmeSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        nome=self.request.query_params.get("nome")
        genero=self.request.query_params.get("genero")
        lancamento=self.request.query_params.get("lancamento")
        datalancamentofinal=self.request.query_params.get("datalancamentofinal")
        autor=self.request.query_params.getlist("autor")

        if nome:
            self.queryset=self.queryset.filter(nome=nome)
        if genero:
            self.queryset=self.queryset.filter(genero=genero)
        if lancamento and datalancamentofinal:
            self.queryset=self.queryset.filter(lancamento__gte=lancamento, lancamento__lte=datalancamentofinal)
        if autor:
            self.queryset=self.queryset.filter(autor__in=autor)
        
        
        
        return self.queryset

    

class AutorViewset (viewsets.ModelViewSet):
    queryset=models.Autor.objects.all()
    serializer_class=serializers.AutorSerializer
    permission_classes=[IsAuthenticated]

class LivroViewset (viewsets.ModelViewSet):
    queryset=models.Livro.objects.all()
    serializer_class=serializers.LivroSerializer
    permission_classes=[IsAuthenticated]


# Create your views here.
