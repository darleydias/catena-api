from django.db import models
from datetime import datetime

class tiposProcesso(models.Model):
    descri = models.CharField(max_length = 150)
    dtTime = models.DateTimeField(default=datetime.now,blank=True)

     
    