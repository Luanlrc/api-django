from django.db import models

class TipoAutor(models.TextChoices):
    filmes = "filmes"
    livros = "livros"
    filmeslivros = "filmeslivros"

class Genero(models.TextChoices):
    terror = "terror"
    animacao = "animação"
    suspense = "suspense"
    acao = "ação"

class Autor(models.Model):
    name=models.TextField(max_length=250)
    idade=models.IntegerField()
    tipoautor=models.TextField(choices=TipoAutor.choices, null=True)
    def __str__ (self):
        return self.name

class Filme(models.Model):
    nome= models.TextField()
    lancamento=models.DateTimeField()
    descrição=models.TextField()
    autor=models.ForeignKey(Autor,on_delete=models.DO_NOTHING)
    genero=models.TextField(choices= Genero.choices, null=True)

class Livro(models.Model):
    nome= models.TextField()
    autor= models.ForeignKey(Autor,on_delete=models.DO_NOTHING)
    publicacao=models.DateTimeField()
    pages=models.IntegerField()


# Create your models here.
