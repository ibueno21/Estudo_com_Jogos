"""
views.py — Funções (views) do projeto "Estudo com Jogos" (versão didática)
=============================================================================

Em Django, uma *view* é uma função Python que recebe uma requisição HTTP
(parâmetro `request`) e devolve uma resposta (normalmente uma página HTML).

O caminho é sempre o mesmo:
  1. O usuário acessa uma URL (ex.: /perfil/).
  2. O Django usa o arquivo `setup/urls.py` para descobrir QUAL view atender.
  3. A view processa o pedido e chama `render(...)` para gerar a página.

Nesta versão didática, cada view é BEM simples: ela apenas devolve um
template HTML com o nome da página no centro da tela. Não há consulta ao
banco de dados (isso vem depois, quando aprendermos "models").

A função `render` recebe 3 argumentos:
  render(request, 'caminho/do/template.html', {contexto opcional})
"""

from django.shortcuts import render, redirect


# =============================================================================
# 1) PÁGINA PRINCIPAL (index) — a "porta de entrada" do site
# =============================================================================
def home(request):
    """
    Página principal (index) do site.

    A partir de agora a view `home` SEMPRE mostra a página de apresentação
    (index.html). É a porta de entrada do projeto: apresenta a plataforma
    "Estudo com Jogos" e traz o link para o login.
    """
    return render(request, 'core/index.html')


# =============================================================================
# 2) PERFIL DO USUÁRIO
# =============================================================================
def perfil(request):
    """
    Página do perfil do usuário logado.

    (Didático) Por enquanto só mostra o título da página. Depois vamos
    exibir nome, turma, pontos etc. usando o objeto `request.user`.
    """
    return render(request, 'core/perfil.html')


# =============================================================================
# 3) LISTAGEM DOS ALUNOS CADASTRADOS
# =============================================================================
def listar_alunos(request):
    """
    Página que vai listar APENAS os alunos cadastrados
    (professores e administradores ficam de fora).

    (Didático) Por enquanto só mostra o título. Depois faremos a consulta
    filtrando por tipo de usuário.
    """
    return render(request, 'core/listar_alunos.html')


# =============================================================================
# 4) CADASTRAR UM JOGO (usada pelo professor)
# =============================================================================
def cadastrar_jogo(request):
    """
    Página onde o professor cadastra um novo jogo (quiz).

    (Didático) Por enquanto só mostra o título. Depois vamos usar um
    formulário (forms.py) para o professor preencher os dados do jogo.
    """
    return render(request, 'core/cadastrar_jogo.html')


# =============================================================================
# 5) PÁGINA DE JOGO (onde o aluno joga/responder o quiz)
# =============================================================================
def jogar(request):
    """
    Página onde o aluno efetivamente JOGA e responde as questões do quiz.

    (Didático) Por enquanto só mostra o título. Depois vamos carregar as
    questões e alternativas do banco de dados e registrar as respostas.
    """
    return render(request, 'core/jogar.html')


# =============================================================================
# 6) ACOMPANHAMENTO DA EVOLUÇÃO DO ALUNO
# =============================================================================
def acompanhar_evolucao(request):
    """
    Página de acompanhamento da evolução do aluno nos jogos.

    (Didático) Por enquanto só mostra o título. Depois vamos mostrar
    gráficos/estatísticas de pontuação por jogo, usando os dados
    das partidas/respostas registradas no banco.
    """
    return render(request, 'core/acompanhar_evolucao.html')


# =============================================================================
# CADASTRO (página auxiliar, usada pelo link do login)
# =============================================================================
def cadastro(request):
    """
    Página de cadastro de um novo usuário.

    (Didático) Por enquanto só mostra o título. Depois vamos usar o
    UserCreationForm nativo do Django para criar uma conta.
    """
    return render(request, 'core/cadastro.html')



