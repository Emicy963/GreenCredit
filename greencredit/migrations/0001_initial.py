# Generated by Django 5.1.5 on 2025-02-19 16:03

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('FRUTA', 'Fruta'), ('LEGUME', 'Legume'), ('VERDURA', 'Verdura')], max_length=10)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unidade_medida', models.CharField(max_length=20)),
                ('disponivel', models.BooleanField(default=True)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bi', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
                ('score_credito', models.IntegerField(default=0)),
                ('limite_credito', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_solicitado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_aprovado', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente de Aprovação'), ('APROVADO', 'Aprovado'), ('REJEITADO', 'Rejeitado'), ('QUITADO', 'Quitado')], default='PENDENTE', max_length=10)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('data_aprovacao', models.DateTimeField(blank=True, null=True)),
                ('prazo_pagamento', models.IntegerField()),
                ('taxa_juros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditos', to='greencredit.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greencredit.cliente')),
                ('credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greencredit.credito')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_pagamento', models.DateTimeField(auto_now_add=True)),
                ('forma_pagamento', models.CharField(choices=[('VISTA', 'Vista'), ('CARTAO', 'Cartão Multicaixa')], max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('comprovante', models.FileField(blank=True, null=True, upload_to='comprovantes/')),
                ('credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greencredit.credito')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='greencredit.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greencredit.produto')),
            ],
        ),
    ]
