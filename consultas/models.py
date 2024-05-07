from django.contrib.auth.models import User
from django.db import models

class Procedimento(models.Model):
    nome_procedimento = models.CharField(max_length=50)
    preco = models.IntegerField()

    def __str__(self):
        return self.nome_procedimento

class Consulta(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    data = models.DateField(verbose_name="Data da Consulta")
    horario = models.TimeField(verbose_name="Horário da Consulta")

    def __str__(self):
        return f"Consulta de {self.paciente.username} em {self.data} às {self.horario}"
    def custo_consulta(self):
        return self.procedimento.preco