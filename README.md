# ML & AI Engineering Journey

Documenting my path from full-stack/Android development into Machine Learning Engineering, and eventually AI/LLM Engineering — built deliberately, in sequence, with real production-quality projects, not just tutorials followed.

## Why this order

I'm going ML Engineering first, then AI/LLM Engineering second. Reasoning: I want to understand how models are actually trained, evaluated, and deployed before I build products on top of them — not just call an API and call it a day. AI/LLM engineering builds directly on this foundation.

## Roadmap

### Phase 1 — ML Engineering
| Week | Topic | Status |
|------|-------|--------|
| 1-2 | Python fundamentals, NumPy, Git, Math foundations (linear algebra, probability & statistics, calculus) | ✅ Complete |
| 3 | Pandas, EDA, data cleaning, feature engineering, basic SQL | ✅ Complete |
| 4-5 | Classical ML (regression, trees, SVMs, k-means, Naive Bayes), model evaluation, explainability (SHAP/LIME) | ⏳ Upcoming |
| 6-8 | Deep Learning (neural networks, CNNs, RNNs/LSTMs, Transformers) — includes a real image classifier build | ⏳ Upcoming |
| 9 | MLOps & Production (MLflow, CI/CD, FastAPI + Docker, monitoring) — **Capstone Project 1**: a deployed, monitored, versioned model | ⏳ Upcoming |

### Phase 2 — AI / LLM Engineering
| Week | Topic | Status |
|------|-------|--------|
| 10 | Async/await, prompt engineering, Hugging Face, fine-tuning (LoRA/QLoRA) | ⏳ Upcoming |
| 11 | Embeddings & retrieval (FAISS/Chroma/Pinecone) — semantic search tool | ⏳ Upcoming |
| 12-13 | RAG & Agents (LangChain, CrewAI, MCP), LLM serving, evaluation (RAGAS, LLM-as-judge) | ⏳ Upcoming |
| 14 | **Capstone Project 2**: a deployed RAG/agent system, AI safety review, interview prep | ⏳ Upcoming |

## Repo structure

```
ml-ai-engineering-journey/
├── week-01-02-python-fundamentals/
├── week-03-pandas-eda/
├── week-04-05-classical-ml/
├── week-06-08-deep-learning/
├── week-09-mlops-capstone-1/
├── week-10-llm-foundations/
├── week-11-embeddings-retrieval/
├── week-12-13-rag-agents/
└── week-14-capstone-2/
```

Each folder contains practice notebooks/scripts for that week's topics, plus a short `notes.md` summarizing what I learned and any gotchas.

## Background

Coming from a full-stack and Android development background (Kotlin/Jetpack Compose), with hands-on internship experience building React/Vite job board applications and CRUD + JWT backends. This repo is where the ML/AI layer gets built on top of that foundation.

## Follow along

I'm committing regularly as I work through each topic. Feedback, corrections, and suggestions are welcome — always glad to hear from people further along this path.
