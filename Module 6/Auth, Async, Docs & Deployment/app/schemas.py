from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

# --- Base Schemas (shared) ---
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=150)

# --- Create (POST) ---
class UserCreate(UserBase):
    password: str = Field(min_length=8)  # For registration

# --- Update (PUT/PATCH) ---
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: Optional[bool] = None

# --- Response (GET) ---
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2

# --- List Response (Paginated) ---
class UsersListResponse(BaseModel):
    total: int
    items: list[UserResponse]
    page: int
    size: int

# --- Authentication Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=150)
    password: str = Field(min_length=8)
