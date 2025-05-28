from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime
from app.models.user import UserType

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    user_type: UserType

class UserCreate(UserBase):
    password: str
    university: Optional[str] = None
    student_id: Optional[str] = None
    major: Optional[str] = None
    graduation_year: Optional[int] = None
    interests: Optional[List[str]] = None
    business_name: Optional[str] = None
    business_type: Optional[str] = None
    location: Optional[Dict[str, float]] = None
    business_hours: Optional[Dict[str, str]] = None
    sponsorship_budget: Optional[int] = None

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    university: Optional[str] = None
    major: Optional[str] = None
    graduation_year: Optional[int] = None
    interests: Optional[List[str]] = None
    business_name: Optional[str] = None
    business_type: Optional[str] = None
    location: Optional[Dict[str, float]] = None
    business_hours: Optional[Dict[str, str]] = None
    sponsorship_budget: Optional[int] = None

class UserInDBBase(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[int] = None 