from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.conf import settings

class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bi = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    score_credito = models.IntegerField(default=0)
    limite_credito = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Produto(models.Model):
    CATEGORIAS = [
        ('FRUTA', 'Fruta'),
        ('LEGUME', 'Legume'),
        ('VERDURA', 'Verdura'),
    ]
    
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    unidade_medida = models.CharField(max_length=20)  # kg, unidade, maço, etc
    disponivel = models.BooleanField(default=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Credito(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente de Aprovação'),
        ('APROVADO', 'Aprovado'),
        ('REJEITADO', 'Rejeitado'),
        ('QUITADO', 'Quitado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="creditos")
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_aprovado = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDENTE')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    prazo_pagamento = models.IntegerField()  # em dias
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"Crédito {self.id} - {self.cliente}"

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Compra {self.id} - {self.cliente}"

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=6, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

class Pagamento(models.Model):
    FORMA_PAGAMENTO = [
        ('VISTA', 'Vista'),
        ('CARTAO', 'Cartão Multicaixa'),
    ]
    
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO)
    status = models.CharField(max_length=20)
    comprovante = models.FileField(upload_to='comprovantes/', null=True, blank=True)
    
    def __str__(self):
        return f"Pagamento {self.id} - {self.credito}"
