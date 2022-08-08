from rest_framework import serializers
from appCatena.models import Operacao, TipoProcedimento, Procedimento, TipoOperacao, Promotor, Comarca,Alvo,ServidorMembro,PartRecon,Ponto

class TipoProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcedimento
        fields = ['id','descri','dtTime']

class TipoOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacao
        fields = '__all__'

class ProcedimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'

class PromotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotor
        fields = '__all__'

class ComarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comarca
        fields = '__all__'
        
class AlvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvo
        fields = '__all__'

class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = '__all__'

class ServidorMembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServidorMembro
        fields = '__all__'

class PartReconSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRecon
        fields = '__all__'
class OperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacao
        fields = '__all__'

