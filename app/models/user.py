from sqlalchemy import Column, String, Boolean, JSON, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.db.base import BaseModel

class UserType(str, enum.Enum):
    STUDENT = "student"
    BUSINESS = "business"
    ADMIN = "admin"

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    user_type = Column(Enum(UserType), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # Student-specific fields
    university = Column(String)
    student_id = Column(String, unique=True)
    major = Column(String)
    graduation_year = Column(Integer)
    interests = Column(JSON)  # List of interests/preferences
    parking_history = Column(JSON)  # List of parking sessions
    
    # Business-specific fields
    business_name = Column(String)
    business_type = Column(String)
    location = Column(JSON)  # {latitude: float, longitude: float}
    business_hours = Column(JSON)
    sponsorship_budget = Column(Integer)  # Monthly budget in cents
    
    # Relationships
    parking_sessions = relationship("ParkingSession", back_populates="user")
    business_sponsorships = relationship("BusinessSponsorship", back_populates="business")
    
    def __repr__(self):
        return f"<User {self.email}>" 