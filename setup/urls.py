from django.contrib import admin
from django.urls import path,include
# from appCatena.models import Funcao, Orgao
from appCatena.views import EquipesOperacaoViewSet, EquipesReconViewSet, EvidenciaViewSet, ExtensoesViewSet, FuncoesViewSet, FuncionariosViewSet, ListaFuncionariosOperacao, MideasEvidenciaViewSet, MideasViewSet, MimeTypesViewSet, OperacoesViewSet, OrgaosViewSet, PontosOperacaoViewSet, ReconsViewSet, SetoresViewSet, TipoMideasViewSet, TiposEvidenciaViewSet, TiposOperacaoViewSet,TiposProcedimentoViewSet,ProcedimentosViewSet,PromotoresViewSet,ComarcasViewSet,AlvosViewSet,PontosViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('tiposProcedimento',TiposProcedimentoViewSet,basename='TipoProcedimento')
router.register('tiposEvidencia',TiposEvidenciaViewSet,basename='TipoEvidencia')
router.register('tiposOperacao',TiposOperacaoViewSet,basename='TipoOperacao')
router.register('mimesType',MimeTypesViewSet,basename='MimeType')
router.register('extensoes',ExtensoesViewSet,basename='Extensao')
router.register('tiposMidea',TipoMideasViewSet,basename='TipoMidea')
router.register('comarcas',ComarcasViewSet,basename='Comarca')
router.register('Orgaos',OrgaosViewSet,basename='Orgao')
router.register('funcoes',FuncoesViewSet,basename='Funcao')
router.register('funcionarios',FuncionariosViewSet,basename='Funcionario')
router.register('setores',SetoresViewSet,basename='Setor')
router.register('mideas',MideasViewSet,basename='Midea')
router.register('alvos',AlvosViewSet,basename='Alvo')
router.register('procedimentos',ProcedimentosViewSet,basename='Procedimento')
router.register('operacoes',OperacoesViewSet,basename='Operacao')
router.register('pontos',PontosViewSet,basename='Ponto')
router.register('evidencias',EvidenciaViewSet,basename='Evidencia')
router.register('promotores',PromotoresViewSet,basename='Promotor')
router.register('recons',ReconsViewSet,basename='Recon')
router.register('pontosOperacao',PontosOperacaoViewSet,basename='PontoOperacao')
router.register('equipesRecon',EquipesReconViewSet,basename='EquipeRecon') 
router.register('equipesOperacao',EquipesOperacaoViewSet,basename='EquipeOperacao') 
router.register('mideasEvidencia',MideasEvidenciaViewSet,basename='MideaEvidencia') 


# router.register('tiposOperacao',TiposOperacaoViewSet,basename='TiposOperacao')
# router.register('tiposProcesso',TiposProcedimentoViewSet,basename='TiposProcedimento')
# router.register('procedimentos',ProcedimentosViewSet,basename='Procedimentos')
# router.register('comarcas',ComarcasViewSet,basename='Comarcas')
# router.register('promotores',PromotoresViewSet,basename='Promotores')
# router.register('servidoresMembros',ServidoresMembrosViewSet,basename='ServidoresMembros')
# router.register('partsRecon',PartsReconViewSet,basename='PartsRecon')
# router.register('ponto',PontosViewSet,basename='Pontos')
# router.register('alvo',AlvosViewSet,basename='Alvos')
# router.register('operacao',OperacoesViewSet,basename='Operacoes')

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("operacao/<int:pk>/EquipeOperacao/",ListaFuncionariosOperacao.as_view())
]
