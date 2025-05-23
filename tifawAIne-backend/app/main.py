"""
Point d'entrée principal de l'application FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import rh, marketing, finance, support

app = FastAPI(
    title="TifawAIne Backend",
    description="Backend intelligent pour TifawAIne",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routers
app.include_router(rh.router)
app.include_router(marketing.router)
app.include_router(finance.router)
app.include_router(support.router)

@app.get("/")
async def root():
    return {
        "message": "Bienvenue sur l'API TifawAIne",
        "status": "online",
        "version": "1.0.0"
    } 