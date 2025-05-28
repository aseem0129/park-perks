from fastapi import APIRouter
from app.api.v1.endpoints import auth, parking

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(parking.router, prefix="/parking", tags=["parking"]) 