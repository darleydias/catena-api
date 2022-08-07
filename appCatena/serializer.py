from rest_framework import serializers
from appCatena.models import TipoProcedimento, Procedimento, TipoOperacao, Promotor, Comarca

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