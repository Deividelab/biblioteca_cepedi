from django.contrib import messages

from .forms import EditoraForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Editora

def inserir_editora(request):
    template_name = 'editoras/form_editora.html'
    if request.method == 'POST':
        form = EditoraForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do editora foi realizado com sucesso!')
        return redirect('editoras:listar_editoras')
    form = EditoraForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_editoras(request):
    template_name = 'editoras/listar_editoras.html'
    editoras = Editora.objects.all()
    context = {'editoras': editoras}
    return render(request, template_name, context)

def editar_editora(request, id):
    template_name = 'editoras/form_editora.html'
    editora = get_object_or_404(Editora, id=id)
    form = EditoraForm(request.POST or None, request.FILES or None, instance=editora)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('editoras:listar_editoras')
    return render(request, template_name, context)

def excluir_editora(request, id):
    template_name = 'editoras/excluir_editora.html'
    editora = Editora.objects.get(id=id)
    context = {'editora': editora}
    if request.method == "POST":
        editora.delete()
        messages.error(request, 'O Editora foi excluído com sucesso.')
        return redirect('editoras:listar_editoras')
    return render(request, template_name, context)