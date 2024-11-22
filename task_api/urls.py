from django.urls import path
from .views import user_view, task_view, TaskRetrieveUpdateAPIView, TaskDeleteAPIView

# Define as rotas para os endpoints da aplicação
urlpatterns = [
    # Rota para listar e criar usuários
    path('users/', user_view, name='create_user'),  
    # Endpoint: /users/
    # View associada: user_view
    # Nome do endpoint: 'create_user'

    # Rota para listar e criar tarefas
    path('tasks/', task_view, name='create_task'),  
    # Endpoint: /tasks/
    # View associada: task_view
    # Nome do endpoint: 'create_task'

    # Rota para recuperar e atualizar uma tarefa específica pelo ID
    path('tasks/<int:pk>/', TaskRetrieveUpdateAPIView.as_view(), name='task-retrieve-update'),  
    # Endpoint: /tasks/<int:pk>/
    # View associada: TaskRetrieveUpdateAPIView
    # Nome do endpoint: 'task-retrieve-update'

    # Rota para excluir uma tarefa específica pelo ID
    path('tasks/del/<int:pk>/', TaskDeleteAPIView.as_view(), name='task-delete'),  
    # Endpoint: /tasks/del/<int:pk>/
    # View associada: TaskDeleteAPIView
    # Nome do endpoint: 'task-delete'
]


