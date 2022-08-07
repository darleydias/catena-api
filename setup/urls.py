from django.contrib import admin
from django.urls import path,include
from appCatena.views import TiposOperacaoViewSet,TiposProcedimentoViewSet,ProcedimentosViewSet,PromotoresViewSet,ComarcasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tiposOperacao',TiposOperacaoViewSet,basename='TiposOperacao')
router.register('tiposProcesso',TiposProcedimentoViewSet,basename='TiposProcedimento')
router.register('procedimentos',ProcedimentosViewSet,basename='Procedimentos')
router.register('comarcas',ComarcasViewSet,basename='Comarcas')
router.register('promotores',PromotoresViewSet,basename='Promotores')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
]
