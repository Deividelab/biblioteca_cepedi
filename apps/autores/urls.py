from django.urls import path
from apps.autores import views

app_name = 'apps.autores'

urlpatterns = [
    path('inserir_autor/', views.inserir_autor, name='inserir_autor'),
    path('listar_autores/', views.listar_autores, name='listar_autores'),
    path('editar_autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('excluir_autor/<int:id>/', views.excluir_autor, name='excluir_autor'),
]