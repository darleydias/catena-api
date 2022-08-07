from rest_framework import serializers
from appCatena.models import TipoProcesso, TipoOperacao

class TipoProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcesso
        fields = ['id','descri','dtTime']

class TipoOperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOperacao
        fields = '__all__'

