from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from app.models.parking import ParkingStatus

class ParkingSessionBase(BaseModel):
    parking_lot_id: int
    start_time: datetime
    end_time: datetime

class ParkingSessionCreate(ParkingSessionBase):
    pass

class ParkingSessionUpdate(BaseModel):
    status: Optional[ParkingStatus] = None
    business_visit_time: Optional[datetime] = None
    business_visit_status: Optional[str] = None
    visit_feedback: Optional[Dict[str, Any]] = None

class ParkingSessionInDBBase(ParkingSessionBase):
    id: int
    user_id: int
    business_sponsor_id: Optional[int] = None
    status: ParkingStatus
    original_cost: Optional[int] = None
    sponsored_amount: Optional[int] = None
    final_cost: Optional[int] = None
    business_visit_time: Optional[datetime] = None
    business_visit_status: Optional[str] = None
    visit_feedback: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ParkingSession(ParkingSessionInDBBase):
    pass

class ParkingLotBase(BaseModel):
    name: str
    location: Dict[str, float]
    total_spaces: int
    hourly_rate: int
    university_id: Optional[int] = None

class ParkingLotCreate(ParkingLotBase):
    description: Optional[str] = None
    amenities: Optional[Dict[str, Any]] = None
    operating_hours: Optional[Dict[str, str]] = None

class ParkingLotUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[Dict[str, float]] = None
    total_spaces: Optional[int] = None
    hourly_rate: Optional[int] = None
    description: Optional[str] = None
    amenities: Optional[Dict[str, Any]] = None
    operating_hours: Optional[Dict[str, str]] = None

class ParkingLotInDBBase(ParkingLotBase):
    id: int
    description: Optional[str] = None
    amenities: Optional[Dict[str, Any]] = None
    operating_hours: Optional[Dict[str, str]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ParkingLot(ParkingLotInDBBase):
    pass 