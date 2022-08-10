from rest_framework import viewsets,generics
from appCatena.models import Comarca, EquipeOperacao, EquipeRecon, Evidencia, Extensao, Funcao, Funcionario, Midea, MideaEvidencia, MimeType, Orgao, PontoOperacao, Promotor, Recon, Setor, TipoEvidencia, TipoMidea, TipoOperacao,TipoProcedimento,Procedimento,Ponto,Alvo,Operacao
from appCatena.serializer import AlvoSerializer, EquipeOperacaoSerializer, EquipeReconSerializer, EvidenciaSerializer, ExtensaoSerializer, FuncaoSerializer, FuncionarioSerializer, MideaEvidenciaOperacaoSerializer, MideaSerializer, MimeTypeSerializer, OperacaoSerializer, OrgaoSerializer, PontoSerializer, PontosOperacaoSerializer, ReconSerializer, SetorSerializer, TipoEvidenciaSerializer, TipoMideaSerializer, TipoOperacaoSerializer, TipoProcedimentoSerializer, ProcedimentoSerializer, PromotorSerializer,ComarcaSerializer,ListaFuncionariosOperacaoSerializer

class TiposProcedimentoViewSet(viewsets.ModelViewSet):
    """Exibe todos os tipos de procedimentos"""
    queryset = TipoProcedimento.objects.all()
    serializer_class = TipoProcedimentoSerializer

class TiposEvidenciaViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoEvidencia.objects.all()
    serializer_class = TipoEvidenciaSerializer

class TiposOperacaoViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoOperacao.objects.all()
    serializer_class = TipoOperacaoSerializer

class MimeTypesViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = MimeType.objects.all()
    serializer_class = MimeTypeSerializer

class ExtensoesViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = Extensao.objects.all()
    serializer_class = ExtensaoSerializer

class TipoMideasViewSet(viewsets.ModelViewSet):
    """ Exibir todos os tipos de operações """
    queryset = TipoMidea.objects.all()
    serializer_class = TipoMideaSerializer

class ComarcasViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Comarca.objects.all()
    serializer_class = ComarcaSerializer

class OrgaosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Orgao.objects.all()
    serializer_class = OrgaoSerializer

class FuncoesViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

class FuncionariosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class SetoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class MideasViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Midea.objects.all()
    serializer_class = MideaSerializer


class AlvosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Alvo.objects.all()
    serializer_class = AlvoSerializer

class ProcedimentosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Procedimento.objects.all()
    serializer_class = ProcedimentoSerializer

class OperacoesViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer

class PontosViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer

class EvidenciaViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer

class PromotoresViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Promotor.objects.all()
    serializer_class = PromotorSerializer

class ReconsViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = Recon.objects.all()
    serializer_class = ReconSerializer

class PontosOperacaoViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = PontoOperacao.objects.all()
    serializer_class = PontosOperacaoSerializer

class EquipesReconViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = EquipeRecon.objects.all()
    serializer_class = EquipeReconSerializer

class EquipesOperacaoViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = EquipeOperacao.objects.all()
    serializer_class = EquipeOperacaoSerializer

class MideasEvidenciaViewSet(viewsets.ModelViewSet):
    """Exibe todos os procedimentos"""
    queryset = MideaEvidencia.objects.all()
    serializer_class = MideaEvidenciaOperacaoSerializer


####################   Listando as funções de um orgao  ##########################

class ListaFuncionariosOperacao(generics.ListAPIView):
    def get_queryset(self):
        queryset = EquipeOperacao.objects.filter(operacao__id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaFuncionariosOperacaoSerializer