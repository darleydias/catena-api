from token import OP
from django.contrib import admin
from appCatena.models import Operacao,TipoProcedimento, TipoOperacao, Promotor, Procedimento,Comarca,PartRecon,Ponto,Alvo,ServidorMembro

class TiposProcedimento(admin.ModelAdmin):
    #campos que serão mostrado  
    list_display =('id','descri')
    #campos que serao usado para selecionar para altererar 
    list_display_list =('id','descri')
    #campo de filtro de pesquisa
    search_field =('descri')
    #paginação
    list_page = 20
    #registrando a interface no admin (entidade,nome da classe admin)
admin.site.register(TipoProcedimento,TiposProcedimento)

class TiposOperacao(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(TipoOperacao,TiposOperacao)

class Procedimentos(admin.ModelAdmin):
    list_display =('id','tipo','nrPro','descri','tipo')
    list_display_list =('id','descri')
    search_field =('nrPro','descri','tipo')
    list_page = 20
admin.site.register(Procedimento,Procedimentos)

class Promotores(admin.ModelAdmin):
    list_display =('id','nome','mamp','idComarca','sexo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(Promotor,Promotores)

class Comarcas(admin.ModelAdmin):
    list_display =('id','nome','sigla','tipo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(Comarca,Comarcas)

class Alvos(admin.ModelAdmin):
    list_display =('nome','alcunha','cpf','rg','ufRg','sexo','dtNasc')
    list_display_list =('id','nome')
    search_field =('nome','alcunha')
    list_page = 20
admin.site.register(Alvo,Alvos)

class Pontos(admin.ModelAdmin):
    list_display =('nrPonto','idOperacao','descri','orientacaoRecon','endereco','complemento','resp','idAlvo','dtPrevRec','dtRealRec','infoColetadasRecon')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(Ponto,Pontos)

class ServidoresMembros(admin.ModelAdmin):
    list_display =('nome','matricula','func','orgao','sexo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(ServidorMembro,ServidoresMembros)

class PartsRecon(admin.ModelAdmin):
    list_display =('idPonto','idServidorMembro')
    list_display_list =('id','idPonto')
    search_field =('idPonto')
    list_page = 20
admin.site.register(PartRecon,PartsRecon)

class Operacoes(admin.ModelAdmin):
    list_display =('servidorMembroIdResp','ratBos','fase','contato','sintese','objetivoEspecifico','evidenciasDigitais','valoresBens','naoBuscar','idProc')
    list_display_list =('id','sintese')
    search_field =('sintese')
    list_page = 20
admin.site.register(Operacao,Operacoes)

