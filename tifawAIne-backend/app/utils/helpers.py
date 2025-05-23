"""
Fonctions utilitaires pour l'application
"""
import logging
from typing import Any, Dict
import json
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def format_response(data: Any) -> Dict:
    """
    Formate la réponse de l'API
    """
    return {
        "data": data,
        "timestamp": datetime.now().isoformat()
    }

def log_agent_interaction(agent_id: str, action: str, details: Dict):
    """
    Journalise les interactions des agents
    """
    logger.info(f"Agent {agent_id} - {action}: {json.dumps(details)}") 