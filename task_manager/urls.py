from django.contrib import admin
from django.urls import path, include

# Configuração das URLs principais do projeto
urlpatterns = [
    path('admin/', admin.site.urls),  
    # Rota para o painel de administração do Django
    # Endpoint: /admin/
    # Fornece uma interface de administração para gerenciar dados diretamente no banco

    path('api/', include('task_api.urls')),  
    # Inclui as URLs do aplicativo "task_api"
    # Endpoint: /api/
    # Redireciona as requisições para o arquivo de URLs do aplicativo "task_api"
    # Essa abordagem modulariza as rotas, permitindo organizar os endpoints relacionados ao aplicativo
]
