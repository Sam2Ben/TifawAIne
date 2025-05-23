"""
Agent Support - Support client et assistance
"""
from crewai import Agent

class SupportAgent:
    def __init__(self):
        self.agent = Agent(
            role='Agent Support',
            goal='Fournir un support client efficace et personnalisé',
            backstory='Expert en support client et résolution de problèmes'
        ) 