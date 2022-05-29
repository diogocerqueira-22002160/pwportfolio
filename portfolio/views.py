from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

import datetime

from .forms import PostForm
from .models import Post
from .models import Cadeira
from .models import Projeto
from .models import PontuacaoQuizz

# Create your views here.


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def blog_page_view(request):
    context = {'posts': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def nova_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)


def edita_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/edita.html', context)


def apaga_page_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def pontuacao_quizz(request):
    score = 0
    if request.POST['questao1'] == 'b':
        score += 1

    if request.POST['questao2'] == 'b':
        score += 1

    if request.POST['questao3'] == 'a':
        score += 1

    return score


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')


def desenha_grafico_resultados(request):
    resultados = sorted(PontuacaoQuizz.objects.all(), key=lambda objeto: objeto.pontuacao, reverse=True)

    lista_nomes = []
    lista_pontuacao = []

    for pessoa in resultados:
        lista_nomes.append(pessoa.nome)
        lista_pontuacao.append(pessoa.pontuacao)

    plt.barh(lista_nomes, lista_pontuacao)
    plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches='tight')

