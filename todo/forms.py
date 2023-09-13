from django.forms import ModelForm
from .models import Record
from django import forms


class RecordForm(ModelForm, forms.Form):
    deadline = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Record
        fields = ['title', 'description', 'important', 'deadline', 'status']
