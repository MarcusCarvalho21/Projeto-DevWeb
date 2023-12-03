import base64
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefas
from .forms import TarefaForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.done = 'doing'
            tarefa.save()
    tarefas = Tarefas.objects.all().order_by('termino')
    return render(request, "tarefas/home.html", {"tarefas": tarefas})

def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefaForm(instance=tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})
    else:
        return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})

def verTarefa(request, encoded_id):
    decoded_id = base64.b64decode(encoded_id).decode('utf-8')
    tarefa = get_object_or_404(Tarefas, pk=decoded_id)
    return render(request, 'tarefas/tarefa.html', {"tarefa": tarefa})

def cadastroTarefa(request):
    return render(request, "tarefas/cadastrarTarefa.html")