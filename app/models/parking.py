from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON, Enum
from sqlalchemy.orm import relationship
import enum
from app.db.base import BaseModel

class ParkingStatus(str, enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class ParkingSession(BaseModel):
    __tablename__ = "parking_sessions"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    parking_lot_id = Column(Integer, ForeignKey("parking_lots.id"), nullable=False)
    business_sponsor_id = Column(Integer, ForeignKey("business_sponsorships.id"))
    
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(Enum(ParkingStatus), default=ParkingStatus.PENDING)
    
    # Payment and sponsorship details
    original_cost = Column(Integer)  # Cost in cents
    sponsored_amount = Column(Integer)  # Amount sponsored in cents
    final_cost = Column(Integer)  # Final cost after sponsorship
    
    # Business visit tracking
    business_visit_time = Column(DateTime)
    business_visit_status = Column(String)  # "visited", "not_visited", "pending"
    visit_feedback = Column(JSON)  # User feedback about the visit
    
    # Relationships
    user = relationship("User", back_populates="parking_sessions")
    parking_lot = relationship("ParkingLot")
    business_sponsorship = relationship("BusinessSponsorship", back_populates="parking_sessions")
    
    def __repr__(self):
        return f"<ParkingSession {self.id} - {self.status}>"

class ParkingLot(BaseModel):
    __tablename__ = "parking_lots"
    
    name = Column(String, nullable=False)
    location = Column(JSON, nullable=False)  # {latitude: float, longitude: float}
    total_spaces = Column(Integer)
    hourly_rate = Column(Integer)  # Rate in cents
    university_id = Column(Integer, ForeignKey("universities.id"))
    
    # Additional details
    description = Column(String)
    amenities = Column(JSON)  # List of available amenities
    operating_hours = Column(JSON)  # Operating hours for each day
    
    def __repr__(self):
        return f"<ParkingLot {self.name}>"

class BusinessSponsorship(BaseModel):
    __tablename__ = "business_sponsorships"
    
    business_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    campaign_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    
    # Campaign settings
    daily_budget = Column(Integer)  # Daily budget in cents
    max_sponsored_hours = Column(Integer)
    target_audience = Column(JSON)  # Targeting criteria
    promotion_details = Column(JSON)  # Promotion details and requirements
    
    # Campaign metrics
    total_spent = Column(Integer, default=0)  # Total spent in cents
    total_impressions = Column(Integer, default=0)
    total_visits = Column(Integer, default=0)
    
    # Relationships
    business = relationship("User", back_populates="business_sponsorships")
    parking_sessions = relationship("ParkingSession", back_populates="business_sponsorship")
    
    def __repr__(self):
        return f"<BusinessSponsorship {self.campaign_name}>" 