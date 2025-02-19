from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto, Credito, Compra
from .forms import ProdutoForm, CreditoForm, CompraForm, ItemCompraForm, ItemCompraFormSet

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def aprovar_credito(request, pk):
    credito = get_object_or_404(Credito, pk=pk)
    if request.method == 'POST':
        credito.status = 'APROVADO' if 'aprovar' in request.POST else 'REJEITADO'
        credito.save()
        return redirect('credito_detail.html', pk)
    return render(request, 'credito_approval.html', {'credito': credito})

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
    form_class = CreditoForm
    template_name = 'credito_form.html'

    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)

class CreditoDetailView(DetailView):
    model = Credito
    template_name = 'credito_detail.html'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['item_formset'] = ItemCompraFormSet(self.request.POST)
        else:
            context['item_formset'] = ItemCompraFormSet()
        
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        form.instance.cliente = self.request.user.cliente
        self.object = form.save()
        item_formset = context['item_formset']
        if item_formset.is_valid():
            item_formset.instance = self.object
            item_formset.save()
        return super().form_valid(form)

class CompraListView(ListView):
    model = Compra
    template_name = 'compra_list.html'

    def get_queryset(self):
        return Compra.objects.filter(cliente__usuario=self.request.user)
    
class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compra_detail.html'
