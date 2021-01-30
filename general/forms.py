from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, IntegerField
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'state', 'time_out']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'type': "text",
                'placeholder': "Введите название"}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"}),
            'time_out': DateInput(attrs={
                'type': "date"}),
            'state': Select(choices=(
                ('Новая', 'Новая'),
                ('Запланированная', 'Запланированная'),
                ('в Работе', 'в Работе'),
                ('Завершённая', 'Завершённая'))),
        }
