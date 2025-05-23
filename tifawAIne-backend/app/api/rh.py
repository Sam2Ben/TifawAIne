"""
Routes API pour les fonctionnalités RH
"""
from fastapi import APIRouter

router = APIRouter(prefix="/rh", tags=["RH"])

@router.get("/")
async def get_rh_status():
    return {"status": "RH API is running"} 