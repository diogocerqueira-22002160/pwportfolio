from django.contrib import admin

from .models import Post
from .models import Professor
from .models import Cadeira
from .models import Projeto
from .models import PontuacaoQuizz

# Register your models here.

admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(PontuacaoQuizz)