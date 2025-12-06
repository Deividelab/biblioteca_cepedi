from django.contrib import messages

from .forms import LivroForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def inserir_livro(request):
    template_name = 'livros/form_livro.html'
    if request.method == 'POST':
        form = LivroForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do Livro foi realizado com sucesso!')
        return redirect('livros:listar_livros')
    form = LivroForm()
    context = {'form': form}
    return render(request, template_name, context)