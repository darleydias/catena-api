from django.contrib import admin
from appCatena.models import TipoProcesso, TipoOperacao, Promotor, Procedimento

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
admin.site.register(TipoProcesso,TpProcesso)
class TiposOperacao(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(TipoOperacao,TiposOperacao)
class Procedimentos(admin.ModelAdmin):
    list_display =('id','tipo','nrPro','descri','comarca')
    list_display_list =('id','descri')
    search_field =('nrPro','descri','comarca')
    list_page = 20
admin.site.register(Procedimento,Procedimentos)
class Promotores(admin.ModelAdmin):
    list_display =('id','nome','mamp','idComarca','sexo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(Promotor,Promotores)