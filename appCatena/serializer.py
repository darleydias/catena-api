from rest_framework import serializers
from appCatena.models import EquipeOperacao, EquipeRecon, Evidencia, Extensao, Funcao, Funcionario, Midea, MideaEvidencia, MimeType, Operacao, Orgao, PontoOperacao, Recon, Setor, TipoEvidencia, TipoMidea, TipoProcedimento, Procedimento, TipoOperacao, Promotor, Comarca,Alvo,Ponto

class TipoProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcedimento
        fields = ['id','descri','dtTime']

class TipoEvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvidencia
        fields = ['id','descri','dtTime']

class TipoOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacao
        fields = '__all__'

class MimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MimeType
        fields = '__all__'


class ExtensaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extensao
        fields = '__all__'


class TipoMideaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMidea
        fields = '__all__'

class ComarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comarca
        fields = '__all__'

class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = '__all__'

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class MideaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Midea
        fields = '__all__'

class AlvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvo
        fields = '__all__'

class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'

class OperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacao
        fields = '__all__'

class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = '__all__'

class EvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencia
        fields = '__all__'

class PromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotor
        fields = '__all__'

class ReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recon
        fields = '__all__'

class PontosOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoOperacao
        fields = '__all__'

class EquipeReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeRecon
        fields = '__all__'

class EquipeOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeOperacao
        fields = '__all__'
        
class MideaEvidenciaOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MideaEvidencia
        fields = '__all__'
        

