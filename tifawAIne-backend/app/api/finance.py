"""
Routes API pour les fonctionnalités Finance
"""
from fastapi import APIRouter

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.get("/")
async def get_finance_status():
    return {"status": "Finance API is running"} 