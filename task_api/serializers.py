from rest_framework import serializers 
from .models import User, Task 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Especifica que o serializer corresponde ao modelo User
        fields = ['id', 'username', 'email']  # Define os campos que serão incluídos na serialização
        # Este serializer transforma os dados do modelo User em um formato adequado (como JSON) e vice-versa.

class TaskSerializer(serializers.ModelSerializer):
    username = serializers.CharField(  # Campo adicional que exibe o nome de usuário associado à tarefa
        source='usuario.username',  # Mapeia o nome de usuário a partir do campo `usuario` no modelo Task
        read_only=True  # Torna o campo somente leitura, para que não possa ser modificado via API
    )

    class Meta:
        model = Task  
        fields = '__all__' 
        # Este serializer suporta a serialização/deserialização completa do modelo Task,
        # incluindo os campos automáticos, relacionais e o campo adicional `username`.
