import base64
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Tarefas
from .forms import TarefaForm
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'tarefas/index.html')

@login_required(login_url='/auth/login/')
def home(request):

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.done = 'doing'
            tarefa.user = request.user
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
    
    search = request.GET.get('search')
    if search:
        tarefas_lista = Tarefas.objects.filter(titulo__icontains=search, done='doing', user=request.user)
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    else:
        tarefas_lista = Tarefas.objects.filter(done='doing').order_by('termino').filter(user=request.user)
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    return render(request, "tarefas/home.html", {"tarefas": tarefas})

@login_required(login_url='/auth/login/')
def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefaForm(instance=tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            messages.success(request, 'Tarefa editada com sucesso!')
            return redirect('/tarefas/')
        else:
            return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})
    else:
        return render(request, 'tarefas/editaTarefa.html', {'form': form, 'tarefa': tarefa})
    
@login_required(login_url='/auth/login/')
def delTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()

    messages.success(request, 'Tarefa excluida com sucesso!')

    return redirect('/tarefas/')
    
@login_required(login_url='/auth/login/')
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
    if caminho_url.startswith('/dashboard/mudastatus/'):
        messages.success(request, 'Tarefa restaurada com sucesso!')
        return redirect('/dashboard/')
    else:
        messages.success(request, 'Tarefa concluida com sucesso!')
        return redirect('/tarefas/')
    
@login_required(login_url='/auth/login/')
def perfilUser(request):
    '''Código para informar os dados para o dashboardboard'''
    tarefasRecentes = Tarefas.objects.filter(done='done', user=request.user, atualizado_em__gt=datetime.now()-timedelta(days=30)).count()
    tarefasFeitas = Tarefas.objects.filter(done='done', user=request.user).count()
    tarefasPendentes = Tarefas.objects.filter(done='doing', user=request.user).count()

    '''Código para listar tarefas do histórico'''
    search = request.GET.get('search')
    if search:
        tarefas_lista = Tarefas.objects.filter(titulo__icontains=search, done='done', user=request.user)
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    else:
        tarefas_lista = Tarefas.objects.filter(done='done').order_by('termino').filter(user=request.user)
        paginator = Paginator(tarefas_lista, 5)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)
    return render(request, "tarefas/perfilUser.html", {"tarefas": tarefas, 'tarefasRecentes': tarefasRecentes, 'tarefasFeitas': tarefasFeitas, 'tarefasPendentes': tarefasPendentes})
    
@login_required(login_url='/auth/login/')
def verTarefa(request, encoded_id):
    decoded_id = base64.b64decode(encoded_id).decode('utf-8')
    tarefa = get_object_or_404(Tarefas, pk=decoded_id)
    return render(request, 'tarefas/tarefa.html', {"tarefa": tarefa})
    
@login_required(login_url='/auth/login/')
def cadastroTarefa(request):
    return render(request, "tarefas/cadastrarTarefa.html")

def logout(request):
    """
    Removes the authenticated user's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()