# API FILMES 🎬 

Uma API REST de cadastro de filmes desenvolvida com **FastAPI**, utilizando **SQLAlchemy** para persistência de dados em **SQLite**.

Este projeto faz parte de um desafio técnico com o objetivo de implementar um CRUD completo de filmes, expondo uma API REST funcional e bem estruturada.

---

## 🚀 Tecnologias usadas nesse projeto

- [Guia sobre ORMs em Python – Real Python](https://realpython.com/python-sql-libraries/#object-relational-mappers-orms)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Docker](https://www.docker.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)




---

## 🗂️ Funcionalidades

- ✅ Criar um novo filme (`POST /filmes/`)
- ✅ Listar todos os filmes cadastrados (`GET /filmes/`)
- ✅ Buscar um filme por ID (`GET /filmes/{id}`)
- ✅ Atualizar um filme (`PUT /filmes/{id}`)
- ✅ Deletar um filme (`DELETE /filmes/{id}`)

---

## 📦 Estrutura de diretórios
movies-api/
├── app/
│ ├── api/ # Arquivos de rota (endpoints)
│ ├── crud/ # Funções de acesso ao banco
│ ├── db/ # Conexão e base do SQLAlchemy
│ ├── models/ # Modelos do banco (ORM)
│ ├── schemas/ # Schemas Pydantic
│ └── main.py # Ponto de entrada da aplicação
├── movies.db # Arquivo SQLite com os dados
├── requirements.txt # Dependências do projeto
├── Dockerfile # Containerização
└── README.md # Este arquivo
    
