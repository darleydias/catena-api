from rest_framework import viewsets
from appCatena.models import Comarca, Promotor, TipoOperacao,TipoProcedimento,Procedimento
from appCatena.serializer import TipoOperacaoSerializer, TipoProcedimentoSerializer, ProcedimentoSerializer, PromotorSerializer,ComarcaSerializer

class TiposOperacaoViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoOperacao.objects.all()
    serializer_class = TipoOperacaoSerializer

class TiposProcedimentoViewSet(viewsets.ModelViewSet):
    """Exibe todos os tipos de procedimentos"""
    queryset = TipoProcedimento.objects.all()
    serializer_class = TipoProcedimentoSerializer

class ProcedimentosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer


class PromotoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Promotor.objects.all()
    serializer_class = PromotorSerializer


class ComarcasViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Comarca.objects.all()
    serializer_class = ComarcaSerializer