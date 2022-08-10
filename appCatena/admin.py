from mimetypes import MimeTypes
from token import OP
from django.contrib import admin
from appCatena.models import EquipeOperacao, EquipeRecon, Evidencia, Extensao, Funcao, Funcionario, Midea, MideaEvidencia, MimeType, Operacao, Orgao, PontoOperacao, Recon, Setor, TipoEvidencia, TipoMidea,TipoProcedimento, TipoOperacao, Promotor, Procedimento,Comarca,Ponto,Alvo

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

class TiposEvidencia(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(TipoEvidencia,TiposEvidencia)

class TiposOperacao(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(TipoOperacao,TiposOperacao)

class MimeTypes(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(MimeType,MimeTypes)

class Extensoes(admin.ModelAdmin):
    list_display =('id','descri')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(Extensao,Extensoes)

class TiposMidea(admin.ModelAdmin):
    list_display =('id','descri','extensao','mimeType')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(TipoMidea,TiposMidea)

class Comarcas(admin.ModelAdmin):
    list_display =('id','nome','sigla','tipo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(Comarca,Comarcas)

class Orgaos(admin.ModelAdmin):
    list_display =('id','sigla','descri')
    list_display_list =('id','descri')
    search_field =('sigla','descri')
    list_page = 20
admin.site.register(Orgao,Orgaos)

class Funcoes(admin.ModelAdmin):
    list_display =('id','orgao','descri')
    list_display_list =('id','descri')
    search_field =('descri','orgao')
    list_page = 20
admin.site.register(Funcao,Funcoes)

class Funcionarios(admin.ModelAdmin):
    list_display =('id','nome','orgao','matricula','cpf','funcao','sexo','dtNasc')
    list_display_list =('id','nome','matricula')
    search_field =('nome','matricula')
    list_page = 20
admin.site.register(Funcionario,Funcionarios)

class Setores(admin.ModelAdmin):
    list_display =('id','orgao','descri')
    list_display_list =('id','descri')
    search_field =('descri','orgao')
    list_page = 20
admin.site.register(Setor,Setores)

class Midias(admin.ModelAdmin):
    list_display =('id','tipoMidea','descri','url')
    list_display_list =('id','descri')
    search_field =('descri','tipoMidea')
    list_page = 20
admin.site.register(Midea,Midias)

class Alvos(admin.ModelAdmin):
    list_display =('id','nome','alcunha','sexo','dtNasc','cpf','rg','ufRg')
    list_display_list =('id','nome')
    search_field =('nome','alcunha')
    list_page = 20
admin.site.register(Alvo,Alvos)

class Procedimentos(admin.ModelAdmin):
    list_display =('id','tipoProcedimento','nrPro','descri')
    list_display_list =('id','descri')
    search_field =('nrPro','descri','tipo')
    list_page = 20
admin.site.register(Procedimento,Procedimentos)

class Operacoes(admin.ModelAdmin):
    list_display =('funcionarioResp','ratBos','fase','contato','sintese','objetivoEspecifico','evidenciasDigitais','valoresBens','naoBuscar','procedimento')
    list_display_list =('id','sintese')
    search_field =('sintese')
    list_page = 20
admin.site.register(Operacao,Operacoes)

class Pontos(admin.ModelAdmin):
    list_display =('nrPonto','operacao','descri','endereco','complemento','alvo')
    list_display_list =('id','nrPonto')
    search_field =('nrPonto','operacao')
    list_page = 20
admin.site.register(Ponto,Pontos)

class Evidencias(admin.ModelAdmin):
    list_display =('nrPonto','dtTimeColeta','operacao','descri','tipoEvidencia','setorAtual','status')
    list_display_list =('id','descri')
    search_field =('descri')
    list_page = 20
admin.site.register(Evidencia,Evidencias)

class Promotores(admin.ModelAdmin):
    list_display =('id','nome','mamp','comarca','sexo')
    list_display_list =('id','nome')
    search_field =('nome')
    list_page = 20
admin.site.register(Promotor,Promotores)

class Recons(admin.ModelAdmin):
    list_display =('id','orientacaoRecon','dtPrev','dtReal','infoColetadasRecon','ponto','alvo')
    list_display_list =('id','ponto')
    search_field =('ponto')
    list_page = 20
admin.site.register(Recon,Recons)

class PontosOperacao(admin.ModelAdmin):
    list_display =('orientacao','operacao','ponto')
    list_display_list =('id','operacao','ponto')
    search_field =('operacao','ponto')
    list_page = 20
admin.site.register(PontoOperacao,PontosOperacao)

class EquipesRecon(admin.ModelAdmin):
    list_display =('recon','funcionario')
    list_display_list =('recon','funcionario')
    search_field =('recon','funcionario')
    list_page = 20
admin.site.register(EquipeRecon,EquipesRecon)

class EquipesOperacao(admin.ModelAdmin):
    list_display =('operacao','funcionario','funcao')
    list_display_list =('operacao','funcionario')
    search_field =('operacao','funcionario')
    list_page = 20
admin.site.register(EquipeOperacao,EquipesOperacao)

class MidiasEvidencia(admin.ModelAdmin):
    list_display =('midea','evidencia')
    list_display_list =('midea','evidencia')
    search_field =('evidencia')
    list_page = 20
admin.site.register(MideaEvidencia,MidiasEvidencia)

