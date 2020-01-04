from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={'class' : 'form-control','placeholder' : 'Enter todo here','aria-label' : 'Todo','aria-describedby' : 'add-btn'}))
    desc = forms.CharField(max_length=300,widget=forms.Textarea)

class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text','desc','due']
        widgets = {
            'due' : forms.widgets.DateTimeInput(attrs={'class':'form-control','type': 'datetime', 'placeholder':'Due Time (YYYY-MM-DD HH:MM:SS) [optional]'}),
            'desc' : forms.TextInput(attrs={'class':'form-control','placeholder':'Description [optional]'}),
            'text' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Task title'}),
        }
