from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas
from fastapi import HTTPException, status
from passlib.context import CryptContext  # For password hashing

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- CREATE ---
def create_user(db: Session, user: schemas.UserCreate):
    # Check if email or username exists
    db_user = db.query(models.User).filter(
        (models.User.email == user.email) | 
        (models.User.username == user.username)
    ).first()
    
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )
    
    # Hash password
    hashed_password = pwd_context.hash(user.password)
    
    db_user = models.User(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        age=user.age,
        # password would be stored in a separate table or hashed field
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- READ (All) ---
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).filter(
        models.User.is_active == True
    ).offset(skip).limit(limit).all()

# --- READ (One) ---
def get_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# --- UPDATE ---
def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = get_user(db, user_id)  # Reuse get_user for not found check
    
    update_data = user_update.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

# --- DELETE ---
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)  # Reuse get_user for not found check
    
    # Soft delete (recommended)
    db_user.is_active = False
    db.commit()
    return {"message": "User deleted successfully"}
    
    # Hard delete (uncomment if needed)
    # db.delete(db_user)
    # db.commit()
    # return {"message": "User permanently deleted"}

# --- COUNT ---
def count_users(db: Session):
    return db.query(models.User).filter(models.User.is_active == True).count()
