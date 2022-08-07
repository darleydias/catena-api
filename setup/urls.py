from django.contrib import admin
from django.urls import path,include
from appCatena.views import TiposOperacaoViewSet,TiposProcessoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tiposOperacao',TiposOperacaoViewSet,basename='TiposOperacao')
router.register('tiposProcesso',TiposProcessoViewSet,basename='TiposProcedimento')
router.register('procedimentos',TiposProcessoViewSet,basename='Procedimento')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
]
