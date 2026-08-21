from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app import schemas, crud, models
from app.database import get_db
from app.auth import get_current_active_user

router = APIRouter(prefix="/api/v1/users", tags=["users"])

# --- CREATE (Protected) ---
@router.post(
    "/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user"
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Create a new user with email, username, and password.
    
    - **email**: Valid email address
    - **username**: 3-50 characters
    - **full_name**: Optional full name
    - **age**: Optional age between 0-150
    - **password**: Minimum 8 characters
    """
    return crud.create_user(db, user)

# --- READ ALL (Protected with Pagination) ---
@router.get(
    "/",
    response_model=schemas.UsersListResponse,
    summary="Get all users with pagination"
)
def get_users(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Max records to return"),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Get paginated list of active users.
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Max records to return (default: 100, max: 1000)
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    total = crud.count_users(db)
    
    return schemas.UsersListResponse(
        total=total,
        items=users,
        page=skip // limit + 1 if limit > 0 else 1,
        size=limit
    )

# --- READ ONE (Protected) ---
@router.get(
    "/{user_id}",
    response_model=schemas.UserResponse,
    summary="Get user by ID"
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Get a single user by their ID.
    
    - **user_id**: The ID of the user to retrieve
    """
    return crud.get_user(db, user_id)

# --- UPDATE (Protected - Full Update) ---
@router.put(
    "/{user_id}",
    response_model=schemas.UserResponse,
    summary="Fully update user"
)
def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Fully update user details (all fields required).
    
    - **user_id**: The ID of the user to update
    - **email**: Valid email address (optional)
    - **username**: 3-50 characters (optional)
    - **full_name**: Full name (optional)
    - **age**: Age between 0-150 (optional)
    - **is_active**: Active status (optional)
    """
    return crud.update_user(db, user_id, user_update)

# --- PARTIAL UPDATE (Protected) ---
@router.patch(
    "/{user_id}",
    response_model=schemas.UserResponse,
    summary="Partially update user"
)
def patch_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Partially update user (only provided fields will be updated).
    
    - **user_id**: The ID of the user to update
    - Any subset of fields can be provided
    """
    return crud.update_user(db, user_id, user_update)

# --- DELETE (Protected - Soft Delete) ---
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user (soft delete)"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Soft delete a user (set is_active=False).
    
    - **user_id**: The ID of the user to delete
    - The user can be restored by updating is_active=True
    """
    crud.delete_user(db, user_id)
    return None  # 204 No Content

# --- HARD DELETE (Protected - Optional) ---
@router.delete(
    "/{user_id}/permanent",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Permanently delete user"
)
def hard_delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Permanently delete a user from the database.
    
    - **user_id**: The ID of the user to delete
    - **Warning**: This action cannot be undone!
    """
    # Check if user exists
    db_user = crud.get_user(db, user_id)
    
    # Optional: Only allow admins to hard delete
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=403, detail="Only admins can permanently delete users")
    
    db.delete(db_user)
    db.commit()
    return None  # 204 No Content

# --- GET CURRENT USER (Protected) ---
@router.get(
    "/me",
    response_model=schemas.UserResponse,
    summary="Get current authenticated user"
)
def get_current_user_info(
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Get the currently authenticated user's information.
    """
    return current_user

# --- UPDATE CURRENT USER (Protected) ---
@router.patch(
    "/me",
    response_model=schemas.UserResponse,
    summary="Update current user"
)
def update_current_user(
    user_update: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Update the currently authenticated user's information.
    
    - Any subset of fields can be provided
    """
    return crud.update_user(db, current_user.id, user_update)

# --- DELETE CURRENT USER (Protected) ---
@router.delete(
    "/me",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete current user"
)
def delete_current_user(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Delete the currently authenticated user (soft delete).
    """
    crud.delete_user(db, current_user.id)
    return None  # 204 No Content

# --- SEARCH USERS (Protected) ---
@router.get(
    "/search/",
    response_model=schemas.UsersListResponse,
    summary="Search users by email or username"
)
def search_users(
    query: str = Query(..., min_length=2, description="Search query (email or username)"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Max records to return"),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    """
    Search for users by email or username (partial match).
    
    - **query**: Search term (minimum 2 characters)
    - **skip**: Number of records to skip
    - **limit**: Max records to return
    """
    # Add search logic to crud.py if needed
    # For now, we'll use the existing get_users and filter in Python
    # But ideally, you'd implement this in the database query
    
    users = db.query(models.User).filter(
        (models.User.email.contains(query)) | 
        (models.User.username.contains(query))
    ).filter(
        models.User.is_active == True
    ).offset(skip).limit(limit).all()
    
    total = db.query(models.User).filter(
        (models.User.email.contains(query)) | 
        (models.User.username.contains(query))
    ).filter(
        models.User.is_active == True
    ).count()
    
    return schemas.UsersListResponse(
        total=total,
        items=users,
        page=skip // limit + 1 if limit > 0 else 1,
        size=limit
    )
