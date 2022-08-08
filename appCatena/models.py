from django.db import models
from datetime import datetime

class TipoProcedimento(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    #para representar cada objeto tipoProcesso pela descri
    def __str__(self):
        return self.descri

class Ponto(models.Model):
    nrPonto = models.CharField(max_length = 100)
    idOperacao = models.IntegerField() #id da tabela de Operação
    descri = models.CharField(max_length = 240) 
    orientacaoRecon = models.TextField()
    endereco = models.TextField() # texto completo obtido de uma API de endereço
    latLong = models.CharField(max_length=40) # exemplo :  -25.330803399999997,-49.135661000000006 obtido de uma API de endereço
    complemento = models.TextField()
    resp = models.CharField(max_length = 10) # mamp
    idAlvo = models.IntegerField() # id da tabela de alvo
    dtPrevRec = models.DateTimeField(default=datetime.now,blank=True) # Data prevista de RECON
    dtRealRec = models.DateTimeField(default=datetime.now,blank=True) # Data que ocorreu o RECON
    infoColetadasRecon = models.TextField()
    def __str__(self):
        return self.descri

class Operacao(models.Model):
    nome = models.CharField(max_length = 150)
    servidorMembroIdResp = models.IntegerField()
    ratBos = models.CharField(max_length = 150)
    fase = models.CharField(max_length = 10)
    contato = models.CharField(max_length = 240) #canal de contato com os membros da operação
    sintese = models.TextField()
    objetivoGeral = models.TextField()
    objetivoEspecifico = models.TextField()
    evidenciasDigitais = models.TextField()
    valoresBens = models.TextField()
    naoBuscar = models.TextField()
    idProc = models.IntegerField()
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    ponto = models.ForeignKey(Ponto,on_delete=models.CASCADE)
    #para representar cada objeto tipoProcesso pela descri
    def __str__(self):
        return self.nome

class TipoOperacao(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Procedimento(models.Model):
    tipo = models.IntegerField()
    descri = models.CharField(max_length = 240)
    nrPro = models.CharField(max_length = 150)
    idComarca = models.CharField(max_length = 150)
    idPromotor = models.IntegerField()
    def __str__(self):
        return self.descri

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
    tipo = models.CharField(max_length = 1,choices=TIPO,default = 'N',blank = False, null=False)
    def __str__(self):
        return self.nome

class PartRecon(models.Model): #pessoas que são participantes do RECON no ponto
    idPonto = models.CharField(max_length = 100) #id da tabela de pontos
    idServidorMembro = models.IntegerField() #id da tabela de servidorMembros
    def __str__(self):
        return self.idPonto

class Alvo(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )    
    UF = (('RS','Rio Grande do Sul'),('SC','Santa Catarina'),('PR','Paraná'),('SP','São Paulo'),('ES','Espírito Santo'),('MG','Minas Gerais'),('MS','Mato grosso do Sul'),('MT','Mato Grosso'))
    nome = models.CharField(max_length = 200) 
    alcunha = models.CharField(max_length = 200)
    cpf = models.CharField(max_length = 40)
    rg = models.CharField(max_length = 30)
    ufRg = models.CharField(max_length = 2,choices=UF,default = 'MG',blank = False, null=False)
    sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
    dtNasc = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.nome

class ServidorMembro(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )    
    UF = (('RS','Rio Grande do Sul'),('SC','Santa Catarina'),('PR','Paraná'),('SP','São Paulo'),('ES','Espírito Santo'),('MG','Minas Gerais'),('MS','Mato grosso do Sul'),('MT','Mato Grosso'))
    FUNCAO = (('MMP','Membro MP'),('SMP','Servidor MP'),('OF','Oficial da Policial Militar'),('PR','Praça da Policial Militar'),('PC','Policial Civil'),('SEF','Servidor da SEF'))
    ORGAO = (('MP','Ministério Público'),('PM','Polícia Militar'),('PC','Policia Civil'),('SF','Secretariua da Fazenda'))
    
    nome = models.CharField(max_length = 200) 
    matricula = models.CharField(max_length = 20)
    func = models.CharField(max_length = 3,choices=FUNCAO,default = 'MMP',blank = False, null=False)    
    orgao = models.CharField(max_length = 2,choices=ORGAO,default = 'MMP',blank = False, null=False)    
    sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
    def __str__(self):
        return self.nome