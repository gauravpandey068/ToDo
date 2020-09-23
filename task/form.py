from django import forms
from .models import Todo


class FormTodo(forms.ModelForm):
    task = forms.CharField(required=True)

    class Meta:
        model = Todo
        fields = ['task']
