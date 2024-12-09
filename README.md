# Projeto Flask com MySQL e NGINX

Este é um exemplo de aplicação simples utilizando Flask como framework web, MySQL como banco de dados e NGINX como proxy reverso. A aplicação foi refatorada a partir de uma versão em PHP para Python.

## Estrutura do Projeto

```plaintext
.
├── banco.sql             # Script para criar a tabela no banco de dados
├── Dockerfile            # Configuração do Docker para a aplicação Flask
├── nginx.conf            # Configuração do NGINX para proxy reverso
├── app/                  # Código-fonte do aplicativo Flask
│   ├── app.py            # Código principal da aplicação em Flask
│   ├── requirements.txt  # Dependências do Python
└── templates/            # Arquivos HTML para renderização
    └── index.html        # Página principal do projeto

graph TD
    A[Usuário] -->|Requisição HTTP| B[NGINX]
    B -->|Proxy Pass| C[Aplicação Flask]
    C -->|Conexão| D[Banco de Dados MySQL]
    C -->|Resposta| A


flowchart LR
    subgraph Frontend
        HTML[HTML Página Principal]
    end
    subgraph Backend
        Flask[Flask App]
        PyMySQL[PyMySQL]
    end
    subgraph Infraestrutura
        NGINX[NGINX Proxy]
        MySQL[MySQL Database]
    end

    HTML --> Flask
    Flask --> PyMySQL
    PyMySQL --> MySQL
    NGINX --> Flask
