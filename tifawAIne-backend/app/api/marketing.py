"""
Routes API pour les fonctionnalités Marketing
"""
from fastapi import APIRouter

router = APIRouter(prefix="/marketing", tags=["Marketing"])

@router.get("/")
async def get_marketing_status():
    return {"status": "Marketing API is running"} 