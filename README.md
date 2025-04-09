# 🚀 FastAPI SQL Server Project

Backend project built with **FastAPI** in Python, using a clean modular architecture and connected to **SQL Server**.  
Designed to be maintainable, scalable, and ready for production.

---

## 🧱 Tech Stack

- 🐍 Python 3.13
- ⚡ FastAPI
- 🛢️ SQLAlchemy + Alembic
- 🧮 SQL Server (via `pyodbc`)
- 🔐 Pydantic v2
- 🔄 JWT Authentication (coming soon)
- 🧪 Uvicorn (development server)

---

## 📁 Project Structure

```
app/
├── main.py                # App entry point
├── config.py              # Environment & DB settings
├── database.py            # DB connection setup
├── models/                # SQLAlchemy models
├── schemas/               # Pydantic schemas (validation)
├── repositories/          # Data access layer
├── services/              # Business logic
├── routers/               # FastAPI route definitions
└── utils/                 # JWT, security, and helpers
```

---

## ⚙️ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your_user/fastapi-project.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create your `.env` file:
   ```env
   database_hostname=localhost
   database_port=1433
   database_username=your_user
   database_password=your_password
   database_name=FastApiDB

   secret_key=YourSuperSecretKey
   algorithm=HS256
   access_token_expire_minutes=30
   ```

5. Run Alembic migrations:
   ```bash
   alembic upgrade head
   ```

6. Launch the server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📡 Endpoints

- `/` — Health check  
- `/check-db` — Verifies connection with SQL Server  
- 🔐 Auth & CRUD endpoints coming soon...

---

## 🔜 Coming Soon

- JWT Authentication
- Role-based Permissions
- Unit & Integration Testing
- CI/CD & Production Deployment

---

## 👨‍💻 Author

> Built with ❤️ by **Javier Méndez** aka _jam300_  
> [GitHub](https://github.com/jam300) — [LinkedIn](https://www.linkedin.com/in/javieradanmendezmendez/)

---
