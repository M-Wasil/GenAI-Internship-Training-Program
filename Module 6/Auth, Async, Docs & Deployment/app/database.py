from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

# Database URL configuration
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # If running in Vercel serverless environment, store sqlite db in /tmp
    if os.getenv("VERCEL"):
        DATABASE_URL = "sqlite:////tmp/app.db"
    else:
        DATABASE_URL = "sqlite:///./app.db"
elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# get_db() function remains exactly the same
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
