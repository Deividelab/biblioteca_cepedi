from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', include("apps.core.urls")),
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('livros/', include('apps.livros.urls', namespace='livros')),
    path('admin/', admin.site.urls),
]
