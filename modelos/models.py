from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from produtos.models import Produto

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f'{self.id}'
    
class Pedido_item(models.Model):
    pedido = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
    
class Carrinho_item(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario}'