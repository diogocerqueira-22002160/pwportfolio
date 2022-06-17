from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .forms import CadeiraForm
from .forms import ProjetoForm
from .forms import ProfessorForm
from .models import Post
from .models import Cadeira
from .models import Projeto
from .models import Professor
from .models import PontuacaoQuizz

from matplotlib import pyplot as plt
import io
import urllib
import base64
import matplotlib

matplotlib.use('Agg')
# Create your views here.


def home_page_view(request):
        return render(request, 'portfolio/home.html')


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def blog_page_view(request):
    context = {'posts': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def pontuacao_quizz(request):
    score = 0
    if request.POST['questao1'] == 'b':
        score += 1

    if request.POST['questao2'] == 'b':
        score += 1

    if request.POST['questao3'] == 'a':
        score += 1

    return score


def web_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    context = {
        'data': desenha_grafico_resultados()
    }

    return render(request, 'portfolio/web.html', context)


def desenha_grafico_resultados():
        pontuacoes = PontuacaoQuizz.objects.all().order_by('pontuacao')

        nomesList = [pontuacao.nome for pontuacao in pontuacoes]
        pontuacaoList = [pontuacao.pontuacao for pontuacao in pontuacoes]

        plt.barh(nomesList, pontuacaoList)
        plt.ylabel("Pontuacao")
        plt.autoscale()

        fig = plt.gcf()
        plt.close()

        buf = io.BytesIO()
        fig.savefig(buf, format='png')

        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)

        return uri


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })


def weather_page_view(request):
    return render(request, 'portfolio/weather.html')


def novo_post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/novo_post.html', context)


def edita_post_page_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}

    return render(request, 'portfolio/edita_post.html', context)


def apaga_post_page_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


@login_required
def nova_cadeira_page_view(request):
    form = CadeiraForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form}

    return render(request, 'portfolio/nova_cadeira.html', context)


@login_required
def edita_cadeira_page_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(pk=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}

    return render(request, 'portfolio/edita_cadeira.html', context)


@login_required
def apaga_cadeira_page_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))


@login_required
def novo_projeto_page_view(request):
    form = ProjetoForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}

    return render(request, 'portfolio/novo_projeto.html', context)


@login_required
def edita_projeto_page_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}

    return render(request, 'portfolio/edita_projeto.html', context)


@login_required
def apaga_projeto_page_view(request, projeto_id):
    Projeto.objects.get(id=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

@login_required
def novo_professor_page_view(request):
    form = ProfessorForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}

    return render(request, 'portfolio/novo_professor.html', context)

