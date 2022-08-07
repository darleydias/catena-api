# INSTALANDO O AMBIENTE NUMA MÁQUINA UBUNTU 22.04

## SISTEMA OPERACIONAL INSTALADO COM CHROME, VSCODE, MYQLWORKBANCH, POSTMAN

## PIPELINE

ORDEM | AÇÃO
-------------
01    | Instalando SO
02    | Criando e ativando o ambiente virtual
03    | Instalando o Django e conferindo
04    | Instalando o Maria-DB e workbanch no Ubuntu
05    | Instalando conector mysql
06    | Ciando as tabelas no banco
07    | Instalando chrome
08    | Criando as Serializer 
09    | USANDO ADMIN
10    | Instalando o POSTMAN
11    | Instlando o VSCODE
12    | Subindo o projeto
13    | Salvando no github



1. INSTALANDO SO

### Conta de root ubunto yhvh()77

### criar conta catena senha Catelecom()123



2. Criando e ativando o ambiente virtual

sudo apt install libpq-dev python3-dev

sudo apt-get install python3-venv

sudo python3 -m venv ./venv

source venv/bin/activate

3. Instalando o Django e conferindo

sudo pip install django

pip freeze

4. Instalando o Maria-DB e workbanch no Ubuntu

sudo apt install mariadb-server

sudo mysql_secure_installation

systemctl start mysql

entre mysql -u root 

trocar senha do root para `Yhvh()77`

criar usuario catena senha 'Catelecom()123'

sudo snap install mysql-workbench-community

sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service


5. Instalando conector mysql

sudo apt-get update -y

sudo apt-get install -y libmariadb-dev

pip3 install mariadb

apt-get install libmariadbclient-dev

apt-get install libmysqlclient-dev

pip install mysqlclient

6. Ciando as tabelas no banco

sudo python3 manage.py makemigrations

sudo python3 manage.py migrate

Mas não criava as migratios

na pasta migration apague as migrations. 

entre em `__pycache__` dentro de migratios e mate os arquivos de cache

Rode novamente

sudo python3 manage.py makemigrations

sudo python3 manage.py migrate

7. Instalando chrome 

sudo apt update && sudo apt upgrade -y

sudo apt install software-properties-common apt-transport-https wget ca-certificates gnupg2 ubuntu-keyring -y

sudo wget -O- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /usr/share/keyrings/google-chrome.gpg

echo deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main | sudo tee /etc/apt/sources.list.d/google-chrome.list

sudo apt update

apt list --upgradable

sudo apt install google-chrome-stable -y

8. Criando as Serializer 

> controla os verbos HTTP e suas rotas, criando os jsons

> django rest framework - Documentação:  [https://www.django-rest-framework.org/]

~~~ bash
pip install djangorestframework

pip install markdown  

pip install django-filter 
~~~

9. USANDO ADMIN

python manage.py createsuperuser

10. Instalando postman

Usei o `Ubuntu software` na barra lateral do Ubuntu

> Cuidado: nas urls do postman tem que ter / no final 
> deveria ser: localhost:8000/tiposProcesso/

Tentei fazer metodo put ou path sem definir um id na barra de endereço:
> localhost:8000/tiposOperacao/
Deu erro de não reconhecer o PUT
> Mudei para localhost:8000/tiposOperacao/2
Deu erro no django
> mudei para localhost:8000/tiposOperacao/2/
! resolveu

11. VSCODE

Usei o `Ubuntu software` na barra lateral do Ubuntu

Para conseguir salvar os arquivos no vscode, entre na pasta da aplicação `catena-api` e digite:

sudo chown -R $USER:$USER .


## Extesões usadas:

Portuguese (Brasil)

pylance

Intellicense (pylance)

12. Subindo o projeto

### sudo python manage.py runserver

#### deu o erro:

> sudo: The "no new privileges" flag is set, which prevents sudo from running as root.

> sudo: If sudo is running in a container, you may need to adjust the container configuration to disable the flag.

### python manage.py runserver

#### deu o erro:

> Comando 'python' não encontrado, você quis dizer:
> comando 'python3' do deb python3
> comando 'python' do deb python-is-python3

### Rodei entao com 

python3 manage.py runserver

> ai subiu

13. Salvando projeto no gitHUB 

### configurando usuario (se necessãrio)

sudo git config user.name "darleydias"

### Configurando e-mail (se necessãrio)

sudo git config user.email "darlley@gmail.com"

### setando ambiente remoto

sudo git remote add origin https://github.com/darleydias/catena-api.git

### setando branch 

sudo git branch -M main

### enviando 

sudo git add .

sudo git commit -m "vx.x"

git push --set-upstream origin main


