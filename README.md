# Ravera Backend

Base inicial em Python para a API da Ravera, uma loja de peças autorais e
personalizadas. O projeto é separado do frontend React, TypeScript e Vite.

Esta etapa contém FastAPI, configuração por ambiente, sessões SQLAlchemy 2 para
PostgreSQL e o ambiente do Alembic. A única rota implementada é
`GET /api/v1/health`, que retorna `{"status":"ok"}` com HTTP 200.

## Requisitos

- Python 3.11 ou superior; Python 3.12 é uma opção para desenvolvimento local.
- pip, instalado normalmente junto com o Python.
- PostgreSQL somente quando houver uso de persistência ou migrations online.

As versões das dependências diretas estão fixadas em `pyproject.toml`.
O driver `psycopg[binary]` inclui os componentes binários necessários para o
acesso ao PostgreSQL, facilitando a instalação local.

## Instalação

Execute os comandos na raiz deste backend.

No Windows, com PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e .
Copy-Item .env.example .env
```

Esses comandos usam o Python do ambiente virtual diretamente e não exigem
alterar a política de execução do PowerShell. Se o comando `python` não estiver
disponível, use `py -3.12` para criar o ambiente, com Python 3.12 instalado.
Copie `.env.example` somente se ainda não houver um `.env` local.

No Linux ou macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -e .
cp -n .env.example .env
```

## Configuração

O Pydantic Settings lê `.env` a partir do diretório atual. Variáveis do ambiente
do processo têm prioridade sobre esse arquivo. Os mesmos valores de exemplo
existem como padrões, permitindo iniciar a API sem criar `.env`.

| Variável | Padrão | Finalidade |
| --- | --- | --- |
| `APP_NAME` | `Ravera API` | Nome exibido na documentação da API. |
| `DEBUG` | `false` | Modo de depuração do FastAPI; mantenha `false` em produção. |
| `DATABASE_URL` | URL fictícia de `.env.example` | Configuração PostgreSQL utilizada pelo SQLAlchemy e Alembic. |

Quando um banco estiver disponível, ajuste `DATABASE_URL` no seu `.env`:

```dotenv
DATABASE_URL=postgresql+psycopg://ravera:senha_ficticia@localhost:5432/ravera
```

Use o prefixo `postgresql+psycopg://`. Caracteres especiais no usuário ou senha
devem ser codificados para uso em URL. As credenciais de exemplo são fictícias;
substitua-as pelas credenciais do seu ambiente quando configurar persistência.
O banco e o usuário precisarão existir previamente.

O `.env` está no `.gitignore`. Reinicie o servidor ao mudar as configurações,
pois elas são carregadas e armazenadas em memória durante a execução.

## Inicialização

No Windows:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

No Linux ou macOS:

```bash
.venv/bin/python -m uvicorn app.main:app --reload
```

O servidor inicia em `http://127.0.0.1:8000`. A opção `--reload` é destinada ao
desenvolvimento local. Para encerrar, use `Ctrl+C`.

- Health check: [GET /api/v1/health](http://127.0.0.1:8000/api/v1/health).
- Documentação interativa: [Swagger UI](http://127.0.0.1:8000/docs).
- Documentação alternativa: [ReDoc](http://127.0.0.1:8000/redoc).
- Especificação: [OpenAPI](http://127.0.0.1:8000/openapi.json).

## Verificação manual

Com o servidor em execução, abra outro terminal e execute:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/v1/health
```

Ou, com curl:

```bash
curl -i http://127.0.0.1:8000/api/v1/health
```

A resposta deve ter HTTP 200 e o corpo:

```json
{"status":"ok"}
```

Este endpoint verifica apenas se a API está respondendo. Ele não consulta o
banco. A inicialização não abre conexão nem cria tabelas, então funciona mesmo
sem PostgreSQL disponível, desde que as dependências estejam instaladas e a
configuração contenha uma URL PostgreSQL válida.

## Alembic

O Alembic já está configurado, mas `alembic/versions/` ainda não contém migrations.
Não execute `alembic init` novamente. Para listar o histórico, sem acessar o banco:

```powershell
.\.venv\Scripts\python.exe -m alembic history
```

Também é possível verificar o ambiente em modo offline:

```powershell
.\.venv\Scripts\python.exe -m alembic upgrade head --sql
```

O histórico está vazio nesta etapa; o modo offline não aplica mudanças ao banco.
Quando modelos e migrations forem desenvolvidos, os comandos serão:

```powershell
.\.venv\Scripts\python.exe -m alembic revision --autogenerate -m "descricao_da_alteracao"
.\.venv\Scripts\python.exe -m alembic upgrade head
```

Esses dois comandos exigem um PostgreSQL acessível e configurado. Os futuros
modelos deverão herdar de `app.db.base.Base` e ser importados em
`app/models/__init__.py` para registrar suas tabelas no metadata. Revise toda
migration gerada antes de aplicá-la. No Linux ou macOS, use `.venv/bin/python`
no lugar de `.\.venv\Scripts\python.exe`.

## Estrutura e escopo

A responsabilidade de cada pasta está descrita em
[docs/architecture.md](docs/architecture.md).

As pastas `models`, `schemas`, `services`, `integrations` e `tests` estão
preparadas para as próximas etapas. Ainda não há modelos de produtos ou
usuários, CRUD, autenticação, permissões, MFA, upload de fotos, integração com
Supabase, dados iniciais ou funcionalidades de frontend.
