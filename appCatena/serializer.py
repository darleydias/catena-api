from rest_framework import serializers
from appCatena.models import TipoProcedimento, Procedimento, TipoOperacao

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
