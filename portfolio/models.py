from django.db import models

# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'


class Professor(models.Model):
    nome = models.CharField(max_length= 64)
    imagem = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Cadeira(models.Model):
    nome = models.CharField(max_length=64)
    ects = models.IntegerField(default=1)
    ano = models.IntegerField(default=2020)
    semestre = models.IntegerField(default=1)
    topicos = models.CharField(max_length=255)
    ranking = models.IntegerField(default=1)
    imagem = models.ImageField(upload_to='pictures/', blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name="Cadeiras")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='pictures/', null=True, blank=True)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.PROTECT, related_name="Projetos")

    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nome} : {self.pontuacao} pontos'


