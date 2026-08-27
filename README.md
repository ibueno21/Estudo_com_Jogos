# 📚 Estudo com Jogos

<!-- 
  README do projeto base para os alunos.
  Nota: o GitHub NÃO carrega fontes externas (Google Fonts, <style>, etc.),
  então o "tamanho da fonte" aqui é controlado pela hierarquia dos títulos
  (#, ##, ###) do próprio markdown.
-->

> Projeto educacional para ensinar **desenvolvimento web** aos alunos por meio da
> construção de uma plataforma de **jogos didáticos**.

Este repositório é a **base de estudos** entregue aos alunos. O objetivo não é
apenas "ter um site pronto", mas sim **aprender, na prática, as tecnologias** que
sustentam um projeto web moderno — do banco de dados ao HTML, passando pelo
servidor e pela lógica de negócio.

---

## 🎯 O objetivo pedagógico

A cada etapa do projeto, o aluno aprende um conceito novo de forma incremental:

1. **Rotas** (`urls.py`) — como o servidor decide qual página mostrar.
2. **Views** (`views.py`) — a ponte entre a requisição do usuário e a resposta.
3. **Templates** (`templates/`) — como o HTML é gerado dinamicamente.
4. **Arquivos estáticos** (`static/`) — CSS e JavaScript que dão visual e interação.
5. **Models** (`models.py`) — como os dados são organizados no banco.
6. **Formulários e autenticação** — login, cadastro e controle de acesso.

> 💡 **Filosofia:** cada arquivo tem comentários didáticos em português
> explicando *o quê*, *o porquê* e *como* funciona. O aluno não decora —
> ele **entende**.

---

## 🧰 Tecnologias utilizadas

### 🐍 [Python](https://www.python.org/)

Linguagem principal do projeto. O aluno aprende **lógica de programação**,
funções e orientação a objetos.

### 🌐 [Django](https://www.djangoproject.com/)

O framework web. Ensina a estrutura **MVT** (Model–View–Template), o **ORM**
para acessar o banco e a **autenticação** nativa.

### 🗄️ [MySQL](https://www.mysql.com/)

O banco de dados. Ensina **modelagem**, **normalização** e consultas **SQL**.

### 📄 [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML)

A estrutura das páginas. Ensina **marcação semântica**.

### 🎨 [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS)

O estilo e o layout. Ensina **Flexbox** e **responsividade**.

### ⚡ [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

A interatividade. Ensina **manipulação do DOM**.

### 🔀 [Git](https://git-scm.com/) + [GitHub](https://github.com/)

O versionamento do código. Ensina **branches**, **commits** e **colaboração**.

---

## 📁 Estrutura do projeto

```
Estudo_com_Jogos_BaseParaAlunos/
├── manage.py                  # CLI do Django (comandos de gestão)
├── requirements.txt           # Dependências do projeto
├── .env.example               # Modelo de configuração (sem segredos)
│
├── setup/                     # Configuração do projeto Django
│   ├── settings.py            # Configurações (banco, apps, idioma...)
│   ├── urls.py                # Rotas do site (quem atende cada URL)
│   ├── wsgi.py                # Servidor de produção (WSGI)
│   └── asgi.py                # Servidor assíncrono (ASGI)
│
└── core/                      # App principal da aplicação
    ├── models.py              # (em breve) modelagem do banco de dados
    ├── views.py               # Lógica que gera as páginas
    ├── admin.py               # Interface administrativa do Django
    ├── apps.py                # Configuração do app
    ├── migrations/            # Histórico de mudanças no banco
    ├── templates/             # HTML das páginas
    │   ├── core/              #   páginas da aplicação
    │   └── registration/      #   login/logout
    └── static/                # Arquivos de estilo e script
        ├── css/               #   estilos (base + por página)
        └── js/                #   scripts
```

---

## 🚀 Como rodar o projeto

### 1. Crie um ambiente virtual

Isolamos as dependências do projeto para não "sujar" o Python do sistema:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o banco de dados

O projeto foi configurado para usar um banco **MySQL** (compartilhado pela turma).
Copie o modelo de configuração e preencha os valores:

```bash
cp .env.example .env
```

> ⚠️ **Importante:** o arquivo `.env` contém dados sensíveis (senha, chave
> secreta) e **não deve ser versionado**. Ele já está no `.gitignore`.

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/** no navegador. 🎉

---

## 🔗 Rotas disponíveis

### 🏠 `/` — Página principal

A **index**: template com visual elaborado, a porta de entrada do site.

### 🔐 `/accounts/login/` — Login

**Autenticação nativa** do Django, pronta para uso.

### 📝 `/cadastro/` — Cadastro

Página de **registro** de novos usuários.

### 👤 `/perfil/` — Perfil do usuário

Demonstra **view + template** simples.

### 🧑‍🎓 `/alunos/` — Listagem de alunos

Prepara a **listagem de dados** vinda do banco.

### ➕ `/cadastrar-jogo/` — Cadastrar jogo

Prepara o uso de **formulários**.

### 🎮 `/jogar/` — Página de jogo

Prepara o fluxo do **quiz**.

### 📈 `/evolucao/` — Acompanhamento

Prepara as **estatísticas** de desempenho.

---

## 🎨 Arquivos estáticos (CSS e JS)

Cada página didática usa **dois** arquivos CSS, na ordem:

1. **`css_basico.css`** — estilo de centralização compartilhado por todas.
2. **CSS individual** (ex.: `perfil.css`) — lugar para o aluno **personalizar**
   aquela página específica, sobrescrevendo o estilo base.

```
core/static/
├── css/
│   ├── css_basico.css            # centralização (compartilhado)
│   ├── perfil.css                # personalização do perfil
│   ├── listar_alunos.css         # personalização da listagem
│   ├── cadastrar_jogo.css        # personalização do cadastro
│   ├── jogar.css                 # personalização do jogo
│   ├── acompanhar_evolucao.css   # personalização da evolução
│   ├── cadastro.css              # personalização do cadastro
│   ├── index_apresentacao.css    # visual da página inicial
│   └── login.css                 # visual do login
└── js/
    ├── index_apresentacao.js     # interação da página inicial
    └── login.js                  # interação do login
```

> 💡 Isso ensina dois conceitos importantes de front-end: **reuso de código**
> (CSS compartilhado) e **ordem de carregamento** (o segundo CSS pode
> sobrescrever o primeiro).

---

## 🧭 O que vem por aí (próximas etapas)

- [ ] **Models normalizados** — `Aluno`, `Professor`, `Quiz`, `Questao`,
      `Alternativa`, etc., seguindo a modelagem aprovada.
- [ ] **Herança de templates** — `{% extends %}` e `{% block %}` para não
      repetir cabeçalho/rodapé.
- [ ] **Formulários** — `forms.py` com `ModelForm` e `UserCreationForm`.
- [ ] **Fluxo completo do quiz** — jogar, registrar respostas, calcular pontos.
- [ ] **Gráficos de evolução** — estatísticas de desempenho por aluno.

---

## 👨‍🏫 Sobre

Projeto desenvolvido pelo professor **Isaac** para as aulas de tecnologia,
focado no **aprendizado prático** das tecnologias web. O código é intencionalmente
**didático** — claro, comentado em português e estruturado em etapas.

> *"Ensinar não é transferir conhecimento, mas criar as possibilidades para a
> sua própria produção."* — Paulo Freire
