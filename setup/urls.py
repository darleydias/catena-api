from django.contrib import admin
from django.urls import path
from appCatena.views import tiposProcesso

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tiposProcesso/", tiposProcesso)
]