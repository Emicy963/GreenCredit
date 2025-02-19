from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Produtos
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/editar/<int:id>/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/exluir/<int:id>/', views.ProdutoDeleteView.as_view(), name='produto_delete'),

]
