"""
Modèles Pydantic pour les entrées/sorties API
"""
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class AgentRequest(BaseModel):
    task: str
    required_agents: List[str]
    context: Optional[Dict[str, Any]] = None

class AgentResponse(BaseModel):
    result: Any
    timestamp: datetime = datetime.now()
    agent_ids: List[str]

class ErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, Any]] = None 