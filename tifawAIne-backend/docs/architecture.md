# Architecture TifawAIne Backend

## Vue d'ensemble

TifawAIne Backend est une application FastAPI qui utilise CrewAI pour orchestrer des agents IA spécialisés. L'architecture est conçue pour être modulaire, extensible et maintenable.

## Composants principaux

### 1. API Layer (app/api/)
- Routes FastAPI pour chaque domaine fonctionnel
- Gestion des requêtes HTTP
- Validation des entrées/sorties

### 2. Agents Layer (app/agents/)
- Implémentation des agents IA spécialisés
- Chaque agent a un rôle et des compétences spécifiques
- Utilisation de CrewAI pour la gestion des agents

### 3. Orchestrator (app/orchestrator/)
- Coordination des agents
- Gestion des workflows
- Distribution des tâches

### 4. Services (app/services/)
- Services d'IA (Gemini LLM)
- Construction de prompts
- Gestion de la mémoire des agents

### 5. Models (app/models/)
- Modèles Pydantic pour la validation
- Schémas de données
- Types personnalisés

### 6. Utils (app/utils/)
- Fonctions utilitaires
- Logging
- Formatage des réponses

## Flux de données

1. Requête HTTP → API Layer
2. Validation des données → Models
3. Traitement → Services
4. Orchestration → Orchestrator
5. Exécution → Agents
6. Réponse → API Layer

## Sécurité

- Authentification via JWT
- Validation des entrées
- Gestion des CORS
- Variables d'environnement

## Base de données

- Supabase (PostgreSQL)
- Stockage vectoriel pour RAG
- Gestion des sessions

## Déploiement

- Conteneurisation avec Docker
- CI/CD avec GitHub Actions
- Monitoring avec Prometheus/Grafana

## Extensions futures

- Support de LangGraph pour workflows complexes
- Intégration de nouveaux modèles LLM
- Système de cache distribué
- Monitoring avancé des agents 