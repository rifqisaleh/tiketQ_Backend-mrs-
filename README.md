# 🎟️ TicketQ Backend API

A RESTful API built with Flask for managing event tickets. It supports full CRUD operations and includes automated tests using `pytest`.

<br><br>

## 🚀 Features

- Create, view, update, and delete tickets
- Mark tickets as used
- UUID-based ticket IDs
- ISO 8601-compliant datetime fields
- Dockerized with PostgreSQL
- SQLite in-memory database for testing
- Clean project structure (routes, services, repositories)


<br><br>

## 🛠️ Tech Stack

- Python 3.11
- Flask + Flask-SQLAlchemy + Flask-Migrate
- PostgreSQL (via Docker)
- Pytest
- Marshmallow for validation


<br><br>

## 📁 Project Structure

```
ticketQ/
├── app/
│   ├── models/
│   ├── routes/
│   ├── repo/
│   ├── schemas/
│   ├── services/
│   └── __init__.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```


<br><br>

## ⚙️ Getting Started

### 🔧 Requirements

- Docker + Docker Compose
- Python 3.11 (for running tests locally)



### 📦 Installation (with Docker)

```bash
git clone https://github.com/your-username/ticketQ_Backend.git
cd ticketQ_Backend

# Build and start containers
docker-compose up --build
```

Visit:  
```
http://localhost:5001/tickets/
```


<br><br>

## 🗃️ Database Migrations (First-Time Only)

```bash
docker exec -it ticketq-api flask db init      # only once
docker exec -it ticketq-api flask db migrate -m "init"
docker exec -it ticketq-api flask db upgrade
```

<br><br>

## 📬 Postman Collection

You can import the API collection using this file:

🗂️ [`tiketQ.postman_collection.json`](./postman/tiketQ.postman_collection.json)

or

```
./postman/tiketQ.postman_collection.json
```
<br>

💡 Make sure your local server is running at: `http://localhost:5001`


<br><br>

## 🧪 Running Tests (Outside Docker)

Tests use SQLite in-memory DB for isolation.

### 1. Install dependencies:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Run tests:

```bash
PYTHONPATH=. pytest tests/
```

<br><br>

## 🔥 API Endpoints

| Method | Endpoint            | Description           |
|--------|---------------------|-----------------------|
| GET    | `/tickets/`         | Get all tickets       |
| POST   | `/tickets/`         | Create new ticket     |
| GET    | `/tickets/<id>`     | Get ticket by ID      |
| PATCH  | `/tickets/<id>`     | Mark ticket as used   |
| DELETE | `/tickets/<id>`     | Delete ticket         |


<br><br>

## 📌 Environment Variables

Create a `.env` file (for local non-Docker use):

```
FLASK_ENV=development
DATABASE_URL=sqlite:///ticket.db
```

---