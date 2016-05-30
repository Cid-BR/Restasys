from django.db import models

class Mesa(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

class Pratos(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    ingredientes = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Pedidos(models.Model):
    mesa_id = models.ForeignKey('Mesa')
    pratos_id = models.ForeignKey('Pratos')
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.mesa_id.numero+" - "+self.pratos_id.nome

class Pedidos_Fechados(models.Model):
    pedidos_id = models.ForeignKey('Pedidos')

    def __str__(self):
        return self.pedidos_id.mesa_id
