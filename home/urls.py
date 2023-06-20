from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("produtos", views.ProdutosView.as_view(), name="produtos")
] 