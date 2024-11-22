from django.db import models

# Modelo para representar os usuários do sistema
class User(models.Model):
    id = models.AutoField(primary_key=True)  # Chave primária gerada automaticamente para cada usuário
    username = models.CharField(max_length=100, unique=True)  # Nome de usuário único com limite de 100 caracteres
    email = models.EmailField(unique=True)  # E-mail único, validado automaticamente pelo Django

    def __str__(self):
        return self.username  # Retorna o nome de usuário como representação textual do objeto

# Modelo para representar tarefas associadas a usuários
class Task(models.Model):
    # Opções de status que podem ser atribuídas a uma tarefa
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),  # Tarefa ainda não iniciada
        ('fazendo', 'Fazendo'),   # Tarefa em andamento
        ('concluido', 'Concluído')  # Tarefa finalizada
    ]

    # Opções de prioridade que podem ser atribuídas a uma tarefa
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),  # Tarefa com prioridade baixa
        ('media', 'Média'),  # Tarefa com prioridade média
        ('alta', 'Alta')     # Tarefa com prioridade alta
    ]

    id = models.AutoField(primary_key=True)  # Chave primária gerada automaticamente para cada tarefa
    usuario = models.ForeignKey(  # Cria uma relação entre tarefas e usuários
        User, 
        related_name='tasks',  # Permite acessar as tarefas de um usuário usando "user.tasks"
        on_delete=models.CASCADE  # Exclui todas as tarefas associadas ao usuário quando ele for removido
    )
    descricao = models.TextField()  # Descrição detalhada da tarefa
    setor = models.CharField(max_length=100)  # Indica o setor responsável pela tarefa (até 100 caracteres)
    prioridade = models.CharField(  # Define a prioridade da tarefa, escolhida entre as opções definidas
        max_length=10, 
        choices=PRIORITY_CHOICES
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)  # Define automaticamente a data/hora de criação da tarefa
    status = models.CharField(  # Define o status da tarefa, com valor padrão "pendente"
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pendente'
    )

    def __str__(self):
        # Retorna a descrição da tarefa junto com o nome do usuário associado
        return f"{self.descricao} - {self.usuario.username}"
