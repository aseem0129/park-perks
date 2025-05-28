from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.parking import ParkingSession as ParkingSessionModel, ParkingLot as ParkingLotModel, ParkingStatus
from app.schemas.parking import (
    ParkingSession,
    ParkingSessionCreate,
    ParkingSessionUpdate,
    ParkingLot,
    ParkingLotCreate,
    ParkingLotUpdate
)

router = APIRouter()

@router.post("/sessions", response_model=ParkingSession)
def create_parking_session(
    *,
    db: Session = Depends(get_db),
    session_in: ParkingSessionCreate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Create a new parking session.
    """
    # Verify parking lot exists
    parking_lot = db.query(ParkingLotModel).filter(ParkingLotModel.id == session_in.parking_lot_id).first()
    if not parking_lot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parking lot not found"
        )
    
    # Calculate cost
    duration = session_in.end_time - session_in.start_time
    hours = duration.total_seconds() / 3600
    original_cost = int(hours * parking_lot.hourly_rate)
    
    # Create parking session
    parking_session = ParkingSessionModel(
        user_id=current_user.id,
        parking_lot_id=session_in.parking_lot_id,
        start_time=session_in.start_time,
        end_time=session_in.end_time,
        status=ParkingStatus.PENDING,
        original_cost=original_cost,
        final_cost=original_cost  # Will be updated if sponsorship is found
    )
    
    db.add(parking_session)
    db.commit()
    db.refresh(parking_session)
    return parking_session

@router.get("/sessions", response_model=List[ParkingSession])
def get_parking_sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Get all parking sessions for the current user.
    """
    sessions = db.query(ParkingSessionModel)\
        .filter(ParkingSessionModel.user_id == current_user.id)\
        .offset(skip)\
        .limit(limit)\
        .all()
    return sessions

@router.get("/sessions/{session_id}", response_model=ParkingSession)
def get_parking_session(
    *,
    db: Session = Depends(get_db),
    session_id: int,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Get a specific parking session.
    """
    session = db.query(ParkingSessionModel)\
        .filter(ParkingSessionModel.id == session_id)\
        .filter(ParkingSessionModel.user_id == current_user.id)\
        .first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parking session not found"
        )
    return session

@router.put("/sessions/{session_id}", response_model=ParkingSession)
def update_parking_session(
    *,
    db: Session = Depends(get_db),
    session_id: int,
    session_in: ParkingSessionUpdate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Update a parking session.
    """
    session = db.query(ParkingSessionModel)\
        .filter(ParkingSessionModel.id == session_id)\
        .filter(ParkingSessionModel.user_id == current_user.id)\
        .first()
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parking session not found"
        )
    
    for field, value in session_in.dict(exclude_unset=True).items():
        setattr(session, field, value)
    
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@router.post("/lots", response_model=ParkingLot)
def create_parking_lot(
    *,
    db: Session = Depends(get_db),
    lot_in: ParkingLotCreate,
    current_user: User = Depends(get_current_user)
) -> Any:
    """
    Create a new parking lot (admin only).
    """
    if current_user.user_type != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    parking_lot = ParkingLotModel(**lot_in.dict())
    db.add(parking_lot)
    db.commit()
    db.refresh(parking_lot)
    return parking_lot

@router.get("/lots", response_model=List[ParkingLot])
def get_parking_lots(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Get all parking lots.
    """
    lots = db.query(ParkingLotModel).offset(skip).limit(limit).all()
    return lots

@router.get("/lots/{lot_id}", response_model=ParkingLot)
def get_parking_lot(
    *,
    db: Session = Depends(get_db),
    lot_id: int
) -> Any:
    """
    Get a specific parking lot.
    """
    lot = db.query(ParkingLotModel).filter(ParkingLotModel.id == lot_id).first()
    if not lot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parking lot not found"
        )
    return lot 