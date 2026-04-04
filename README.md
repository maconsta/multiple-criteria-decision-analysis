# Multiple Criteria Decision Analysis

A web application for evaluating and ranking alternatives using multiple-criteria decision analysis (MCDA) methods. Users can create projects, define decision tasks with criteria and alternatives, run an MCDA method, and view ranked results.

**Supported methods:** TOPSIS, AHP, ELECTRE, PROMETHEE, Weighted Sum.

**Stack:** Vue 3 (frontend) · Flask + SQLAlchemy (backend) · PostgreSQL · numpy (MCDA algorithms)

---

## Project Structure

```
├── frontend/       Vue 3 SPA
├── backend/        Flask REST API
└── mcda/           MCDA algorithm library + CLI
```

---

## Running Locally

### Prerequisites

- Python 3.11+
- Node.js 20+
- PostgreSQL 14+

### 1. Configure environment variables

```bash
cp backend/.env.example backend/.env
```

Edit `backend/.env`. The default values in `.env.example` match a standard local PostgreSQL install (`localhost`, user `postgres`, database `mcda`). Generate a JWT secret key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 2. Set up a local PostgreSQL database

Create the database and run the init script to create all tables:

```bash
# Create the database (run once)
createdb -U postgres mcda

# Create all tables
psql -U postgres -d mcda -f backend/db/init.sql
```

> The init script is idempotent — safe to re-run any time.

### 3. Set up Python environment

From the project root:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r backend/requirements.txt
```

### 4. Test the database connection

```bash
python -c "import sys; sys.path.insert(0, '.'); from backend.app.db.models import engine; conn = engine.connect(); print('DB OK'); conn.close()"
```

### 5. Start the Flask backend

```bash
python backend/run.py
```

Runs on `http://127.0.0.1:5000`.

### 6. Start the Vue frontend

In a separate terminal:

```bash
cd frontend
npm install   # first time only
npm run serve
```

Runs on `http://localhost:8080`.

---

## CLI (optional)

A standalone command-line interface for running MCDA analyses without the web app:

```bash
python mcda/console-app.py
```

