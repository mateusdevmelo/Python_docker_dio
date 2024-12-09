# Projeto Flask com MySQL e NGINX

Este projeto é uma aplicação simples construída em Python utilizando Flask como framework web, MySQL como banco de dados e NGINX como proxy reverso para balanceamento de carga. A aplicação permite registrar entradas aleatórias no banco de dados e exibir informações básicas.

## Diagrama da Aplicação

```mermaid
graph TD
    User[Usuário] -->|Requisição HTTP| NGINX[NGINX Proxy]
    NGINX -->|Proxy Pass| Flask[Aplicação Flask]
    Flask -->|Grava/Consulta| MySQL[Banco de Dados MySQL]
    Flask -->|Resposta HTTP| User
