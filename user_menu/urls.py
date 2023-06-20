from django.urls import path
from . import views

urlpatterns = [
    path('carrinho', views.CarrinhoView.as_view(), name = 'carrinho'),
    path('gdw@uhuahwi#aidsuohwuoahWEDiodhfuia', views.ConcluidoView.as_view(), name='concluido')
]
