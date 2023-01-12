from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        #estilisar el formulario del fronted con las clases que necesites
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'descritpion' : forms.Textarea(attrs={'class' : 'form-control'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }