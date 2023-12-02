from django import forms
from .models import Tarefas

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['titulo', 'descricao', 'termino']
        
