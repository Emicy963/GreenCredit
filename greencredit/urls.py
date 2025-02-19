from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Produtos
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/editar/<int:pk>/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/excluir/<int:pk>/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    # Créditos
    path('creditos/', views.CreditoListView.as_view(), name='credito_list'),
    path('creditos/novo/', views.CreditoCreateView.as_view(), name='credito_create'),
    path('creditos/<int:pk>', views.CreditoDetailView.as_view(), name='credito_detail'),
]
