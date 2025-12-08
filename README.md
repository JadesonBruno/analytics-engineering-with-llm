# 🤖 Analytics Engineering with LLM

> **Demonstração prática de Analytics Engineering usando Python, SQL e LLM para Extração de Insights em Pipelines de Engenharia de Dados**

Este projeto demonstra como implementar uma pipeline de **analytics engineering** que combina bancos de dados PostgreSQL, processamento de dados com Python e geração de insights automatizados usando **Large Language Models (LLMs)**. Utilizamos o **Ollama** com o modelo **Llama3** para análise inteligente de padrões de compras de clientes.

## 🎯 Objetivo

Implementar uma solução completa de analytics engineering usando:
- **PostgreSQL** como banco de dados relacional
- **Python** para ETL e orquestração de pipelines
- **SQLAlchemy** e **psycopg2** para conexão com banco de dados
- **LangChain** + **Ollama (Llama3)** para geração de insights com IA
- **Docker** para ambiente de desenvolvimento isolado e reproduzível
- **Pre-commit** para qualidade de código (Black, Flake8, isort, Bandit)

## 🏗️ Arquitetura da Solução

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   CSV Files     │────▶│   PostgreSQL    │────▶│  Python Query   │────▶│   Ollama LLM    │
│  (Raw Data)     │     │   (Database)    │     │  (Analytics)    │     │   (Insights)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
   data/raw/                 :5433              src/3_query.py         src/4_llm.py
                                                                              │
                                                                              ▼
                                                                    ┌─────────────────┐
                                                                    │   CSV Output    │
                                                                    │   (Insights)    │
                                                                    └─────────────────┘
                                                                    data/outputs/
```

## 📁 Estrutura do Projeto

```
analytics-engineering-with-llm/
├── 📄 README.md                    # Documentação do projeto
├── 🐳 dockerfile                   # Imagem Docker PostgreSQL
├── 🐳 docker-compose.yml           # Orquestração do ambiente
├── 📦 pyproject.toml               # Dependências e configuração do projeto
├── 🔧 .pre-commit-config.yaml      # Configuração de hooks de qualidade
├── 🐍 .python-version              # Versão do Python (3.12.9)
├── 📝 LICENSE                      # Licença MIT
├── 🐙 .gitignore                   # Arquivos e pastas ignorados pelo Git
├── 🔒 .env                         # Variáveis de ambiente (não versionado)
├── 🗂️ src/
│   ├── 🐍 main.py                  # Pipeline principal (orquestrador)
│   ├── 🐍 1_create_db.py           # Criação do schema e tabelas
│   ├── 🐍 2_load_db.py             # Carga de dados CSV para PostgreSQL
│   ├── 🐍 3_query.py               # Execução de queries SQL
│   └── 🐍 4_llm.py                 # Geração de insights com LLM
├── 🗂️ sql/
│   ├── 📋 script.sql               # Script de criação do schema e tabelas
│   └── 📋 query.sql                # Query de análise de compras
└── 🗂️ data/
    ├── 📂 raw/                     # Dados brutos (CSV)
    │   ├── 📊 customers.csv        # Dados de clientes
    │   ├── 📊 products.csv         # Dados de produtos
    │   └── 📊 purchases.csv        # Dados de compras
    └── 📂 outputs/                 # Dados processados
        └── 📊 insights.csv         # Insights gerados pelo LLM
```

## 🛠️ Pré-requisitos

### 📋 Ferramentas Necessárias
- **Python 3.12+**
- **Docker** e **Docker Compose**
- **Poetry** (gerenciador de dependências)
- **Ollama** com modelo **Llama3** instalado
- **DBeaver** ou outro cliente SQL (opcional)

### 🔑 Configuração de Credenciais

Criar um arquivo `.env` na raiz do projeto:

```bash
# PostgreSQL credentials
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_segura
POSTGRES_DB=postgres
```

## 🚀 Roadmap

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/JadesonBruno/analytics-engineering-with-llm.git
cd analytics-engineering-with-llm
```

### 2️⃣ Configurar o Ambiente Python

```bash
# Instalar dependências com Poetry
poetry install

# Ativar o ambiente virtual
source .venv/Scripts/activate  # Windows
```

### 3️⃣ Configurar o Ambiente Docker

```bash
# Build e start do container PostgreSQL
docker-compose up -d --build
```

### 4️⃣ Instalar o Ollama e o Modelo Llama3

```bash
# Instalar Ollama (Windows/Mac/Linux)
# Acesse: https://ollama.ai/download

# Baixar o modelo Llama3
ollama pull llama3

# Verificar se o modelo está disponível
ollama list
```

