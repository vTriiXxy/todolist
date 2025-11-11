from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        fields = ['titulo', 'descripcion', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }