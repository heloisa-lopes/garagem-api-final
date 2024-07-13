from django.db import models

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} - {self.id}"