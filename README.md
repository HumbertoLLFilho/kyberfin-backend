# KyberFin - Gerenciador Financeiro Pessoal API

## Visão Geral

KyberFin é uma API RESTful minimalista para gerenciamento financeiro pessoal, desenvolvida com Flask e arquitetura limpa, pensada para escalabilidade e segurança.  
Projetada para uso pessoal, com potencial de crescimento e integração contínua (CI/CD).

---

## Tecnologias

- Python 3.11+  
- Flask  
- Pydantic (validação e modelagem de dados)  
- PostgreSQL (banco de dados)  
- psycopg2 (driver PostgreSQL)  
- JWT para autenticação e segurança  
- Passlib (hashing de senha com bcrypt)  
- Docker (opcional para desenvolvimento e deploy)

---

## Padrão de Resposta da API

Todas as respostas JSON seguem o padrão:

```json
{
  "data": {...} | null,
  "errors": [...] | null
}
```

- Em sucesso: `data` contém o payload, `errors` é `null`.  
- Em erro: `errors` contém lista de objetos `{ "code": "...", "message": "..." }`, `data` é `null`.

---

## Rodando o Projeto

### Pré-requisitos

- Python 3.11+  
- PostgreSQL rodando e configurado  
- Variáveis de ambiente configuradas (ex: JWT_SECRET, DATABASE_URL)

### Passos

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure variáveis de ambiente:

- Copie `.env.example` para `.env` e ajuste conforme seu ambiente local, especialmente o `DATABASE_URL` e `JWT_SECRET_KEY`.

3. Crie o banco PostgreSQL e rode a aplicação:

```bash
python migrations/main.py
python src/main.py
```
---

## Testes

```bash
pytest
```

---

## Contato

Desenvolvido por Humberto Lisboa – kyberfin@kyberfin.com

---

Fique à vontade para abrir issues e pull requests!  
Este projeto está em contínuo desenvolvimento para ser sua ferramenta financeira pessoal ideal.

---