### 5️⃣ Executar o Pipeline Completo

```bash
# Executar todos os scripts em sequência
python src/main.py
```

Ou executar cada etapa individualmente:

```bash
# 1. Criar schema e tabelas no PostgreSQL
python src/1_create_db.py

# 2. Carregar dados CSV para o banco
python src/2_load_db.py

# 3. Executar query de análise
python src/3_query.py

# 4. Gerar insights com LLM
python src/4_llm.py
```

### 6️⃣ Verificar os Resultados

Os insights gerados pelo LLM serão salvos em `data/outputs/insights.csv` e exibidos no terminal.

## ⚙️ Configurações Principais

### 🐳 Dockerfile

```dockerfile
# Use the official PostgreSQL image as base
FROM postgres:18

# Image maintainer
LABEL maintainer="jadesonbruno.a@outlook.com"
```

### 🐘 Docker Compose

```yaml
services:
  db_source:
    build:
      context: .
      dockerfile: dockerfile
    ports:
      - "5433:5432"
    env_file:
      - .env
```

### 🔧 Schema do Banco de Dados

```sql
-- Schema: analytics_engineering
CREATE SCHEMA analytics_engineering;

-- Tabelas: customers, products, purchases
CREATE TABLE analytics_engineering.customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(101),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics_engineering.products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE analytics_engineering.purchases (
    purchase_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES analytics_engineering.customers(customer_id),
    product_id INTEGER REFERENCES analytics_engineering.products(product_id),
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 🤖 Configuração do LLM

O projeto utiliza **LangChain** com **Ollama** para executar o modelo **Llama3** localmente:

```python
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Instanciar o LLM
llm = OllamaLLM(model="llama3")

# Criar o prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um analista de dados especializado..."),
    ("user", "question: {question}")
])

# Criar a chain de execução
chain = prompt | llm | StrOutputParser()
```

## 🔐 Qualidade de Código

O projeto utiliza **pre-commit** com os seguintes hooks:

| Hook | Descrição |
|------|-----------|
| **Black** | Formatação automática de código |
| **Flake8** | Linting e verificação de estilo |
| **isort** | Ordenação de imports |
| **Bandit** | Análise de segurança |
| **trailing-whitespace** | Remove espaços em branco |
| **end-of-file-fixer** | Garante nova linha no final |

```bash
# Instalar hooks
pre-commit install

# Executar em todos os arquivos
pre-commit run --all-files
```

## 🐛 Troubleshooting

### ❌ Erro de Conexão com PostgreSQL
```
connection to server at "localhost" (127.0.0.1), port 5433 failed
```
**Solução:** Verifique se o container Docker está rodando:
```bash
docker-compose ps
docker-compose up -d
```

### ❌ Módulo psycopg2 Não Encontrado
```
ModuleNotFoundError: No module named 'psycopg2'
```
**Solução:** Instale as dependências com Poetry:
```bash
poetry install
poetry shell
```

### ❌ Ollama Não Conecta
```
Connection refused: localhost:11434
```
**Solução:** Verifique se o Ollama está rodando:
```bash
ollama serve
ollama list
```

### ❌ Modelo Llama3 Não Encontrado
```
model "llama3" not found
```
**Solução:** Baixe o modelo:
```bash
ollama pull llama3
```

## 📚 Recursos e Referências

- [📖 LangChain Documentation](https://python.langchain.com/docs/)
- [🦙 Ollama Documentation](https://ollama.ai/)
- [🐘 PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [🐳 Docker Documentation](https://docs.docker.com/)
- [📦 Poetry Documentation](https://python-poetry.org/docs/)

## 🔄 Próximos Passos e Melhorias

- [ ] **📊 Dashboard**: Visualização dos insights com Streamlit
- [ ] **🧪 Testes**: Testes unitários e de integração com pytest
- [ ] **📈 Métricas**: Logging e monitoramento de execução
- [ ] **🔄 Scheduling**: Agendamento de execução com Airflow ou Prefect
- [ ] **☁️ Cloud**: Deploy em ambiente cloud (AWS/GCP/Azure)
- [ ] **🤖 Modelos**: Suporte a outros LLMs (GPT-4, Claude, Gemini)

## 📞 Suporte e Contato

**Jadeson Bruno**
- 📧 Email: jadesonbruno.a@outlook.com
- 🐙 GitHub: [@JadesonBruno](https://github.com/JadesonBruno)
- 💼 LinkedIn: [Jadeson Bruno](https://www.linkedin.com/in/jadeson-silva/)

---

⭐ **Se este projeto foi útil, deixe uma estrela no repositório!**

📝 **Licença**: MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
