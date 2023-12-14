from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        email = request.POST.get('user-email')
        name = request.POST.get('user-fullname')
        username = request.POST.get('user-username')
        senha = request.POST.get('user-pwd')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('Já existe')

        user = User.objects.create_user(username=username, email=email, first_name=name, password=senha)
        user.save()
        return HttpResponse('Cadastrado com sucesso')
            

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user-username')
        senha = request.POST.get('user-pwd') 

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Sucesso')
        else:
            return HttpResponse('Falha')