from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        fields = ['titulo', 'descripcion', 'estado']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }