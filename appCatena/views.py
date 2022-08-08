from rest_framework import viewsets
from appCatena.models import Comarca, Promotor, TipoOperacao,TipoProcedimento,Procedimento,Ponto,PartRecon,Alvo,ServidorMembro,Operacao
from appCatena.serializer import AlvoSerializer, OperacaoSerializer, PontoSerializer, ServidorMembroSerializer, TipoOperacaoSerializer, TipoProcedimentoSerializer, ProcedimentoSerializer, PromotorSerializer,ComarcaSerializer,PartReconSerializer

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

class PontosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer

class PartsReconViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = PartRecon.objects.all()
    serializer_class = PartReconSerializer

class AlvosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Alvo.objects.all()
    serializer_class = AlvoSerializer

class ServidoresMembrosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = ServidorMembro.objects.all()
    serializer_class = ServidorMembroSerializer

class OperacoesViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer