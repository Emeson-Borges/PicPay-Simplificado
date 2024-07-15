# PicPay Backend

Este repositório contém a resolução do desafio backend para o PicPay, desenvolvido com Python e Django. O projeto também utiliza o django_q para gerenciamento de tarefas e notificações.

## Sumário

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

O objetivo deste projeto é desenvolver uma aplicação backend capaz de gerenciar transações e notificações de forma eficiente. A aplicação foi construída com o framework Django e utiliza django_q para a execução e agendamento de tarefas em segundo plano, proporcionando um sistema de notificações robusto.

## Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Django 3.x](https://www.djangoproject.com/)
- [django_q](https://django-q.readthedocs.io/en/latest/)
- [SQLite](https://www.sqlite.org/index.html) (para desenvolvimento e testes, recomendável uso de PostgreSQL em produção)
- [Docker](https://www.docker.com/) (opcional para ambiente isolado)

## Instalação

### Requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)
- Docker (opcional)

### Passos para Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/picpay-backend-challenge.git
    cd picpay-backend-challenge
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados (SQLite por padrão):
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

### Usando Docker (Opcional)

1. Construa a imagem Docker:
    ```bash
    docker build -t picpay-backend-challenge .
    ```

2. Inicie os contêineres:
    ```bash
    docker-compose up -d
    ```

## Configuração

### Configuração do django_q

1. Adicione as configurações do django_q no `settings.py`:
    ```python
    Q_CLUSTER = {
        'name': 'DjangoQ',
        'workers': 4,
        'recycle': 500,
        'timeout': 60,
        'queue_limit': 50,
        'bulk': 10,
        'orm': 'default'
    }
    ```

2. Inicie o django_q:
    ```bash
    python manage.py qcluster
    ```

## Uso

### Rotas Principais

- `POST /api/transactions/` - Cria uma nova transação
- `GET /api/transactions/` - Lista todas as transações
- `GET /api/transactions/<id>/` - Detalha uma transação específica

### Notificações

As notificações são gerenciadas pelo django_q e são enviadas de acordo com a lógica definida nas tarefas em segundo plano.

## Estrutura do Projeto
picpay-backend-challenge/
├── app/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── tasks.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── picpay_backend_challenge/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md


## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commite suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
