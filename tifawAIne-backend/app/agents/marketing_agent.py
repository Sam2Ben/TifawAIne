"""
Agent Marketing - Stratégies marketing et analyse de marché
"""
from crewai import Agent

class MarketingAgent:
    def __init__(self):
        self.agent = Agent(
            role='Agent Marketing',
            goal='Développer et optimiser les stratégies marketing',
            backstory='Expert en marketing digital et analyse de marché'
        ) 