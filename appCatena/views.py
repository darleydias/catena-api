from django.http import JsonResponse
import datetime

def tiposProcesso(request):
    current_datetime = datetime.datetime.now()  
    if request.method=="GET":
        tipoProcesso={'tpPro_id':1,'tpPro_descri':'IPM','tpPro_dh':current_datetime}
        return JsonResponse(tipoProcesso)