# Passos de instalação e uso do Django

## Criando a venv (ambiente virtual)
$ python -m venv venv

OSB: O último venv é o nome do ambiente

## Entrar no ambiente

## Instalar o Django no ambiente
$ pip install django

## Criar um Projeto no django (nele terá o manage.py)
$ django-admin startproject nomeapp

## Testar se foi instalado
$ python manage.py runserver

## Criar App no Django (funcionalidade dentro do projeto)
$ django-admin startapp nomeapp
Obs: usar no singular o nome

## Criar superuser

Rodar a modificação no BD
$ python manage.py migrate

OBS: os comandos tem na documentação
makemigrations: pega toda criação no BD
migration: modifica o BD

# Conectar o App no Projeto
Na pasta de Projeto, entrar no arquivo settings.py em INSTALLED_APPS = [], adicionar o app.
ex:
app 'filme' adiciona 'filme' dentro de INSTALLED_APPS = ['filmes',]
Ir para arquivo urls.py do Projeto e adicionar

# Aparecer o app dentro do admin
Em admin.py importar o arquivo do models aqui. ex: from ./models import Filme
add uma linha admin.site.register(Filme)

Para ajustar o titulo do filme, criar a def __str__(self) retorna self.titulo dentro do Models Filme. Executar o makemigrations e migrate.

# Criar pasta para arquivos estáticos(image, css, js)

Adicionar em settings.py do projeto e adicionar esta constante abaixo no local de statics

STATICFILES_DIRS = [
    BASE_DIR / "static",    
]

criar uma pasta 'static' com as subpastas css, js, imagem

# Criando as Views e Templates
Configurar em urls do projeto, neste caso a pasta hashflix e add em urlpatterns o seguinte código:
path('', include('filme.urls')),

Neste exemmplo está chamando o app filme apontando para o arquivo url desta pasta que deverá ser criado.

criar a pasta template no app filme (pasta filme). Podemos criar uma pasta template fora do app e projeto paraser um template global.

Na View, criaremos o caminho que a lógica que será exibida no template.
Deve chamar a View da seguinte forma:

Entrar na urls.py de filme e adicionar o seguinte código:
#from filme.views import homepage
from .views import homepage

urlpatterns = [
    path('', homepage),
]

Na View, tem que criar a função def homepage(request) e tem que receber como parametro o request e retorna a função render com o template(página html):

from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')

OBS: o template global é configurado no settings.py em template= [ "Dir":['templates']]

# Template dinâmico

usar o {% block conteudo %} e fecha com {% endblock %}. Use isso para inserir em outros templates e receber os valores dentro do bloco.
No template que irão receber o template global tem user o {% extends base.html %}. base.html é o template global. 

Para incluir um elemento html podemos utilizar {% include 'navbar.html' %}. Nesse exemplo inclui o arquivo/elemento navbar no arquivo global. Não fecha igual ao bloco.

Para colocar uma imagem do seu arquivo static deve incluir o {% load static %} e a tag img logo abaixo. incluir isso no navbar. No src incluir 
src="{% static 'my_app/example.jpg' %}"
