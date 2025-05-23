"""
Agent Finance - Analyse financière et gestion budgétaire
"""
from crewai import Agent

class FinanceAgent:
    def __init__(self):
        self.agent = Agent(
            role='Agent Finance',
            goal='Optimiser la gestion financière et l\'analyse budgétaire',
            backstory='Expert en finance et analyse financière'
        ) 