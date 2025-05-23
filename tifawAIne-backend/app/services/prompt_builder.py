"""
Service de construction de prompts dynamiques
"""
from typing import Dict, Any

class PromptBuilder:
    @staticmethod
    def build_agent_prompt(agent_type: str, context: Dict[str, Any]) -> str:
        """
        Construit un prompt personnalisé pour un agent spécifique
        """
        base_prompts = {
            "rh": "En tant qu'agent RH, analysez la situation suivante: {context}",
            "marketing": "En tant qu'agent Marketing, évaluez la stratégie suivante: {context}",
            "finance": "En tant qu'agent Finance, analysez les données financières suivantes: {context}",
            "support": "En tant qu'agent Support, traitez la demande suivante: {context}"
        }
        
        return base_prompts.get(agent_type, "Analysez la situation suivante: {context}").format(context=context) 