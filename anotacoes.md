# Iniciando o projeto
## Criando e ativando o ambiente virtual
sudo python3 -m venv ./venv
source venv/bin/activate
## Instalando o Django e conferindo
sudo pip install django
pip freeze
## Criando o Projeto
sudo django-admin startproject setup .
## Criando o app
sudo django-admin startapp appCatena
## Subindo projeto
sudo python manage.py runserver
## preciso mudar a lógica de retornar html para REST json
### Dentro do arquivo view do app troco o render por JsonResponse

from appCatena.views import tiposProcesso
from django.http import JsonResponse

### Pra definir o que será entregue pela API, no view do app fica:

from django.http import JsonResponse
import datetime

def tiposProcesso(request):
     current_datetime = datetime.datetime.now()  
    if request.method=="GET":
        tipoProcesso={'tpPro_id':1,'tpPro_descri':'IPM','tpPro_dh':current_datetime}
        return JsonResponse(tipoProcesso)
## pra usar isso no navegador tenho que criar uma rota no arquivo urls dentro do setup
from appCatena.views import tiposProcesso
urlpatterns = [
    path("admin/", admin.site.urls),
    path("tiposProcesso/", tiposProcesso),

## rodei:
pip install mysqlclient
sudo python manage.py makemigrations
sudo python manage.py migrate

## Mas não criava as migratios

## Estava faltando configurar o app dentro do arquivo setings

INSTALLED_APPS = [
    "appCatena",
    "django.contrib.admin",






