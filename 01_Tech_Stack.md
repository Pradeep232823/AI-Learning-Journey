# AI Engineering Bootcamp - Tech Stack

Document ID: TECH_STACK_V1

> **Version:** 1.0
> **Status:** Active
> **Last Updated:** [Date]

---

# Purpose

This document defines the official technology stack used throughout the AI Engineering Bootcamp.

Only the technologies listed here are considered part of the learning roadmap.

New technologies should only be added if they provide significant practical value and align with the bootcamp objectives.

---

# Bootcamp Philosophy

The goal is **not** to learn every AI tool.

The goal is to master the technologies required to build real-world AI applications.

Priority is given to:

- Industry adoption
- Practical usefulness
- Strong fundamentals
- Long-term relevance

---

# Technology Stack Overview

```
Programming
        │
        ▼
Development Tools
        │
        ▼
Backend Development
        │
        ▼
Databases
        │
        ▼
LLM Engineering
        │
        ▼
RAG Systems
        │
        ▼
AI Agents
        │
        ▼
Frontend
        │
        ▼
Deployment
        │
        ▼
Production AI Applications
```

---

# 1. Programming

|       Technology            | Purpose                   | Setup Status                      | Status   |
|-----------------------------|---------------------------|-----------------------------------|----------|
| Python                      | Programming language      | Python 3.10.0                     | Learning |
| Git                         | Version control           | git version 2.50.1.windows.1      | Learning |
| GitHub                      | Portfolio & collaboration | Active account                    | Learning |
| VS Code                     | Development environment   | Installed                         | Learning |
| Terminal / CLI              | Professional workflow     | VS Code Terminal / System CLI     | Learning |
| Virtual Environments (venv) | Project isolation         | venv will be created in projects  | Learning |
| pip                         | Package management        | pip 26.0.1                        | Learning |

---

# 2. Internet & API Fundamentals

| Technology            | Purpose                                 | Status |
|-----------------------|-----------------------------------------|--------|
| HTTP                  | Communication between client and server | Learn  |
| REST APIs             | Build AI services                       | Learn  |
| JSON                  | Data exchange                           | Learn  |
| Environment Variables | Secure API keys                         | Learn  |

---

# 3. AI & LLM Engineering

| Technology               | Purpose                   | Status |
|--------------------------|---------------------------|--------|
| LLM APIs                 | Build AI applications     | Learn  | (Open AI Api created)
| Prompt Engineering       | Better AI outputs         | Learn  |
| Context Engineering      | Better AI systems         | Learn  |
| Structured Outputs       | Reliable responses        | Learn  |
| Function / Tool Calling  | AI actions                | Learn  |
| Streaming Responses      | Real-time AI applications | Learn  |
| Token Management         | Cost optimization         | Learn  |

---

# 4. Backend Development

| Technology | Purpose                | Status | Setup Status |
|------------|------------------------|--------|--------------|
| FastAPI    | AI backend development | Learn  |   0.141.1    |
| Pydantic   | Data validation        | Learn  |   2.12.5     |
| Uvicorn    | API server             | Learn  |   0.52.0     |

---

# 5. Databases

| Technology | Purpose                    | Status |      Setup Status          |
|------------|----------------------------|--------|----------------------------|
| SQLite     | Local application database | Learn  |         3.35.5             |
| PostgreSQL | Production database        | Learn  | postgres (PostgreSQL) 18.4 |

> **Note:** Existing MySQL knowledge will be leveraged. Only database-specific differences will be covered.

---

# 6. RAG (Retrieval-Augmented Generation)

| Technology               | Purpose                | Status | Setup Status |
|--------------------------|------------------------|--------|--------------|
| Embeddings               | Semantic understanding | Learn  |      NA      |
| Chunking                 | Document processing    | Learn  |      NA      |
| Vector Database (Chroma) | Store embeddings       | Learn  |     1.5.9    |
| Retrieval Pipeline       | Knowledge retrieval    | Learn  |      NA      |

---

# 7. AI Agents & Workflows

| Technology         | Purpose                   | Status |
|--------------------|---------------------------|--------|
| Tool Calling       | External tool usage       | Learn  |
| Memory             | Personalized AI           | Learn  |
| AI Workflows       | Multi-step automation     | Learn  |
| Agent Architecture | Autonomous task execution | Learn  |

---

# 8. AI Frameworks

These frameworks will be introduced **only after** understanding the underlying concepts.

| Technology | Purpose         | Status | Setup Status |
|------------|-----------------|--------|--------------|
| LangChain  | AI pipelines    | Learn  |    1.3.14    |
| LangGraph  | Agent workflows | Learn  |    1.2.10    |

> Frameworks are used to improve productivity, not to replace understanding.

---

# 9. Frontend Development

| Technology | Purpose                 | Status | Setup Status                  |
|------------|-------------------------|--------|-------------------------------|
| HTML       | Structure               | Learn  |      NA                       |
| CSS        | Styling                 | Learn  |      NA                       |
| JavaScript | Client-side interaction | Learn  |      NA                       |
| React      | Build AI interfaces     | Learn  | node (v22.19.0), npm (10.9.3) |

> Only the frontend knowledge required for AI applications will be covered.

---

# 10. Deployment

| Technology       | Purpose             | Status |          Setup Status                |
|------------------|---------------------|--------|--------------------------------------|
| Docker           | Containerization    | Learn  | Docker version 29.6.2, build dfc4efb |
| Render / Railway | Cloud deployment    | Learn  |           Render ok                  |
| GitHub           | Source code hosting | Learn  |           Completed                  |

---

# Development Workflow

Throughout the bootcamp, every project follows this workflow:

```
Idea
    ↓
Planning
    ↓
Development
    ↓
Testing
    ↓
Debugging
    ↓
Git Commit
    ↓
GitHub Push
    ↓
Documentation
    ↓
Deployment
```

---

# Project Technology Progression

## Beginner Projects

- Python
- Git
- GitHub
- APIs
- Prompt Engineering

---

## Intermediate Projects

- FastAPI
- Pydantic
- LLM APIs
- Structured Outputs
- Function Calling

---

## Advanced Projects

- Embeddings
- Chroma
- RAG
- AI Agents
- Memory
- Workflows

---

## Production Projects

- PostgreSQL
- Docker
- Deployment
- Portfolio
- Production Architecture

---

# Technologies Not Included

The following technologies are intentionally excluded from this 30-day bootcamp.

They may be learned after becoming proficient in AI Engineering.

- Java
- TensorFlow
- PyTorch Model Training
- CUDA
- Reinforcement Learning
- Computer Vision
- GANs
- Diffusion Model Training
- Advanced MLOps
- Distributed AI Training
- Building Foundation Models

---

# Learning Order

The technologies will be learned in this sequence:

```
Python
        ↓
Git & GitHub
        ↓
HTTP + APIs
        ↓
LLM APIs
        ↓
Prompt Engineering
        ↓
FastAPI
        ↓
Databases
        ↓
Embeddings
        ↓
Vector Database
        ↓
RAG
        ↓
AI Agents
        ↓
LangChain
        ↓
LangGraph
        ↓
Deployment
        ↓
Portfolio
```

---

# Guiding Principles

- Learn concepts before frameworks.
- Build before memorizing.
- Use official documentation.
- Understand every line of code.
- Optimize for employable skills.
- Build production-style applications.
- Focus on quality over quantity.

---

# Final Goal

By the end of this bootcamp, I should be capable of designing, building, deploying, and explaining modern AI applications using this technology stack without relying on tutorials.