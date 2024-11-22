from rest_framework import status  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from .models import User, Task  
from .serializers import UserSerializer, TaskSerializer 
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView  

# View para listar e criar usuários
@api_view(['GET', 'POST'])  # Define que esta view aceita requisições GET e POST
def user_view(request):
    if request.method == 'GET':  # Quando o método for GET
        users = User.objects.all()  # Recupera todos os usuários do banco de dados
        serializer = UserSerializer(users, many=True)  # Serializa os dados em uma lista
        return Response(serializer.data)  # Retorna os dados serializados no formato JSON
    
    elif request.method == 'POST':  # Quando o método for POST
        serializer = UserSerializer(data=request.data)  # Cria o serializer com os dados enviados
        if serializer.is_valid():  # Valida os dados
            serializer.save()  # Salva o novo usuário no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados criados e o status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna os erros e o status 400

# View para listar e criar tarefas
@api_view(['GET', 'POST'])  # Define que esta view aceita requisições GET e POST
def task_view(request):
    if request.method == 'GET':  # Quando o método for GET
        tasks = Task.objects.all()  # Recupera todas as tarefas do banco de dados
        serializer = TaskSerializer(tasks, many=True)  # Serializa os dados em uma lista
        return Response(serializer.data)  # Retorna os dados serializados no formato JSON
    
    elif request.method == 'POST':  # Quando o método for POST
        serializer = TaskSerializer(data=request.data)  # Cria o serializer com os dados enviados
        if serializer.is_valid():  # Valida os dados
            serializer.save()  # Salva a nova tarefa no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna os dados criados e o status 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna os erros e o status 400

# View para recuperar e atualizar uma tarefa específica
class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()  # Define o conjunto de dados como todas as tarefas
    serializer_class = TaskSerializer  # Usa o serializer TaskSerializer para processar os dados
    # Esta classe lida automaticamente com GET (recuperação de uma tarefa) e PUT/PATCH (atualização de uma tarefa)

# View para excluir uma tarefa específica
class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()  # Define o conjunto de dados como todas as tarefas
    serializer_class = TaskSerializer  # Usa o serializer TaskSerializer para processar os dados
    # Esta classe lida automaticamente com DELETE para remover a tarefa específica
