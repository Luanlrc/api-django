# Generated by Django 4.1.6 on 2023-02-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrofilmes', '0004_alter_autor_tipoautor_alter_filme_genero'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livros',
            new_name='Livro',
        ),
    ]