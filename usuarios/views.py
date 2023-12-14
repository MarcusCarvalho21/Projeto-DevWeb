from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, user_logged_out
from django.contrib.auth import login as login_django
def cadastro(request):
    error = 0
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        email = request.POST.get('user-email')
        name = request.POST.get('user-fullname')
        username = request.POST.get('user-username')
        senha = request.POST.get('user-pwd')
        confirmasenha = request.POST.get('confirm-pwd')

        user = User.objects.filter(username = username).first()
        verificaremail = User.objects.filter(email = email).first()

        if user:
            messages.error(request, 'Nome de usuario já em uso')
            error += 1
        if verificaremail:
            messages.error(request, 'Email já em uso')
            error += 1

        if senha != confirmasenha:
            messages.error(request, 'As senhas não combinam')
            error += 1

        
        if error > 0:
            return redirect('/auth/cadastro/#')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=name, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            
        return redirect('/auth/cadastro/')
            

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user-username')
        senha = request.POST.get('user-pwd') 

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('/tarefas/')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
            return redirect('/auth/login/')
        
def logout(request):
    user = getattr(request, 'user', None)
    if user.is_authenticated:
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()

    messages.info(request, 'Você encerrou sua sessão')
    return redirect('/auth/login')
