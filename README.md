<div align="center">

# 🤖 GenAI Internship Training Program
### From Python Fundamentals to Production-Ready Generative AI Systems

*A complete, hands-on 43-day journey through Python, Data Engineering, Databases, APIs, and Generative AI — documented as a public learning repository.*

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20%26%20Agents-1C3C3C?style=for-the-badge)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude-D97757?style=for-the-badge)](https://www.anthropic.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/your-username/GenAI-Internship-Training-Program?style=flat-square&color=gold)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](#)
[![Made with ❤](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red.svg?style=flat-square)](#)

</div>

---

## 📖 Table of Contents

- [About this Repository](#-about-this-repository)
- [Internship Overview](#-internship-overview)
- [Learning Roadmap](#-learning-roadmap)
- [Repository Structure](#-repository-structure)
- [Module Breakdown](#-module-breakdown)
  - [Module 1 · Python Foundations](#module-1--python-foundations-days-14)
  - [Module 2 · Advanced Python & Logic](#module-2--advanced-python--logic-days-58)
  - [Module 3 · NumPy, Pandas & ML](#module-3--numpy-pandas--ml-days-914)
  - [Module 4 · Data Engineering & ETL](#module-4--data-engineering--etl-days-1519)
  - [Module 5 · Databases: SQL & NoSQL](#module-5--databases-sql--nosql-days-2024)
  - [Module 6 · APIs & FastAPI](#module-6--apis--fastapi-days-2527)
  - [Module 7 · GenAI Foundations & Prompt Engineering](#module-7--genai-foundations--prompt-engineering-days-2832)
  - [Module 8 · RAG Systems](#module-8--rag-systems-days-3337)
  - [Module 9 · Agentic AI & Tools](#module-9--agentic-ai--tools-days-3841)
  - [Module 10 · Closed-Source Models & Capstone](#module-10--closed-source-models--capstone-days-4243)
- [Technologies Used](#-technologies-used)
- [Skills Acquired](#-skills-acquired)
- [Projects](#-projects)
- [Learning Progress](#-learning-progress)
- [How to Use](#-how-to-use)
- [Resources](#-resources)
- [Future Improvements](#-future-improvements)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)

---

## 📌 About this Repository

This repository is my public learning log for a **2-month, 43-working-day Generative AI Internship**. It's not a course dump — it's a working archive of everything I built, broke, and fixed while going from Python basics to shipping RAG pipelines and tool-using agents.

Inside you'll find:

- 📝 **Daily notes** — concepts, gotchas, and "what I learned" write-ups for every working day
- 📂 **Assignments** — the small, focused exercises tied to each day's objective
- 🧪 **Mini projects** — module-closing builds that combine that module's skills
- 🔬 **Practice code & experiments** — scratch work, benchmarks, and "let me just try this" scripts
- 📚 **Resources** — courses, docs, and references that were actually useful
- 🚀 **Final projects** — the larger, portfolio-grade builds (ETL pipeline, RAG app, agent, capstone)

> [!NOTE]
> This board — and this repo — track a *real, in-progress* internship. Some modules are marked complete, others are still being worked through. The [Learning Progress](#-learning-progress) section reflects the current status honestly rather than pretending everything is finished on day one.

---

## 🧭 Internship Overview

| | |
|---|---|
| 🗓️ **Duration** | Wed, June 10 2026 → Fri, August 7 2026 (Mon–Fri working days) |
| 📆 **Length** | 43 working days across ~9 weeks |
| 📦 **Modules** | 10 modules organized into 2 phases |
| 🎯 **Learning approach** | One card = one working day: objective → topics → hands-on task → shipped deliverable |
| 🛠️ **Hands-on projects** | A mini-project or project at the end of nearly every module |
| 🎓 **Capstone** | A single end-to-end system combining data ingestion, a database, a RAG layer, and a tool-using agent |

The program runs in two phases:

- **Phase 1 — Programming & Data (Days 1–27):** Python from scratch → NumPy/Pandas/ML → Data Engineering & ETL → SQL/NoSQL databases → building APIs with FastAPI.
- **Phase 2 — Generative AI (Days 28–43):** LLM foundations & prompt engineering → Retrieval-Augmented Generation → agentic AI & tool use → closed-source models in production → final capstone.

**Daily routine:** concept session in the morning, hands-on exercise/project work in the afternoon, and code pushed to GitHub with a short learning note by end of day. Progress is checked at **Milestone reviews** at the end of each module, plus a final capstone presentation and demo on Day 43.

---

## 🗺️ Learning Roadmap

| Module | Duration | Topics | Projects | Status |
|---|---|---|---|---|
| **1. Python Foundations** | Days 1–4 | Environment setup, variables & types, collections, control flow | Calculator, unit converter, contact book, FizzBuzz | ✅ Done |
| **2. Advanced Python & Logic** | Days 5–8 | Functions & scope, nested loops & algorithms, comprehensions, OOP & file I/O | Reusable `utils.py`, pattern/algorithm drills, bank-account OOP app | ✅ Done |
| **3. NumPy, Pandas & ML** | Days 9–14 | NumPy arrays, Pandas I/II, visualization & EDA, regression, classification & clustering | EDA report, end-to-end ML mini-project | ✅ Done |
| **4. Data Engineering & ETL** | Days 15–19 | ETL/ELT concepts, web scraping, API ingestion, ETL pipelines, orchestration | Full ETL pipeline (`etl_pipeline.py`), scheduled job | ✅ Done |
| **5. Databases: SQL & NoSQL** | Days 20–24 | MySQL fundamentals, advanced SQL, PostgreSQL + Python, MongoDB & NoSQL | Scrape → DB pipeline (Phase 1 capstone) | ✅ Done |
| **6. APIs & FastAPI** | Days 25–27 | REST fundamentals, Pydantic/CRUD, auth/async/deployment | Deployed, authenticated CRUD API | 🟡 In Progress |
| **7. GenAI Foundations & Prompt Engineering** | Days 28–32 | How LLMs work, prompt engineering, OpenAI API, embeddings & function calling | GenAI mini-app (study buddy / summarizer) | ⬜ Upcoming |
| **8. RAG Systems** | Days 33–37 | RAG architecture, vector databases, LangChain/LlamaIndex pipelines, evaluation | "Chat with your Docs" RAG app | ⬜ Upcoming |
| **9. Agentic AI & Tools** | Days 38–41 | Agent concepts, function/tool calling, real-time actions, agent frameworks | Multi-tool research-assistant agent | ⬜ Upcoming |
| **10. Closed-Source Models & Capstone** | Days 42–43 | Production model landscape, provider comparison, final capstone | End-to-end capstone project | ⬜ Upcoming |

---

## 🗂️ Repository Structure

```
GenAI-Internship-Training-Program/
│
├── Module-01-Python-Foundations/
│   ├── day01_setup_basics/
│   ├── day02_variables_operators/
│   ├── day03_collections/
│   └── day04_control_flow/
│
├── Module-02-Advanced-Python-Logic/
│   ├── day05_functions_scope/
│   ├── day06_nested_loops_algorithms/
│   ├── day07_comprehensions_error_handling/
│   └── day08_oop_modules_fileio/
│
├── Module-03-NumPy-Pandas-ML/
│   ├── day09_numpy_fundamentals/
│   ├── day10_pandas_series_dataframes/
│   ├── day11_pandas_cleaning_groupby/
│   ├── day12_visualization_eda/
│   ├── day13_regression/
│   └── day14_classification_clustering_project/
│
├── Module-04-Data-Engineering-ETL/
│   ├── day15_etl_concepts/
│   ├── day16_web_scraping/
│   ├── day17_apis_data_ingestion/
│   ├── day18_etl_pipeline_project/
│   └── day19_automation_orchestration/
│
├── Module-05-Databases-SQL-NoSQL/
│   ├── day20_mysql_fundamentals/
│   ├── day21_advanced_sql/
│   ├── day22_postgresql_python/
│   ├── day23_mongodb_nosql/
│   └── day24_scrape_to_db_project/
│
├── Module-06-APIs-FastAPI/
│   ├── day25_rest_fastapi_basics/
│   ├── day26_pydantic_crud_db/
│   └── day27_auth_async_deployment/
│
├── Module-07-GenAI-Foundations-Prompt-Engineering/
│   ├── day28_intro_to_genai_llms/
│   ├── day29_prompt_engineering/
│   ├── day30_openai_api/
│   ├── day31_embeddings_function_calling/
│   └── day32_genai_mini_project/
│
├── Module-08-RAG-Systems/
│   ├── day33_rag_concepts_architecture/
│   ├── day34_vector_databases/
│   ├── day35_rag_pipeline_langchain/
│   ├── day36_rag_evaluation/
│   └── day37_chat_with_your_docs_project/
│
├── Module-09-Agentic-AI-Tools/
│   ├── day38_agentic_ai_concepts/
│   ├── day39_tools_function_calling/
│   ├── day40_realtime_knowledge_actions/
│   └── day41_agent_framework_project/
│
├── Module-10-Closed-Source-Models-Capstone/
│   ├── day42_closed_source_models/
│   └── day43_final_capstone/
│
├── resources/
│   └── learning-resources.md
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📚 Module Breakdown

### Module 1 · Python Foundations (Days 1–4)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Stand up a working Python environment and build fluency with core syntax, data types, and control flow.

**Learning objectives**
- Set up Python 3.12, VS Code, virtual environments, and Git/GitHub
- Master scalar types, operators, and string formatting
- Work fluently with lists, tuples, dicts, and sets
- Control program flow with conditionals and loops

**Topics covered**
- `venv`, `pip`, `requirements.txt`, REPL vs. scripts, Jupyter/Colab
- `int`/`float`/`str`/`bool`/`None`, type casting, f-strings, operator precedence
- List/tuple/dict/set CRUD, slicing, mutability, set algebra
- `if`/`elif`/`else`, `for`/`while`, `break`/`continue`, common loop patterns

**Hands-on exercises & assignments**
- Input-based calculator, unit converter (km↔mi, °C↔°F), BMI calculator
- Contact book, word-frequency counter, FizzBuzz, number-guessing game, multiplication table

**Projects:** —

**Key takeaways:** A working dev environment and Git workflow, plus fluency with Python's built-in data structures and control flow.

**Skills gained:** `Python syntax` · `Git/GitHub basics` · `Virtual environments` · `Data structures` · `Control flow`

</details>

---

### Module 2 · Advanced Python & Logic (Days 5–8)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Move from writing scripts to writing reusable, well-structured, Pythonic code.

**Learning objectives**
- Write reusable functions with proper scoping and argument handling
- Build algorithmic thinking through nested loops and pattern problems
- Use comprehensions, lambdas, and robust error handling
- Structure code with classes, modules, and file I/O

**Topics covered**
- `def`, `*args`/`**kwargs`, local vs. global scope, docstrings & type hints
- Nested loops, 2D lists, linear search, bubble sort, Big-O intuition
- List/dict/set comprehensions, `map`/`filter`/`sorted`/`enumerate`/`zip`
- `try`/`except`/`finally`, custom exceptions
- Classes, `__init__`, inheritance, module/package structure, JSON/CSV file I/O

**Hands-on exercises & assignments**
- Refactored Day 1–4 scripts into a `utils.py` module
- Matrix transpose, prime sieve, star patterns, 5 algorithm practice problems
- Pythonic rewrite of loop-based code with full input validation

**Projects**
- 🏦 **Bank-account OOP mini-project** with persisted JSON records

**Key takeaways:** Clean, modular, defensively-written Python that's ready to scale into larger applications.

**Skills gained:** `Functions & scope` · `Algorithmic thinking` · `Comprehensions` · `Exception handling` · `OOP` · `File I/O`

</details>

---

### Module 3 · NumPy, Pandas & ML (Days 9–14)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Go from raw numerical computing to a full, evaluated machine learning workflow.

**Learning objectives**
- Perform fast, vectorized computation with NumPy
- Load, clean, and reshape tabular data with Pandas
- Run a proper exploratory data analysis with visualizations
- Train and evaluate regression, classification, and clustering models

**Topics covered**
- `ndarray`, broadcasting, aggregations, reshaping, basic linear algebra
- `Series`/`DataFrame`, `loc`/`iloc`, `groupby`, `merge`/`join`, `pivot_table`
- Matplotlib/Seaborn, histograms, box plots, correlation heatmaps
- Train/test split, linear & polynomial regression, MAE/MSE/R²
- Logistic Regression, KNN, Decision Trees, Random Forest, K-Means, confusion matrix

**Hands-on exercises & assignments**
- `numpy_lab.ipynb`, `pandas_explore.ipynb` (10 insights on a real dataset)
- `data_cleaning.ipynb` (raw → clean) and `eda_report.ipynb`
- `regression.ipynb` predicting a numeric target

**Projects**
- 📊 **Module 3 mini-project:** full pipeline — dataset → clean → EDA → train → evaluate → written report

**Key takeaways:** The complete "data → model → evaluation" ML workflow, and when to reach for which algorithm.

**Skills gained:** `NumPy` · `Pandas` · `Data visualization` · `EDA` · `scikit-learn` · `Model evaluation`

</details>

---

### Module 4 · Data Engineering & ETL (Days 15–19)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Learn how data actually moves — from source, through transformation, into storage — and automate it.

**Learning objectives**
- Understand the ETL/ELT model and where data engineering fits
- Extract data via web scraping and REST APIs
- Build a complete, runnable ETL pipeline
- Automate and schedule pipelines reliably

**Topics covered**
- ETL vs. ELT, batch vs. streaming, staging areas, idempotency, data quality
- `requests`, BeautifulSoup, Selenium/Playwright, pagination, `robots.txt` ethics
- REST auth (API keys/tokens), retries, backoff, raw-data staging
- Structuring extract/transform/load functions, Pandas transforms, logging
- `cron`, Python schedulers, an introduction to **Apache Airflow DAGs**

**Hands-on exercises & assignments**
- Architecture sketch of a chosen ETL use-case
- `scraper.py` producing clean CSV/JSON output
- `api_ingest.py` with retry logic and saved raw responses

**Projects**
- ⚙️ **`etl_pipeline.py`** — a runnable end-to-end ETL pipeline with logging
- 🕒 **Scheduled ETL job** with a short operational runbook

**Key takeaways:** How to design idempotent, observable pipelines that run unattended on a schedule.

**Skills gained:** `Web scraping` · `API ingestion` · `ETL pipeline design` · `Scheduling & orchestration` · `Logging & error handling`

</details>

---

### Module 5 · Databases: SQL & NoSQL (Days 20–24)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Model and query data relationally and non-relationally, then connect it all to Python.

**Learning objectives**
- Design relational schemas and write core-to-advanced SQL
- Connect PostgreSQL and MongoDB to Python programs
- Choose the right database for a given use-case
- Load pipeline output into a real database

**Topics covered**
- MySQL fundamentals: tables, keys, `CREATE`/`SELECT`/`UPDATE`/`DELETE`, normalization
- Advanced SQL: joins, `GROUP BY`, subqueries, CTEs, indexing, `EXPLAIN`, transactions
- PostgreSQL + `psycopg2`/SQLAlchemy, parameterized queries, Pandas integration
- MongoDB: collections, BSON documents, `pymongo` CRUD, aggregation pipelines
- Bulk inserts/upserts, batching, SQL vs. NoSQL trade-offs

**Hands-on exercises & assignments**
- `schema.sql` with a 3-table design, `analytics_queries.sql`
- `pg_client.py` querying Postgres into a DataFrame
- `mongo_crud.py` with an aggregation example

**Projects**
- 🔗 **Phase 1 capstone:** full automated pipeline — source → ETL → database, scheduled end-to-end

**Key takeaways:** Confident, safe SQL and NoSQL usage, and the judgment to pick the right storage layer.

**Skills gained:** `SQL` · `PostgreSQL` · `MongoDB` · `Database design` · `SQL-injection-safe querying`

</details>

---

### Module 6 · APIs & FastAPI (Days 25–27)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Build, validate, secure, and deploy a real backend API — the layer that later serves GenAI features.

**Learning objectives**
- Understand REST principles and HTTP semantics
- Build validated, data-backed CRUD endpoints
- Add authentication, async support, and deploy an API

**Topics covered**
- HTTP verbs & status codes, path/query params, FastAPI + Uvicorn, auto-generated `/docs`
- Pydantic models, request/response schemas, `Depends`, CRUD wired to a database
- API keys/JWT/OAuth2 basics, `async def`, middleware, CORS, Docker deployment

**Hands-on exercises & assignments**
- A small FastAPI app with multiple GET/POST endpoints
- A CRUD API backed by the Module 5 PostgreSQL/MySQL schema

**Projects**
- 🔐 **Deployed, authenticated API** — auth added, deployed, and called from a client

**Key takeaways:** How to expose data and (eventually) models behind a production-shaped, documented API.

**Skills gained:** `REST API design` · `FastAPI` · `Pydantic validation` · `Authentication` · `Async programming` · `Deployment`

</details>

---

### Module 7 · GenAI Foundations & Prompt Engineering (Days 28–32)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Build accurate mental models of how LLMs work, then learn to steer them reliably and call them programmatically.

**Learning objectives**
- Understand tokens, context windows, temperature, and embeddings at an intuitive level
- Write effective zero-shot, few-shot, and chain-of-thought prompts
- Call LLM APIs safely and handle keys/secrets correctly
- Use embeddings for semantic search and structured/function-calling output

**Topics covered**
- The GPT/Claude/Llama landscape, hallucinations & limitations, cost/latency/safety basics
- System/user/assistant roles, output formatting, guardrails, prompt debugging
- `.env` secrets, the OpenAI Python SDK, streaming, retries, token/cost tracking
- Embeddings API, forced JSON/structured outputs, an introduction to function/tool calling

**Hands-on exercises & assignments**
- Logged observations from a chat-model playground session
- `prompts.md` — a 5-task prompt library with before/after iterations
- `llm_client.py` CLI app streaming model responses
- `semantic_search.py` performing embedding-based search

**Projects**
- 🤖 **GenAI mini-project:** an assistant (study buddy / email writer / summarizer) with a Streamlit or CLI front-end

**Key takeaways:** LLMs go from "black box" to a programmable component with predictable failure modes and levers you can pull.

**Skills gained:** `Prompt engineering` · `LLM APIs (OpenAI/Anthropic)` · `Embeddings` · `Structured output` · `Function calling basics`

</details>

---

### Module 8 · RAG Systems (Days 33–37)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Ground LLM outputs in real, private, or fresh data using Retrieval-Augmented Generation.

**Learning objectives**
- Understand the load → chunk → embed → store → retrieve → generate architecture
- Store and query embeddings efficiently with a vector database
- Build an end-to-end RAG pipeline with citations
- Evaluate and improve retrieval quality

**Topics covered**
- Chunking strategies & overlap, similarity metrics, metadata filtering
- Vector databases: FAISS, Chroma, Pinecone, pgvector; ANN search; persistence
- LangChain/LlamaIndex: loaders, text splitters, retrievers, prompt templates
- Re-ranking, hybrid search, hallucination reduction, RAGAS-style evaluation

**Hands-on exercises & assignments**
- RAG architecture diagram + a chunking experiment
- `vector_store.py` with query examples over indexed chunks
- `rag_pipeline.py` answering questions with source citations
- An evaluation notebook comparing baseline vs. improved retrieval

**Projects**
- 📄 **"Chat with your Docs":** upload → index → ask → cited answers, with a Streamlit UI and evaluated retrieval

**Key takeaways:** How to build a RAG system that's not just functional, but measurably accurate.

**Skills gained:** `RAG architecture` · `Vector databases` · `LangChain / LlamaIndex` · `Retrieval evaluation` · `Hallucination mitigation`

</details>

---

### Module 9 · Agentic AI & Tools (Days 38–41)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Give models the ability to act — calling tools, chaining steps, and working toward a goal.

**Learning objectives**
- Understand what makes a system "agentic" vs. a plain LLM call
- Define tools with JSON schemas and wire up a function-calling loop
- Combine RAG (knowledge) with tools (actions) for multi-step tasks
- Use an agent framework to orchestrate tools, memory, and planning

**Topics covered**
- Agents vs. LLM calls, the ReAct (reason→act) loop, planning & reflection
- Tool/function schemas, execution & error handling, argument-validation safety
- Live tools (web search, REST APIs, databases), short vs. long-term memory
- LangChain agents / LangGraph / CrewAI overview, guardrails, observability

**Hands-on exercises & assignments**
- Traced an agent's decision loop from logs
- `tools.py` with 2–3 callable tools (calculator, web/DB lookup) plus a selecting agent
- `realtime_agent.py` performing a multi-step task against live data

**Projects**
- 🕵️ **Multi-tool research-assistant agent:** search → RAG → summarize → save

**Key takeaways:** How to move from "the model answers" to "the model acts" — safely and observably.

**Skills gained:** `Agentic AI design` · `Function/tool calling` · `Multi-step reasoning` · `Agent frameworks` · `Observability & guardrails`

</details>

---

### Module 10 · Closed-Source Models & Capstone (Days 42–43)

<details>
<summary><strong>Expand for full module details</strong></summary>

**Overview:** Choose and run closed-source models responsibly in production, then bring the entire program together.

**Learning objectives**
- Compare closed-source model providers on capability, cost, and latency
- Write a provider-agnostic client wrapper
- Ship one capstone system that integrates data, retrieval, and agentic action

**Topics covered**
- OpenAI GPT, Anthropic Claude, and Google Gemini landscape
- Key management, rate limits, caching, monitoring, safety & privacy
- Open- vs. closed-source trade-offs (brief)

**Hands-on exercises & assignments**
- Ran the same task across two providers and compared cost/quality

**Projects**
- 🎓 **Final Capstone:** one project combining a data pipeline (scrape/ingest → ETL → database), a GenAI layer (RAG over that data), a tool-using agent, a simple UI, and safe API-key handling — presented live with a code walkthrough and Q&A

**Key takeaways:** How every module — data, databases, APIs, GenAI, RAG, and agents — fits together into one production-shaped system.

**Skills gained:** `Provider evaluation` · `Production LLM concerns` · `System integration` · `Technical presentation`

</details>

---

## 🧰 Technologies Used

<table>
<tr><td valign="top">

**Programming**
- Python 3.12
- PEP8 / clean code practices

</td><td valign="top">

**AI**
- OpenAI API
- Anthropic (Claude) API
- Prompt Engineering

</td><td valign="top">

**Machine Learning**
- scikit-learn
- NumPy
- Pandas

</td></tr>
<tr><td valign="top">

**Databases**
- MySQL
- PostgreSQL
- MongoDB
- SQLAlchemy / psycopg2 / pymongo

</td><td valign="top">

**Vector Databases**
- Chroma
- FAISS
- (Pinecone / pgvector — overview)

</td><td valign="top">

**Cloud & Deployment**
- Docker
- Uvicorn / Gunicorn
- Cloud hosting (API deployment)

</td></tr>
<tr><td valign="top">

**Frameworks**
- FastAPI
- LangChain / LlamaIndex
- Streamlit
- Apache Airflow (intro)

</td><td valign="top">

**Tools**
- Jupyter / Google Colab
- BeautifulSoup / Selenium / Playwright
- Matplotlib / Seaborn

</td><td valign="top">

**Developer Tools & VCS**
- VS Code
- Git & GitHub
- `venv` / `pip` / `requirements.txt`

</td></tr>
</table>

---

## 🧠 Skills Acquired

| Category | Skills |
|---|---|
| **Python** | Core syntax, data structures, OOP, error handling, comprehensions, file I/O |
| **Machine Learning** | Regression, classification, clustering, model evaluation, scikit-learn |
| **Generative AI** | LLM fundamentals, embeddings, structured output, closed-source model selection |
| **Prompt Engineering** | Zero-/few-shot prompting, chain-of-thought, guardrails, prompt debugging |
| **Data Engineering** | Web scraping, API ingestion, ETL pipeline design, scheduling & orchestration |
| **Backend** | REST API design, FastAPI, Pydantic validation, auth, async, deployment |
| **LLMs** | OpenAI & Anthropic SDKs, token/cost management, function calling |
| **Agentic AI** | Tool calling, the ReAct loop, multi-step reasoning, agent frameworks |
| **RAG** | Chunking, vector databases, retrieval pipelines, retrieval evaluation |
| **Problem Solving** | Algorithmic thinking, debugging, system design, end-to-end project delivery |

---

## 🚀 Projects

| Project | Description | Technologies | Folder |
|---|---|---|---|
| ML Mini-Project | End-to-end pipeline: clean → EDA → train → evaluate a classifier/regressor | Pandas, NumPy, scikit-learn | `Module-03-NumPy-Pandas-ML/day14_.../` |
| ETL Pipeline | Idempotent extract → transform → load pipeline with logging | Python, Requests, BeautifulSoup, Pandas | `Module-04-Data-Engineering-ETL/day18_.../` |
| Scheduled ETL Job | The ETL pipeline running unattended on a schedule | Python, `cron` / Airflow concepts | `Module-04-Data-Engineering-ETL/day19_.../` |
| Scrape → DB Pipeline | Full pipeline loading scraped/ingested data into a real database | Python, MySQL/PostgreSQL/MongoDB | `Module-05-Databases-SQL-NoSQL/day24_.../` |
| Deployed CRUD API | Authenticated, documented REST API backed by a database | FastAPI, Pydantic, SQLAlchemy, Docker | `Module-06-APIs-FastAPI/day27_.../` |
| GenAI Mini-App | A prompt-driven assistant with a simple UI | OpenAI/Anthropic SDK, Streamlit | `Module-07-.../day32_.../` |
| Chat-with-your-Docs | RAG app answering questions over uploaded documents with citations | LangChain/LlamaIndex, Chroma/FAISS, Streamlit | `Module-08-RAG-Systems/day37_.../` |
| Research-Assistant Agent | Multi-tool agent: search → RAG → summarize → save | LangChain agents / LangGraph, tool calling | `Module-09-Agentic-AI-Tools/day41_.../` |
| **Final Capstone** | Full-stack GenAI system: data pipeline + RAG + agent + UI | Everything above | `Module-10-.../day43_final_capstone/` |

---

## 📈 Learning Progress

> [!TIP]
> This tracker reflects real, current status — it's updated as modules are actually completed, not pre-filled.

- ✅ **Module 1** · Python Foundations
- ✅ **Module 2** · Advanced Python & Logic
- ✅ **Module 3** · NumPy, Pandas & ML
- ✅ **Module 4** · Data Engineering & ETL
- ✅ **Module 5** · Databases: SQL & NoSQL
- 🟡 **Module 6** · APIs & FastAPI
- ⬜ **Module 7** · GenAI Foundations & Prompt Engineering
- ⬜ **Module 8** · RAG Systems
- ⬜ **Module 9** · Agentic AI & Tools
- ⬜ **Module 10** · Closed-Source Models & Capstone

---

## 🛠️ How to Use

### Clone the repository

```bash
git clone https://github.com/your-username/GenAI-Internship-Training-Program.git
cd GenAI-Internship-Training-Program
```

### Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Set up environment variables

Create a `.env` file for any module that calls an external API (never commit real keys):

```env
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
MONGODB_URI=mongodb://localhost:27017
```

### Run notebooks

```bash
jupyter notebook
# or open any .ipynb directly in VS Code / Google Colab
```

### Run scripts

```bash
python Module-01-Python-Foundations/day01_setup_basics/calculator.py
```

### Run the FastAPI service (Module 6+)

```bash
uvicorn main:app --reload
# Interactive docs available at http://127.0.0.1:8000/docs
```

---

## 📚 Resources

A running list of the resources actually used throughout the program:

- **Foundational GenAI & RAG courses** — introductory video series on generative AI concepts and Retrieval-Augmented Generation
- **Data Engineering course material** — ETL/ELT concepts, pipeline design, and orchestration fundamentals
- **Vector database documentation** — FAISS, Chroma, and general vector-store references used in Module 8
- **RAG-specific resources** — architecture patterns and evaluation approaches (RAGAS-style) for retrieval quality
- **Official docs** — Python, FastAPI, Pandas, scikit-learn, LangChain/LlamaIndex, OpenAI, and Anthropic documentation, used continuously as ground truth throughout the program

---

## 🔮 Future Improvements

- [ ] Add more end-to-end projects beyond the capstone (e.g. a multi-agent workflow)
- [ ] Expand datasets used in Module 3 with real-world, messier sources
- [ ] Explore fine-tuning open-source models as a complement to closed-source APIs
- [ ] Deploy select projects (API, RAG app, agent) to a persistent cloud environment
- [ ] Build out a formal evaluation suite for the RAG and agent projects
- [ ] Extend Module 9 into more advanced multi-agent orchestration
- [ ] Add multi-modal AI experiments (vision + text) as a follow-on module

---

## 🙏 Acknowledgements

Thanks to the mentors and reviewers behind this internship program for structuring a curriculum that goes deep on fundamentals before ever touching an LLM API — and for the module-review checkpoints that kept the pace honest. Thanks also to the open-source maintainers of Python, Pandas, scikit-learn, FastAPI, LangChain, and the broader GenAI tooling ecosystem that this program builds on.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If you're following a similar learning path, consider starring this repo to track along.**

</div>
