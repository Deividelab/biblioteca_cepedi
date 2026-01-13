from django.urls import path
from apps.editoras import views

app_name = 'editoras'

urlpatterns = [
    path('inserir_editora/', views.inserir_editora, name='inserir_editora'),
    path('listar_editoras/', views.listar_editoras, name='listar_editoras'),
    path('editar_editora/<int:id>/', views.editar_editora, name='editar_editora'),
    path('excluir_editora/<int:id>/', views.excluir_editora, name='excluir_editora'),
]
