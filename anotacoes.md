# Iniciando o projeto

## Extesões usadas:

Protuguese (Brasil)

pylance

Intellicense (pylance)
 
## Criando e ativando o ambiente virtual

sudo apt install libpq-dev python3-dev

sudo apt-get install python3-venv

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

### A view que antes renderizava um HTML, agora renderiza um JSON e remete para qum chamou a API   
~~~ python
from django.http import JsonResponse

import datetime


def tiposProcesso(request):

    current_datetime = datetime.datetime.now()  

    if request.method=="GET":

        tipoProcesso={'tpPro_id':1,'tpPro_descri':'IPM',
        
        'tpPro_dh':current_datetime}
        
        return JsonResponse(tipoProcesso)

## pra usar isso no navegador tenho que criar uma rota no arquivo urls dentro do setup

from django.contrib import admin

from django.urls import path

from appCatena.views import tiposProcesso

urlpatterns = [

    path("admin/", admin.site.urls),

    path("tiposProcesso/", tiposProcesso)
]
~~~
## rodei:

pip install mysqlclient

## no Ubuntu deu pau, ai fiz:

sudo apt-get update -y

sudo apt-get install -y libmariadb-dev

pip3 install mariadb

apt-get install libmariadbclient-dev

apt-get install libmysqlclient-dev

## ------------------------

pip install mysqlclient

sudo python manage.py makemigrations

sudo python manage.py migrate


## A conta do banco é user Yhvh()77

## de root ubunto          yhvh()77

## Mas não criava as migratios

## Estava faltando configurar o app dentro do arquivo setings
~~~ python
INSTALLED_APPS = [

    "appCatena",

    "django.contrib.admin",
~~~
## Instalando o workbanch no Ubuntu

sudo snap install mysql-workbench-community
sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service


## Para cadastrar so verbos HTTP e suas rotas tem uma ferramenta
### django rest framework - Documentação: https://www.django-rest-framework.org/ 

pip install djangorestframework

pip install markdown       # Markdown support for the browsable API.

pip install django-filter  # Filtering support

### Necessário registrar o App no settings.py, seçao INSTALED_APPS
~~~ python
INSTALLED_APPS = [

    ...,

    "rest_framework"

]
~~~
### No models.py registro todas entidades
#### Crio a classe dentro o método __str__ para referenciar o model
#### em entidades ue tenho relaóes de um pra ele com poucos "N`s" faco:
 ~~~ python  
 SEXO = (
        ('M','Masculino'),

        ('F','Feminino')

    )
sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
~~~
## Vamos agora gravar no banco

python manage.py makemigrations

python manage.py migrate

## o meu python makemigrations estava sempre dizendo que não havia mudanças
### tinha esquecido do atributo das novas classes criadas no arquivo model:

class promotor(models.Model):
### estava:
class promotor(): 

## Configurando o admim para cadastrar essas entidades
### Basta configurar o arquivo admin.py no app
~~~ python
class TpProcesso(admin.ModelAdmin):

    #campos que serão mostrado

    list_display =('id','descri')

    #campos que serao usado para selecionar para altererar 

    list_display_list =('id','descri')

    #campo de filtro de pesquisa

    search_field =('descri')

    #paginação

    list_page = 20

    #registrando a interface no admin (entidade,nome da classe admin)
~~~
admin.site.register(TipoProcesso,TpProcesso)

## Apanhei pois dava a informação:
admin.site.register(TipoProcesso,TpProcesso)

NameError: name 'TpProcesso' is not defined
## Era que a última linha tinha uma indentação
    list_page = 20

    admin.site.register(TipoProcesso,TpProcesso)
## Qundo deveria ser
    list_page = 20

admin.site.register(TipoProcesso,TpProcesso)
## Estava dando um pau qund tentava gerara migratiosn
Was the model appCatena.tiposProcesso renamed to TipoProcesso? [y/N] y

It is impossible to add a non-nullable field 'descri' to procedimento 

without specifying a default. This is because the database needs 

something to populate existing rows.

Please select a fix:

 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)

 2) Quit and manually define a default value in models.py.
Select an option: 1

Please enter the default value as valid Python.

The datetime and django.utils.timezone modules are available, so it is

 possible to provide e.g. timezone.now as a value.

Type 'exit' to exit this prompt

## Ai quando ele "pediu Please enter the default value as valid Python", digitei

datetime.date()

## Passou a dar outro pau

TypeError: function missing required argument 'year' (pos 1)

## gerei as migratios de novo ai passou a dar:

django.db.migrations.exceptions.NodeNotFoundError: Migration appCatena.

0002_procedimento_promotor_tipooperacao dependencies reference 

nonexistent parent node ('appCatena', '0001_initial')

## fui na pasta migratioon e apaguei as migrations. Ai passou a daroutro pau

## Entao entrei em __pycache__ dentro de migratios e matei os arquivos de cache

## testando admim http://localhost:8000/admin

python manage.py createsuperuser

## Problemas com migratios

1) apaguei todas as tabelas do banco

2) apaguei arquivos dentro de migratios e __pycache__

3) rodei de novo migrations e migrate

## serializer faz o mapeamento pytthon json

## Erro - estava dando direto o erro

  File "/home/darley/catena/catena-api/setup/urls.py", line 3, in <module>
    from appCatena.views import TiposOperacaoViewSet,TiposProcessoViewSet
  File "/home/darley/catena/catena-api/appCatena/views.py", line 3, in <module>
    from serializer import TipoOperacaoSerializer, TipoProcessoSerializer
ModuleNotFoundError: No module named 'serializer'

## na importação do arquivo de view estva faltando referencia oa pacote

~~~ python
from rest_framework import viewsets
from appCatena.models import TipoOperacao,TipoProcesso
from serializer import TipoOperacaoSerializer, TipoProcessoSerializer
~~~
## quando o certo seria

~~~ python
from rest_framework import viewsets
from appCatena.models import TipoOperacao,TipoProcesso
from appCatena.serializer import TipoOperacaoSerializer, TipoProcessoSerializer
~~~

## erro postrman 

### quando eu estava tentando gravar o tiposProcesso no postman dava errado:

#### estava gravando: localhost:8000/tiposProcesso
#### deveria ser: localhost:8000/tiposProcesso/


