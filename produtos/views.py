from django.shortcuts import render
from django.views.generic import DetailView
from .models import Produto
# Create your views here.

class ProdutoDetailView(DetailView):
    template_name = 'produtos/produto.html'
    model = Produto

    def post(self, request):
        current_user = request.user
        
