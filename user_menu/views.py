from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from modelos.models import Carrinho_item, Pedido_item, Pedido
from produtos.models import Produto
from django.db import transaction
from django.utils import timezone

class CarrinhoView(TemplateView):
    template_name = 'user_menu/carrinho.html'
    
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        carrinho = Carrinho_item.objects.filter(usuario=current_user.id)
        produtos = []

        for item in carrinho:
            produto = item.produto
            produtos.append(produto)

        context["produtos"] = produtos
        return context
    
    def post(self, request, **kwargs):
        produto_id = request.POST['produto_id']
        produto = Carrinho_item.objects.filter(produto=produto_id, usuario=request.user)
        produto = produto[0]
        produto.delete()
        return redirect('carrinho')
    
class ConcluidoView(View):
    def get(self, request):
        current_user = self.request.user
        carrinho = Carrinho_item.objects.filter(usuario=current_user.id)
        new_pedido = Pedido(usuario=current_user, data=timezone.now())
        new_pedido.save()
        for item in carrinho:
            produto = item.produto
            new_pedido_item = Pedido_item(pedido=new_pedido, produto=produto)
            new_pedido_item.save()
            item.delete()

        return render(request=request,  template_name="user_menu/finalizado.html")
            
