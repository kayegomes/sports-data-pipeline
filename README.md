# ⚽ Sports Data Pipeline — Engenharia de Dados Moderna

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![dbt](https://img.shields.io/badge/dbt-1.8-orange)](https://getdbt.com)
[![BigQuery](https://img.shields.io/badge/BigQuery-Data%20Warehouse-blue)](https://cloud.google.com/bigquery)
[![Looker Studio](https://img.shields.io/badge/Looker-Studio-4285F4)](https://lookerstudio.google.com)
[![Airflow](https://img.shields.io/badge/Airflow-Orchestration-green)](https://airflow.apache.org) *(em breve)*
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 **Sobre o Projeto**

Este repositório contém um **pipeline de dados end‑to‑end** que extrai informações de partidas de futebol de uma API pública, processa‑as seguindo a **arquitetura Medallion (Bronze, Silver, Gold)** e disponibiliza os dados para consumo analítico em ferramentas de BI.

O projeto foi desenvolvido para demonstrar habilidades práticas em **Engenharia de Dados**, incluindo:

- Coleta e ingestão de dados (Python + requests)
- Modelagem dimensional e transformação com **dbt** + **BigQuery**
- Criação de dashboards interativos com **Looker Studio**
- Versionamento de código e CI/CD com **GitHub Actions**
- (Em andamento) Orquestração com **Apache Airflow**

---

## 🏗️ **Arquitetura do Pipeline**
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ EXTRACT │ ──▶ │ BRONZE │ ──▶ │ SILVER │ ──▶ │ GOLD │
│ (API / CSV) │ │ (raw.matches) │ │ (stg_matches) │ │ (dim / fact) │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
│ │ │
▼ ▼ ▼
Dados brutos Limpeza e tipagem Modelos de negócio
(ingestão) (padronização) (dimensões, fatos,
agregações)

- **Camada Bronze** – Tabela `raw.matches` no BigQuery (dados exatamente como ingeridos).
- **Camada Silver** – Views no dbt que limpam, renomeiam e tipam os dados (`stg_matches`).
- **Camada Gold** – Tabelas físicas (dimensões, fatos e agregações) otimizadas para consumo analítico:
  - `dim_teams` (dimensão de times)
  - `fact_matches` (fato de partidas com chaves estrangeiras)
  - `league_table` (classificação do campeonato)
  - `team_stats` (estatísticas detalhadas por time)

---

## 🛠️ **Tecnologias & Ferramentas**

| Categoria              | Tecnologias                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Linguagem**          | Python 3.10+ (pandas, requests)                                            |
| **Data Warehouse**     | Google BigQuery                                                             |
| **Transformação**      | dbt Core (dbt-bigquery)                                                     |
| **Orquestração**       | Apache Airflow *(em implementação)*                                         |
| **Visualização**       | Google Looker Studio (ex‑Data Studio)                                       |
| **CI/CD**              | GitHub Actions                                                              |
| **Contêineres**        | Docker                                                                      |
| **Controle de Versão** | Git                                                                         |

---

## 📂 **Estrutura do Repositório**
├── .github/workflows/ # CI/CD: testes automáticos e build Docker
├── data/ # Dados brutos e processados (ignorados pelo Git)
├── pipelines/ # Scripts legados de execução (ETL)
├── sql/ # Consultas auxiliares
├── src/
│ ├── extract/ # Extração de dados da API
│ ├── load/ # Carga inicial para o BigQuery
│ ├── quality/ # Validações de qualidade (pandas)
│ └── utils/ # Funções auxiliares
├── dbt_project/ # Projeto dbt com arquitetura Medallion
│ └── meu_projeto_dbt/
│ ├── models/
│ │ ├── bronze/ # Fonte raw (sources.yml)
│ │ ├── silver/ # Modelos de staging (stg_matches)
│ │ └── gold/ # Dimensões, fatos e métricas
│ ├── dbt_project.yml
│ └── ...
├── .gitignore
├── README.md # Você está aqui!
├── requirements.txt
└── dockerfile

---

## 🔄 **Fluxo de Trabalho**

### 1️⃣ **Extração e Carga (EL)**
- O script `src/load/load_raw.py` lê o arquivo `data/processed/matches_clean.csv` e o carrega na tabela `raw.matches` do BigQuery.
- Futuramente, a extração será feita diretamente de uma API e orquestrada pelo Airflow.

### 2️⃣ **Transformação com dbt (T)**
- O dbt executa os modelos SQL na ordem correta (respeitando as dependências via `ref`).
- Os modelos são materializados conforme a camada:
  - **Bronze / Silver** → views (leves e sempre atualizadas)
  - **Gold** → tabelas (físicas, particionáveis e otimizadas para consultas)

### 3️⃣ **Testes e Documentação**
- Testes de qualidade (not null, unique, relationships) são definidos em arquivos `schema.yml`.
- A documentação é gerada automaticamente com `dbt docs generate`.

### 4️⃣ **Visualização**
- O Looker Studio conecta‑se diretamente às tabelas `gold` para criar dashboards interativos.
- Exemplo: [link para o dashboard](#) *(a ser inserido)*

---

## 🚀 **Como Executar Localmente**

### Pré‑requisitos
- Python 3.10+ e Git
- Conta no Google Cloud com BigQuery ativado
- Google Cloud SDK instalado e autenticado (`gcloud auth application-default login`)
- dbt Core (`pip install dbt-bigquery`)

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/kayegomes/sports-data-pipeline.git
cd sports-data-pipeline

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
.\venv\Scripts\activate          # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o perfil do dbt (em ~/.dbt/profiles.yml) com seus dados
# Exemplo:
# meu_projeto_dbt:
#   target: dev
#   outputs:
#     dev:
#       type: bigquery
#       method: oauth
#       project: seu-projeto-id
#       dataset: dbt_dev
#       threads: 4
#       location: southamerica-east1

# Carregue os dados brutos para o BigQuery
python src/load/load_raw.py

# Execute as transformações com dbt
cd dbt_project/meu_projeto_dbt
dbt run
dbt test              # (opcional)

📊 Dashboard Interativo
O Looker Studio consome as tabelas gold e apresenta:

Tabela de classificação (pontos, vitórias, derrotas, saldo de gols)

Gráfico comparativo de gols pró e sofridos por time

Scorecards com totais do campeonato

Filtros interativos por time

🔗 Acesse o dashboard aqui (coloque o link real)

🧠 Habilidades Demonstradas
Modelagem de dados dimensional (star schema) e arquitetura Medallion

ELT moderno com dbt + BigQuery

Automação de testes de qualidade no pipeline

Versionamento de código e boas práticas de Git

CI/CD com GitHub Actions (validação e build)

Containerização com Docker

Orquestração de pipelines (Airflow em breve)

Visualização de dados para stakeholders de negócio

🎯 Próximos Passos
Integrar orquestração com Apache Airflow (agendamento, tratamento de falhas)

Substituir a carga manual por extração automatizada da API

Adicionar testes unitários e de integração

Implementar partições e clustering nas tabelas gold para performance


# Author

Lincoln Gomes  

Data & Automation | Python | Data Pipelines | Analytics Engineering  

LinkedIn  
https://www.linkedin.com/in/lincoln-kaye-gomes-b89a44184
