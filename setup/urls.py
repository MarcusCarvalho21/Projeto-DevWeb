"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tarefas.views import home, verTarefa, editTarefa, delTarefa, mudaStatus, perfilUser, index
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', home, name='home'),
    path('tarefa/<str:encoded_id>/', verTarefa, name='verTarefa'),
    path('tarefas/edit/<int:id>', editTarefa, name='editTarefa'),
    path('tarefas/mudastatus/<int:id>', mudaStatus, name='mudaStatus'),
    path('tarefas/deleta/<int:id>', delTarefa, name='delTarefa'),
    path('perfil/', perfilUser, name='perfilUser'),
    path('perfil/mudastatus/<int:id>', mudaStatus, name='mudaStatusPerfil'),
    path('perfil/deleta/<int:id>', delTarefa, name='delTarefaPerfil'),
    path('auth/', include('usuarios.urls')),
    path('', index, name='index')
]
