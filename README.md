```markdown
<div align="center">

# 🔗 Short URL API

**Encurtador de Links profissional com FastAPI, SQLite e Docker**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)

</div>

---

## 📌 Sobre o Projeto

Uma API REST que transforma URLs longas em links curtos e rastreáveis. Construída com **FastAPI** para alta performance, **SQLAlchemy** para persistência em banco de dados SQLite e **Docker** para facilitar a execução em qualquer ambiente.

## 🛠️ Tecnologias

- **Python 3.12** + **FastAPI**
- **SQLAlchemy** (ORM para SQLite)
- **Docker** & **Docker Compose**
- **Pytest** (Testes automatizados)
- **GitHub Actions** (CI/CD)

## ⚙️ Como Executar

A forma mais fácil de rodar o projeto é usando Docker:

```bash
docker compose up --build
```

A API estará disponível em `http://localhost:8000`. 

### 📖 Documentação Interativa (Swagger)
Após subir o container, acesse:
👉 **http://localhost:8000/docs**

## 🧪 Como rodar os testes

```bash
# Certifique-se de estar no ambiente virtual
source .venv/bin/activate
pytest
```

## 📂 Estrutura do Projeto

```text
short-url-api/
├── app/
│   ├── models/       # Modelos do banco de dados (SQLAlchemy)
│   ├── routers/      # Endpoints da API (FastAPI)
│   ├── services/     # Regras de negócio (geração de código)
│   ├── database.py   # Conexão com o banco
│   └── main.py       # Ponto de entrada da aplicação
├── tests/            # Testes automatizados (Pytest)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
```