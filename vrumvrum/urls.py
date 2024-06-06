from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('autenticacao.urls')),
    path('admin/', admin.site.urls),
    path('', include ('cadastros.urls')),
    path('', include ('usuarios.urls')),
]
