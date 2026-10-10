# Arquitetura inicial

O backend é um projeto independente do frontend React, TypeScript e Vite.
Nesta etapa, oferece apenas a aplicação FastAPI e o health check.

| Pasta | Responsabilidade |
| --- | --- |
| `app/` | Código da aplicação; `main.py` cria a API e registra suas rotas. |
| `app/api/` | Camada HTTP e dependências compartilhadas, como a sessão de banco por requisição. |
| `app/api/v1/` | Router que reúne a primeira versão da API, publicada em `/api/v1`. |
| `app/api/v1/routes/` | Endpoints HTTP; inicialmente contém apenas `/health`. |
| `app/core/` | Configurações carregadas de variáveis de ambiente e do arquivo `.env`. |
| `app/db/` | Base declarativa, engine e fábrica de sessões SQLAlchemy. |
| `app/models/` | Reservada para futuros modelos de persistência. |
| `app/schemas/` | Reservada para futuros schemas Pydantic de entrada e saída. |
| `app/services/` | Reservada para futuras regras de negócio. |
| `app/integrations/` | Reservada para futuros acessos a serviços externos. |
| `alembic/` | Ambiente e template de migrations, usando `Base.metadata` e `DATABASE_URL`. |
| `alembic/versions/` | Reservada para futuras migrations versionadas; atualmente vazia. |
| `tests/` | Reservada para futuros testes automatizados. |
| `docs/` | Documentação técnica do projeto. |

O health check não depende da sessão SQLAlchemy. Criar a engine ou uma sessão
não abre uma conexão: ela é necessária quando uma operação de persistência
for executada. Não há criação automática de tabelas na inicialização.

As sessões são síncronas e usam o driver psycopg 3 para PostgreSQL. A dependência
`get_db` fecha a sessão ao final da requisição; commits ficam sob responsabilidade
da funcionalidade que vier a usar essa sessão.

Quando modelos forem adicionados, deverão herdar de `Base` e ser importados em
`app/models/__init__.py` para que o Alembic reconheça suas tabelas.
