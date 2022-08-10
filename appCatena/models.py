from django.db import models
from datetime import datetime
from smart_selects.db_fields import GroupedForeignKey

######## Classes tipo ########

class TipoProcedimento(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class TipoEvidencia(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class TipoOperacao(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class MimeType(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Extensao(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class TipoMidea(models.Model):
    descri = models.CharField(max_length = 150)
    mimeType = models.ForeignKey(MimeType,on_delete=models.CASCADE)
    extensao = models.ForeignKey(Extensao,on_delete=models.CASCADE)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri



######### Classes entidades ###############

class Comarca(models.Model):
    TIPO = (
        ('N','Normal'),
        ('E','Especial')
    )
    nome = models.CharField(max_length = 240,verbose_name="Nome")
    sigla = models.CharField(max_length = 20,verbose_name="Sigla")
    tipo = models.CharField(max_length = 1,choices=TIPO,default = 'N',blank = False, null=False,verbose_name="Tipo")
    class Meta:
       ordering = ['nome']
    def __str__(self):
        return self.nome

class Orgao(models.Model):
    descri = models.CharField(max_length = 240,verbose_name="Descrição") 
    sigla = models.CharField(max_length = 20,verbose_name="Sigla")
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Funcao(models.Model):
    orgao = models.ForeignKey(Orgao,on_delete=models.CASCADE)
    descri = models.CharField(max_length = 240,verbose_name="Descrição") 
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Funcionario(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )    
    UF = (('RS','Rio Grande do Sul'),('SC','Santa Catarina'),('PR','Paraná'),('SP','São Paulo'),('ES','Espírito Santo'),('MG','Minas Gerais'),('MS','Mato grosso do Sul'),('MT','Mato Grosso'))
    nome = models.CharField(max_length = 200) 
    orgao = models.ForeignKey(Orgao,on_delete=models.CASCADE)
    matricula = models.CharField(max_length = 20)
    cpf = models.CharField(max_length = 20)
    funcao = models.ForeignKey(Funcao,on_delete=models.CASCADE)
    sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
    dtNasc = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.nome

class Setor(models.Model):
    orgao = models.ForeignKey(Orgao,on_delete=models.CASCADE)
    descri = models.CharField(max_length = 240,verbose_name="Descrição") 
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Midea(models.Model):
    descri = models.CharField(max_length = 240) 
    url = models.CharField(max_length = 244) 
    tipoMidea = models.ForeignKey(TipoMidea,on_delete=models.CASCADE)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

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

class Promotor(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    nome = models.CharField(max_length = 240)
    mamp = models.CharField(max_length = 20)
    comarca = models.ForeignKey(Comarca,on_delete=models.CASCADE)
    sexo = models.CharField(max_length = 1,choices=SEXO,default = 'M',blank = False, null=False)
    dtNasc = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.nome


class Procedimento(models.Model):
    tipoProcedimento = models.ForeignKey(TipoProcedimento,on_delete=models.CASCADE)
    descri = models.CharField(max_length = 240)
    nrPro = models.CharField(max_length = 150)
    comarca = models.ForeignKey(Comarca,on_delete=models.CASCADE)
    promotor = models.ForeignKey(Promotor,on_delete=models.CASCADE)
    def __str__(self):
        return self.descri

class Operacao(models.Model):
    tipoOperacao = models.ForeignKey(TipoOperacao,on_delete=models.CASCADE)
    nome = models.CharField(max_length = 150)
    funcionarioResp = models.ForeignKey(Promotor,on_delete=models.CASCADE)
    ratBos = models.CharField(max_length = 150)
    fase = models.CharField(max_length = 10)
    contato = models.CharField(max_length = 240) #canal de contato com os membros da operação
    sintese = models.TextField()
    objetivoGeral = models.TextField()
    objetivoEspecifico = models.TextField()
    evidenciasDigitais = models.TextField()
    valoresBens = models.TextField()
    naoBuscar = models.TextField()
    procedimento = models.ForeignKey(Procedimento,on_delete=models.CASCADE)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    #para representar cada objeto tipoProcesso pela descri
    def __str__(self):
        return self.nome

class Ponto(models.Model):
    nrPonto = models.CharField(max_length = 100)
    operacao = models.ForeignKey(Operacao,on_delete=models.CASCADE)
    descri = models.CharField(max_length = 240) 
    endereco = models.TextField() # texto completo obtido de uma API de endereço
    latLong = models.CharField(max_length=40) # exemplo :  -25.330803399999997,-49.135661000000006 obtido de uma API de endereço
    complemento = models.TextField()
    alvo = models.ForeignKey(Alvo,on_delete=models.CASCADE)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.descri

class Evidencia(models.Model):
    nrPonto = models.CharField(max_length = 100)
    dtTimeColeta = models.DateTimeField(default=datetime.now,blank=True)
    operacao = models.ForeignKey(Operacao,on_delete=models.CASCADE)
    tipoEvidencia = models.ForeignKey(TipoEvidencia,on_delete=models.CASCADE)
    setorAtual = models.ForeignKey(Setor,on_delete=models.CASCADE)
    descri = models.CharField(max_length = 240) 
    status = models.CharField(max_length = 100)
    def __str__(self):
        return self.descri

class Recon(models.Model):
    orientacaoRecon = models.TextField()
    dtPrev = models.DateTimeField(default=datetime.now,blank=True,verbose_name="Data Prevista") # Data prevista de RECON
    dtReal = models.DateTimeField(default=datetime.now,blank=True,verbose_name="Data do Recon") # Data que ocorreu o RECON
    infoColetadasRecon = models.TextField(verbose_name="Informação Coletada")
    ponto = models.ForeignKey(Ponto,on_delete=models.CASCADE,verbose_name="Ponto")
    alvo = models.ForeignKey(Alvo,on_delete=models.CASCADE,verbose_name="Alvo")
    def __str__(self):
        return self.ponto


############# Classes relacionais N | N

class PontoOperacao(models.Model): #Vários pontos de uma operação
    orientacao = models.TextField()
    operacao = models.ForeignKey(Operacao,on_delete=models.CASCADE)
    # ponto = models.ForeignKey(Ponto,on_delete=models.CASCADE)
    ponto = GroupedForeignKey(Ponto,"operacao")
    def __str__(self):
        return self.ponto

class EquipeRecon(models.Model): #Varias pessoa s em um Recon
    recon = models.ForeignKey(Recon,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    def __str__(self):
        return self.recon

class EquipeOperacao(models.Model): #Varias pessoa s em um Recon
    FUNCAO = (
        ('C','Coordenação'),
        ('M','Membro')
    )  
    funcao = models.CharField(max_length = 1,choices=FUNCAO,default = 'M',blank = False, null=False)
    operacao = models.ForeignKey(Operacao,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    def __str__(self):
        return self.funcao
        
class MideaEvidencia(models.Model): #Varias pessoa s em um Recon
    midea = models.ForeignKey(Midea,on_delete=models.CASCADE)
    evidencia = models.ForeignKey(Evidencia,on_delete=models.CASCADE)
    def __str__(self):
        return self.evidencia