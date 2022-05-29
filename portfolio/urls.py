from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('',views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('nova', views.nova_page_view, name='nova'),
    path('edita/<int:post_id>', views.edita_page_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_page_view, name='apaga'),
    path('quizz', views.quizz_page_view, name='quizz'),
]