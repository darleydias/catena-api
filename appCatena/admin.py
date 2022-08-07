from django.contrib import admin
from appCatena.models import TipoProcedimento, TipoOperacao, Promotor, Procedimento,Comarca

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