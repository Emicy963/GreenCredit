from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto, Credito
from .forms import ProdutoForm, CreditoForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = '/produtos/'

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = '/produtos/'

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = '/produtos/'
    template_name = 'produto_confirm_delete.html'
 
class CreditoListView(ListView):
    model = Credito
    template_name = 'credito_list.html'

    def get_queryset(self):
        return Credito.objects.filter(cliente__usuario=self.request.user)
    
class CreditoCreateView(CreateView):
    model = Credito
    form_class = ProdutoForm
    template_name = 'credito_form.html'

    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)
