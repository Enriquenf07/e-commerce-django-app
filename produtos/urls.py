from django.urls import path 
from . import views

urlpatterns = [
    path('<int:pk>', views.ProdutoDetailView.as_view(), name='detailproduto')
]
