from django import forms
from django.forms import ModelForm
from .models import Post
from .models import Cadeira
from .models import Projeto
from .models import Professor


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'inputText'}),
            'titulo': forms.TextInput(attrs={'class': 'inputText'}),
            'descricao': forms.Textarea(attrs={'class': 'inputText'}),
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'inputText'}),
            'ects': forms.RadioSelect(choices=[(5, 5), (6, 6), (20, 20)], attrs={'class': 'inputRadio'}),
            'ano': forms.RadioSelect(choices=[(1, "1º"), (2, "2º"), (3, "3º")], attrs={'class': 'inputRadio'}),
            'semestre': forms.RadioSelect(choices=[(1, "1º"), (2, "2º")], attrs={'class': 'inputRadio'}),
            'topicos': forms.Textarea(attrs={'class': 'inputText'}),
            'ranking': forms.RadioSelect(choices=[(1, "⭐"), (2, "⭐⭐"), (3, "⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (5, "⭐⭐⭐⭐⭐")], attrs={'class': 'inputRadio'}),
        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'inputText'}),
            'descricao': forms.Textarea(attrs={'class': 'inputText'}),
        }


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'inputText'}),
        }