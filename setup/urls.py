"""
URL configuration for setup project (Estudo com Jogos — versão didática).

O `urlpatterns` é uma LISTA de rotas. Cada rota mapeia uma URL (caminho)
para uma função (view) localizada em `core/views.py`.

Exemplo:
    path('perfil/', views.perfil, name='perfil')
        ├── 'perfil/'  → o que o usuário digita depois do domínio
        ├── views.perfil → a função que atende essa URL
        └── name='perfil' → o "apelido" usado nos templates com {% url %}
"""

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # Painel de administração do Django (só para superusuários)
    path('admin/', admin.site.urls),

    # Login, logout e recuperação de senha (views nativas do Django)
    path('accounts/', include('django.contrib.auth.urls')),

    # 1) Página principal (index) — a view `home` sempre mostra o index.html
    path('', views.home, name='home'),

    # 2) Perfil do usuário
    path('perfil/', views.perfil, name='perfil'),

    # 3) Listagem dos alunos cadastrados (só alunos)
    path('alunos/', views.listar_alunos, name='listar_alunos'),

    # 4) Cadastro de um novo jogo (usado pelo professor)
    path('cadastrar-jogo/', views.cadastrar_jogo, name='cadastrar_jogo'),

    # 5) Página de jogo (onde o aluno joga)
    path('jogar/', views.jogar, name='jogar'),

    # 6) Acompanhamento da evolução do aluno
    path('evolucao/', views.acompanhar_evolucao, name='acompanhar_evolucao'),

    # Cadastro de novo usuário (auxiliar, usada pelo link do login)
    path('cadastro/', views.cadastro, name='cadastro'),
]
