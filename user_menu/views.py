from django.shortcuts import render
from django.views.generic.base import TemplateView
from modelos.models import Carrinho_item
from produtos.models import Produto

class CarrinhoView(TemplateView):
    template_name = 'user_menu/carrinho.html'
    
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        carrinho = Carrinho_item.objects.filter(usuario=current_user.id)
        produtos = []

        for item in carrinho:
            produto_id = item.produto
            produtos.append(produto_id)

        context["produtos"] = produtos
        return context