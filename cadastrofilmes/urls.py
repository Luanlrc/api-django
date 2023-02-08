from django.urls import path, include
from . import views
from rest_framework import routers
app_name="cadastrofilmes.urls"

routers = routers.SimpleRouter()
routers.register(r"Filmes",views.FilmeViewset)
routers.register(r"Autor",views.AutorViewset)


urlpatterns=[path("Api/",include(routers.urls)) ]