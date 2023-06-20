from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Produto
from modelos.models import Carrinho_item
# Create your views here.

class ProdutoDetailView(DetailView):
    template_name = 'produtos/produto.html'
    model = Produto

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = request.user
            produto_id =  self.kwargs['pk']
            produto = Produto.objects.get(id=produto_id)
            new_carrinho = Carrinho_item(usuario=current_user, produto=produto)
            new_carrinho.save()
            return redirect("carrinho")
        else:
            return redirect('login')

        
