# Atlas

> A production-ready FastAPI backend built to demonstrate modern backend engineering practices.

## Overview

Atlas is a backend engineering project focused on building a clean, scalable, and production-oriented API using FastAPI.

The goal of the project is not simply to build CRUD endpoints, but to showcase the engineering practices expected from backend and founding engineers, including authentication, database migrations, containerization, and maintainable architecture.

---

## Features

- User Authentication (JWT)
- Secure Password Hashing
- Authorization
- Notes CRUD API
- SQLAlchemy ORM
- Alembic Database Migrations
- PostgreSQL
- Docker & Docker Compose
- Environment Variable Configuration
- Request Logging
- Global Exception Handling
- Pydantic Validation
- Modular Project Structure

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migrations |
| Pydantic | Data Validation |
| Docker | Containerization |
| Docker Compose | Multi-container Development |
| JWT | Authentication |

---

## Project Structure

```
Atlas/
│
├── alembic/
├── app/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── db/
│   ├── middleware/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd Atlas
```

---

## Run with Docker

Build the containers

```bash
docker compose build
```

Start the application

```bash
docker compose up
```

The API will be available at

```
http://localhost:8000
```

Interactive API documentation

```
http://localhost:8000/docs
```

---

## Local Development

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

---

## Current Progress

- [x] FastAPI setup
- [x] PostgreSQL integration
- [x] SQLAlchemy ORM
- [x] Alembic migrations
- [x] JWT Authentication
- [x] Authorization
- [x] Notes CRUD
- [x] Docker support
- [x] Docker Compose
- [x] Logging
- [x] Exception Handling

### Planned

- [ ] Health Checks
- [ ] Automatic Alembic Migrations
- [ ] GitHub Actions CI
- [ ] Automated Testing
- [ ] Cloud Deployment
- [ ] Monitoring & Observability

---

## Engineering Goals

Atlas is being built to demonstrate production-level backend engineering practices including:

- Clean Architecture
- Maintainable Code
- Containerized Development
- Secure Authentication
- Database Versioning
- Scalable API Design
- Production Readiness

---

## License

This project is for educational and portfolio purposes.