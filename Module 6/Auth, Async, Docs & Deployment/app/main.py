from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.database import engine, Base
from app.routes import users, auth  # <-- Import auth
from sqlalchemy.exc import SQLAlchemyError
import logging

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Module 6 CRUD API with Auth",
    description="Production-ready CRUD API with JWT authentication",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(users.router)
app.include_router(auth.router)  # <-- Add auth routes

# --- Global Error Handlers ---

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body
        }
    )

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logging.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal database error occurred"}
    )

# --- Health Check ---
@app.get("/health", tags=["system"])
async def health_check():
    return {
        "status": "healthy",
        "service": "Module 6 CRUD API",
        "database": "connected"  # Could verify connection here
    }

# --- Root ---
@app.get("/", tags=["system"])
async def root():
    return {
        "message": "Welcome to Module 6 CRUD API",
        "docs": "/docs",
        "health": "/health"
    }
