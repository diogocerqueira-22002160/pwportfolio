from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


from .forms import PostForm
from .models import Post
from .models import Cadeira
from .models import Projeto
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

    context = {
        'data': desenha_grafico_resultados()
    }

    return render(request, 'portfolio/quizz.html', context)


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
