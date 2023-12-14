from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, user_logged_out
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
        return redirect('/auth/login/')
            

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
            return HttpResponse('Falha')
        
def logout(request):
    """
    Removes the authenticated user's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if user.is_authenticated:
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    
    return redirect('/auth/login')
