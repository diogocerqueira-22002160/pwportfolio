from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-autor'}),
            'titulo': forms.TextInput(attrs={'class': 'form-titulo'}),
            'descricao': forms.TextInput(attrs={'class': 'form-descricao'}),
        }