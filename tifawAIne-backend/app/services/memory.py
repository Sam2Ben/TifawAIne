"""
Service de gestion de la mémoire des agents
"""
from typing import Dict, List, Any
import json
from datetime import datetime

class AgentMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict[str, Any]]] = {}
    
    def add_interaction(self, agent_id: str, interaction: Dict[str, Any]):
        if agent_id not in self.memory:
            self.memory[agent_id] = []
        
        interaction["timestamp"] = datetime.now().isoformat()
        self.memory[agent_id].append(interaction)
    
    def get_agent_history(self, agent_id: str) -> List[Dict[str, Any]]:
        return self.memory.get(agent_id, [])
    
    def clear_agent_memory(self, agent_id: str):
        if agent_id in self.memory:
            self.memory[agent_id] = [] 