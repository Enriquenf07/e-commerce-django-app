from django.contrib import admin
from .models import Pedido, Pedido_item, Carrinho_item
# Register your models here.

admin.site.register(Pedido)
admin.site.register(Pedido_item)
admin.site.register(Carrinho_item)