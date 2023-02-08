from django.db import models

class Autor(models.Model):
    nome=models.TextField(max_length=250)
    idade=models.IntegerField()
    
    def __str__ (self):
        return self.nome
        
class Genero(models.IntegerChoices):
    terror = 0
    animacao = 1
    suspense = 2
    acao = 3
 

class Filme(models.Model):
    nome= models.TextField()
    lancamento=models.DateTimeField()
    descrição=models.TextField()
    autor=models.ForeignKey(Autor,on_delete=models.DO_NOTHING)
    genero=models.IntegerField(choices= Genero.choices, null=True)

# Create your models here.
