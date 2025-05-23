"""
Routes API pour les fonctionnalités Support
"""
from fastapi import APIRouter

router = APIRouter(prefix="/support", tags=["Support"])

@router.get("/")
async def get_support_status():
    return {"status": "Support API is running"} 