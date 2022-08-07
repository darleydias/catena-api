from rest_framework import viewsets
from appCatena.models import TipoOperacao,TipoProcedimento,Procedimento
from appCatena.serializer import TipoOperacaoSerializer, TipoProcedimentoSerializer, ProcedimentoSerializer

class TiposOperacaoViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoOperacao.objects.all()
    serializer_class = TipoOperacaoSerializer

class TiposProcedimentoViewSet(viewsets.ModelViewSet):
    """Exibe todos os tipos de procedimentos"""
    queryset = TipoProcedimento.objects.all()
    serializer_class = TipoProcedimentoSerializer

class ProcedimentoViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer