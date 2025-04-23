from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Sistema funcionando! API disponível nos endpoints configurados.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/v1/', include('authentication.urls')),  # Inclui as URLs do app 'authentication'
    path('api/v1/', include('decano.urls')),
    path('api/v1/', include('nucleo.urls')),
    path('api/v1/', include('pacientes.urls')),
    path('api/v1/', include('relatorio.urls')),
    path('api/v1/', include('terapeuta.urls')),
]
