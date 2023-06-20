from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView

from produtos.models import Produto
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = Produto.objects.all()
        context["produtos"] = produtos
        return context
    
class ProdutosView(TemplateView):
    template_name = 'home/produtos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = Produto.objects.all()
        context["produtos"] = produtos
        return context
        