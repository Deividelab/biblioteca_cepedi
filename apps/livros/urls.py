from django.urls import path
from . import views


app_name = 'apps.livros'

urlpatterns = [
    path('inserir_livro/', views.inserir_livro, name='inserir_livro'),
]