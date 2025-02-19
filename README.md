# Crédito Verde

Bem-vindo ao repositório do **Crédito Verde**, uma plataforma que conecta você a alimentos saudáveis e acessíveis, com crédito facilitado para uma vida melhor.

## Sobre o Projeto

O Crédito Verde é uma aplicação web desenvolvida em Django que permite:

- Visualizar produtos saudáveis.
- Solicitar crédito para compras.
- Gerenciar compras e pagamentos.

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Banco de Dados:** SQLite (desenvolvimento), PostgreSQL (produção)

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- Pipenv (ou pip)

### Passos para Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/credito-verde.git
cd credito-verde
```

2. Crie um Ambiente Virtual e ativo:

```bash
python -m venv venv
venv/Scripts/activate # Windows
source venv/bin/activate # Para Linux/
```

3. Instale os requisitos:

```bash
pip install -r requirements.txt
```

4. Execute as migrações:

```bash
python manage.py migrate
```

5. Crie um usuário (caso necessário):

```bash
python manage.py creatsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse o projeto em:

<http://localhost:800>

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature.

```bash
git checkout -b feature/minha-feature
```

3. Commit suas mudanças.

```bash
git commit -m 'Adiciona nova feature'
```

4. Faça push para a branch.

```bash
git push origin minha-feature
```

5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Email: [andersonpaulo931@gmail.com](andersonpaulo931@gmail.com)
