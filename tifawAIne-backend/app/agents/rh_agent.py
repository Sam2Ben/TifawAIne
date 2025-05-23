"""
Agent RH - Gestion des ressources humaines
"""
from crewai import Agent

class RHAgent:
    def __init__(self):
        self.agent = Agent(
            role='Agent RH',
            goal='Optimiser la gestion des ressources humaines',
            backstory='Expert en ressources humaines avec une forte expérience en recrutement et gestion de carrière'
        ) 