from django.db import models
from datetime import datetime

class TipoProcedimento(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    #para representar cada objeto tipoProcesso pela descri
    def __str__(self):
        return self.descri

class TipoOperacao(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Procedimento(models.Model):
    tipo = models.IntegerField()
    descri = models.CharField(max_length = 240)
    nrPro = models.CharField(max_length = 150)
    comarca = models.CharField(max_length = 150)
    idPromotor = models.IntegerField()
    def __str__(self):
        return self.proced

class Promotor(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    nome = models.CharField(max_length = 240)
    mamp = models.CharField(max_length = 20)
    idComarca = models.IntegerField()
    sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
    def __str__(self):
        return self.nome

class Comarca(models.Model):
    TIPO = (
        ('N','Normal'),
        ('E','Especial')
    )
    nome = models.CharField(max_length = 240)
    sigla = models.CharField(max_length = 20)
    idComarca = models.IntegerField()
    sexo = models.CharField(max_length = 1,choices=TIPO,default = 'N',blank = False, null=False)
    def __str__(self):
        return self.nome


        