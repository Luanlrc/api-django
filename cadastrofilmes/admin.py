from django.contrib import admin
from cadastrofilmes import models

class FilmeAdmin (admin.ModelAdmin):
    list_display = ("nome", "autor")
    list_display_links = ("autor",)

class AutorAdmin (admin.ModelAdmin):
    list_display = ("name", "idade")

class LivroAdmin(admin.ModelAdmin):
    list_display=("nome", "autor")

admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.Filme, FilmeAdmin)
admin.site.register(models.Livro, LivroAdmin)

# Register your models here.
