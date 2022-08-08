from django.contrib import admin
from django.urls import path,include
from appCatena.views import OperacoesViewSet, TiposOperacaoViewSet,TiposProcedimentoViewSet,ProcedimentosViewSet,PromotoresViewSet,ComarcasViewSet,ServidoresMembrosViewSet,AlvosViewSet,PartsReconViewSet,PontosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tiposOperacao',TiposOperacaoViewSet,basename='TiposOperacao')
router.register('tiposProcesso',TiposProcedimentoViewSet,basename='TiposProcedimento')
router.register('procedimentos',ProcedimentosViewSet,basename='Procedimentos')
router.register('comarcas',ComarcasViewSet,basename='Comarcas')
router.register('promotores',PromotoresViewSet,basename='Promotores')
router.register('servidoresMembros',ServidoresMembrosViewSet,basename='ServidoresMembros')
router.register('partsRecon',PartsReconViewSet,basename='PartsRecon')
router.register('ponto',PontosViewSet,basename='Pontos')
router.register('alvo',AlvosViewSet,basename='Alvos')
router.register('operacao',OperacoesViewSet,basename='Operacoes')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
]
