import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Tarefas
from .forms import TarefaForm
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.done = 'doing'
            tarefa.save()
            messages.info(request, 'Tarefa criada com sucesso!')
    
    search = request.GET.get('search')

    if search:
        tarefas_lista = Tarefas.objects.filter(titulo__icontains=search)
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    else:
        tarefas_lista = Tarefas.objects.all().order_by('termino')
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    return render(request, "tarefas/home.html", {"tarefas": tarefas})

def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefaForm(instance=tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            messages.info(request, 'Tarefa editada com sucesso!')
            return redirect('/tarefas/')
        else:
            return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})
    else:
        return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})

def delTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/tarefas/')

def verTarefa(request, encoded_id):
    decoded_id = base64.b64decode(encoded_id).decode('utf-8')
    tarefa = get_object_or_404(Tarefas, pk=decoded_id)
    return render(request, 'tarefas/tarefa.html', {"tarefa": tarefa})

def cadastroTarefa(request):
    return render(request, "tarefas/cadastrarTarefa.html")