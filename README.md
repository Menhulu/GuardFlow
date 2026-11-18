# GuardFlow

**Drag-and-drop AI agents with quality gates built in.**

GuardFlow is an agent platform for regulated industries such as insurance and finance.
Business users build and change agents on a visual canvas. Every change, from a canvas
edit to a prompt tweak, must pass two gates before it goes live:

1. **Structure check**: policy rules on the graph itself (for example, every "decline" path must pass human review).
2. **Regression check**: the new version is replayed against real past cases and compared with the current version.

## Why

Most agent builders help teams ship fast. GuardFlow helps them ship safely.
In insurance or finance, one missing edge on a canvas can skip a human review step.
GuardFlow keeps the flexibility of a no-code canvas and adds the controls a production team needs.

## Key features

- **Visual canvas**: build agents from typed nodes (LLM call, retrieval, branch, tool, judge, human review, reply).
- **One flow spec**: the canvas, forms and natural-language edits all change the same JSON flow spec, which is compiled into a [LangGraph](https://docs.langchain.com/oss/python/langgraph) graph.
- **Tiered judging**: a fast decision model ([Jev](https://typesafe.ai)) or small model first, an LLM judge with a rubric second, a human reviewer last.
- **Human review queue**: low-confidence outputs pause the graph and wait for a reviewer.
- **Closed loop**: every human override becomes a new regression case.
- **Release gate**: structure and regression checks run on every change, in the UI and in CI.
- **Dashboards**: quality, latency and cost per agent version.

## Demo scenario

**Insurance claims intake agent**: reads a customer claim email, extracts key details,
retrieves the relevant policy clauses, decides the route (accept, request documents,
or send to a human) and drafts a reply.

A second agent (tenancy maintenance requests) is built from the same template by
configuration only, to show the platform is not tied to one use case.

## Architecture

```
Canvas / Forms (Next.js + React Flow)
        │  JSON flow spec
        ▼
Flow compiler ──► LangGraph runtime ──► agent outputs + traces
        │                                     │
Structure check                     Tiered judges (Jev / LLM / human)
        │                                     │
        └────────► Regression suite ◄─────────┘
                        │
                 Release gate + dashboards
```

## Tech stack

| Layer | Choice |
| --- | --- |
| Agent runtime | Python, LangGraph |
| API | FastAPI |
| Storage | Postgres + pgvector |
| Frontend | Next.js, React Flow |
| Observability | Langfuse |
| CI | GitHub Actions |

## Getting started

```bash
# Database
docker compose up -d db

# Backend
cd backend
uv sync
uv run uvicorn guardflow.api:app --reload
uv run pytest
```

Copy `.env.example` to `.env` and fill in your model API keys.

## Project layout

```
backend/    Python: flow spec, compiler, runtime, judges, API
frontend/   Next.js canvas and review UI
```

## License

MIT
