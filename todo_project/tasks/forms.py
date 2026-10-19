from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder': 'Add description...'}))

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'bootstrap-select'}),
            'priority': forms.Select(attrs={'class': 'bootstrap-select'}),
            'price': forms.NumberInput(attrs={'min': '0.0'}),
        }

class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = '__all__'        