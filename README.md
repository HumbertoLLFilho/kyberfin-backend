# KyberFin

KyberFin é um gerenciador financeiro pessoal minimalista e moderno, construído com Flask, SQLAlchemy e Pydantic.  
Inspirado na vibe futurista e geek, ele nasceu para ser simples, seguro e escalável — ideal para quem quer ter controle total sobre suas finanças com tecnologia de ponta.

---

## Tecnologias

- Python 3.9+
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Pydantic
- PostgreSQL
- python-dotenv

---

## Funcionalidades iniciais

- Cadastro e atualização de usuários
- Autenticação segura via JWT
- Estrutura limpa e modular baseada em UseCases
- Preparado para expansão com novas entidades financeiras

---

## Setup Local

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/kyberfin.git
cd kyberfin/src
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure variáveis de ambiente:

- Copie `.env.example` para `.env` e ajuste conforme seu ambiente local, especialmente o `DATABASE_URL` e `JWT_SECRET_KEY`.

5. Crie o banco PostgreSQL e rode a aplicação:

```bash
# No psql ou outra ferramenta, crie o banco
CREATE DATABASE finance_manager;

# Rode o app
python application/main.py
```

---

## Como usar

- Use os endpoints de cadastro `/users/` e login `/auth/login` para iniciar.
- Autentique-se via JWT para acessar rotas protegidas.
- Desenvolva novos módulos seguindo a arquitetura de UseCases.

---

## Próximos passos

- Implementar CRUD para contas, receitas e despesas
- Testes automatizados
- Dockerização e pipeline CI/CD
- Deploy em nuvem (Render, Railway, etc.)
- Documentação automática da API

---

## Contato

Desenvolvido por Humberto Lisboa — mantenha-se em contato!

---

## Licença

Apache-2.0 license
