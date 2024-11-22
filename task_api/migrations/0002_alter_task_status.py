# Generated by Django 5.1 on 2024-11-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('fazendo', 'Fazendo'), ('concluido', 'Concluído')], default='pendente', max_length=10),
        ),
    ]
