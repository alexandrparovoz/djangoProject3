from .models import Task
from django.forms import ModelForm, TextInput, Textarea, TimeInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'text']
        widgets = {
            'task_name':TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Введите название'
        }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }