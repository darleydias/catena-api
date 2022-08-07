from rest_framework import viewsets
from appCatena.models import TipoOperacao,TipoProcesso
from appCatena.serializer import TipoOperacaoSerializer, TipoProcessoSerializer

class TiposOperacaoViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoOperacao.objects.all()
    serializer_class = TipoOperacaoSerializer

class TiposProcessoViewSet(viewsets.ModelViewSet):
    """Exibe todos os tipos de operações"""
    queryset = TipoProcesso.objects.all()
    serializer_class = TipoProcessoSerializer