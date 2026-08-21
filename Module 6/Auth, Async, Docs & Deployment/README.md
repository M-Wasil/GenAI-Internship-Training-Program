# FastAPI CRUD API with JWT Authentication

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black.svg?logo=vercel&logoColor=white)](https://fast-api-crud-auth-api.vercel.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A production-ready RESTful API built with **FastAPI**, **SQLAlchemy ORM**, **Pydantic v2**, and **JWT Authentication** (OAuth2 with Bearer token & bcrypt). Fully deployed on **Vercel Serverless Functions**.

---

## 🌐 Live Deliverable & Interactive Docs

- 🚀 **Deployed API URL**: [https://fast-api-crud-auth-api.vercel.app](https://fast-api-crud-auth-api.vercel.app)
- 📖 **Interactive Swagger UI**: [https://fast-api-crud-auth-api.vercel.app/docs](https://fast-api-crud-auth-api.vercel.app/docs)
- 📚 **ReDoc Documentation**: [https://fast-api-crud-auth-api.vercel.app/redoc](https://fast-api-crud-auth-api.vercel.app/redoc)
- 🩺 **Health Check**: [https://fast-api-crud-auth-api.vercel.app/health](https://fast-api-crud-auth-api.vercel.app/health)

---

## 🚀 Key Features

- **🔐 Robust Authentication**: OAuth2 Password Flow with JWT access tokens and secure `bcrypt` password hashing.
- **⚡ High-Performance CRUD**: Full Create, Read, Update, and Soft/Hard Delete operations.
- **🔍 Search & Pagination**: Query users by email or username substring with configurable pagination (`skip`, `limit`).
- **🛡️ Data Validation**: Powered by Pydantic v2 schemas for strict type safety and detailed validation errors.
- **💾 Database Agnostic**: Compatible with SQLite and PostgreSQL (e.g., Neon, Supabase) via SQLAlchemy ORM.
- **🌐 CORS Enabled**: Cross-Origin Resource Sharing configured for frontend clients.
- **☁️ Serverless Ready**: Configured with `api/index.py` and `vercel.json` for one-click Vercel deployments.

---

## 📋 API Endpoints

### 🩺 System
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:-------------:|
| `GET` | `/` | API Welcome message & endpoint directory | ❌ |
| `GET` | `/health` | Health check & service status | ❌ |

### 🔐 Authentication (`/api/v1/auth`)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:-------------:|
| `POST` | `/api/v1/auth/register` | Register a new user | ❌ |
| `POST` | `/api/v1/auth/token` | Login with username/email & password to get JWT token | ❌ |
| `GET` | `/api/v1/auth/me` | Get the currently authenticated user's profile | ✅ Bearer Token |

### 👥 Users CRUD (`/api/v1/users`)
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:-------------:|
| `POST` | `/api/v1/users/` | Create a new user | ✅ Bearer Token |
| `GET` | `/api/v1/users/` | Get paginated list of active users | ✅ Bearer Token |
| `GET` | `/api/v1/users/{id}` | Get user details by ID | ✅ Bearer Token |
| `PUT` | `/api/v1/users/{id}` | Full update of user details | ✅ Bearer Token |
| `PATCH` | `/api/v1/users/{id}` | Partial update of user details | ✅ Bearer Token |
| `DELETE` | `/api/v1/users/{id}` | Soft delete user (`is_active = False`) | ✅ Bearer Token |
| `DELETE` | `/api/v1/users/{id}/permanent` | Hard delete user from database | ✅ Bearer Token |
| `GET` | `/api/v1/users/search/` | Search users by query (`?query=...`) | ✅ Bearer Token |
| `GET` | `/api/v1/users/me` | Get current user info | ✅ Bearer Token |
| `PATCH` | `/api/v1/users/me` | Update current user info | ✅ Bearer Token |
| `DELETE` | `/api/v1/users/me` | Soft delete own account | ✅ Bearer Token |

---

## 📁 Project Structure

```text
├── api/
│   └── index.py            # Vercel Serverless Function entrypoint
├── app/
│   ├── __init__.py
│   ├── auth.py             # JWT token handling & bcrypt password hashing
│   ├── crud.py             # Database CRUD logic & queries
│   ├── database.py         # SQLAlchemy engine & session management
│   ├── main.py             # FastAPI app initialization & CORS middleware
│   ├── models.py           # SQLAlchemy database models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py         # Authentication routes (/register, /token, /me)
│   │   └── users.py        # User CRUD & search endpoints
│   └── schemas.py          # Pydantic request/response models
├── test_client.py          # Automated client test suite for local & cloud APIs
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel routing and runtime configuration
├── .env.example            # Environment variables template
├── .gitignore
└── README.md
```

---

## 🛠️ Local Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/M-Wasil/FastAPI-CRUD-Auth-API.git
cd FastAPI-CRUD-Auth-API
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Set your `SECRET_KEY` and optional `DATABASE_URL`.

### 5. Run the development server
```bash
uvicorn app.main:app --reload
```
API will be live at `http://localhost:8000`. Interactive docs available at `http://localhost:8000/docs`.

---

## 🧪 Testing with the Python Client

The included `test_client.py` performs an end-to-end test suite (Registration -> Token -> Profile -> CRUD -> Search -> Update).

### Test against Local Server:
```bash
python test_client.py http://localhost:8000
```

### Test against Live Deployed Vercel API:
```bash
python test_client.py https://fast-api-crud-auth-api.vercel.app
```

---

## ☁️ Deployment on Vercel

1. Push your repository to GitHub.
2. Log in to [Vercel](https://vercel.com) and click **"Add New..."** ➔ **"Project"**.
3. Import your `FastAPI-CRUD-Auth-API` repository.
4. Set Environment Variables:
   - `SECRET_KEY`: `your-random-production-secret-key`
   - *(Optional)* `DATABASE_URL`: `postgresql://user:password@host/dbname`
5. Click **Deploy**.
