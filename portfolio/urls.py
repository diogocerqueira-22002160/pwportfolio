from . import views
from django.urls import path

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('web/', views.web_page_view, name='web'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('weather', views.weather_page_view, name='weather'),
    path('novo_post', views.novo_post_page_view, name='novo_post'),
    path('edita_post/<int:post_id>', views.edita_post_page_view, name='edita_post'),
    path('apaga_post/<int:post_id>', views.apaga_post_page_view, name='apaga_post'),
    path('nova_cadeira', views.nova_cadeira_page_view, name='nova_cadeira'),
    path('edita_cadeira/<int:cadeira_id>', views.edita_cadeira_page_view, name='edita_cadeira'),
    path('apaga_cadeira/<int:cadeira_id>', views.apaga_cadeira_page_view, name='apaga_cadeira'),
    path('novo_projeto', views.novo_projeto_page_view, name='novo_projeto'),

    path('edita_projeto/<int:projeto_id>', views.edita_projeto_page_view, name='edita_projeto'),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_page_view, name='apaga_projeto'),
    path('novo_professor', views.novo_professor_page_view, name='novo_professor'),
]