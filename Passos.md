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