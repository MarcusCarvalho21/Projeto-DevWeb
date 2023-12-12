import base64
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Tarefas
from .forms import TarefaForm
from django.contrib import messages
from datetime import datetime, timedelta

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
        tarefas_lista = Tarefas.objects.filter(titulo__icontains=search, done='doing')
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    else:
        tarefas_lista = Tarefas.objects.filter(done='doing').order_by('termino')
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

def mudaStatus(request, id):
    caminho_url = request.path
    tarefa = get_object_or_404(Tarefas, pk=id)
    if(tarefa.done == 'doing'):
        tarefa.done = 'done'
    else:
        tarefa.done = 'doing'
    tarefa.finalizado_em = datetime.now().date()
    tarefa.save()
    print(f'{caminho_url}')
    if caminho_url.startswith('/perfil/mudastatus/'):
        messages.info(request, 'Tarefa restaurada com sucesso!')
        return redirect('/perfil/')
    else:
        messages.info(request, 'Tarefa concluida com sucesso!')
        return redirect('/tarefas/')

def perfilUser(request):
    '''Código para informar os dados para o dashboard'''
    tarefasRecentes = Tarefas.objects.filter(done='done', atualizado_em__gt=datetime.now()-timedelta(days=30)).count()
    tarefasFeitas = Tarefas.objects.filter(done='done').count()
    tarefasPendentes = Tarefas.objects.filter(done='doing').count()

    '''Código para listar tarefas do histórico'''
    search = request.GET.get('search')
    if search:
        tarefas_lista = Tarefas.objects.filter(titulo__icontains=search, done='done')
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    else:
        tarefas_lista = Tarefas.objects.filter(done='done').order_by('termino')
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    return render(request, "tarefas/perfilUser.html", {"tarefas": tarefas, 'tarefasRecentes': tarefasRecentes, 'tarefasFeitas': tarefasFeitas, 'tarefasPendentes': tarefasPendentes})

def verTarefa(request, encoded_id):
    decoded_id = base64.b64decode(encoded_id).decode('utf-8')
    tarefa = get_object_or_404(Tarefas, pk=decoded_id)
    return render(request, 'tarefas/tarefa.html', {"tarefa": tarefa})

def cadastroTarefa(request):
    return render(request, "tarefas/cadastrarTarefa.html")