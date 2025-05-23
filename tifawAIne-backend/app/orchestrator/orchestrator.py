"""
Orchestrateur central pour la gestion des agents
"""
from crewai import Crew
from typing import List, Dict, Any
from ..agents.rh_agent import RHAgent
from ..agents.marketing_agent import MarketingAgent
from ..agents.finance_agent import FinanceAgent
from ..agents.support_agent import SupportAgent

class AgentOrchestrator:
    def __init__(self):
        self.agents = {
            "rh": RHAgent(),
            "marketing": MarketingAgent(),
            "finance": FinanceAgent(),
            "support": SupportAgent()
        }
    
    def create_crew(self, task: str, required_agents: List[str]) -> Crew:
        """
        Crée une équipe d'agents pour une tâche spécifique
        """
        selected_agents = [self.agents[agent_type].agent for agent_type in required_agents]
        return Crew(
            agents=selected_agents,
            tasks=[task],
            verbose=True
        )
    
    async def execute_task(self, task: str, required_agents: List[str]) -> Dict[str, Any]:
        """
        Exécute une tâche avec les agents spécifiés
        """
        crew = self.create_crew(task, required_agents)
        result = await crew.kickoff()
        return {"result": result} 