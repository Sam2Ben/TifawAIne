# TifawAIne Backend

Backend intelligent pour TifawAIne, utilisant FastAPI et CrewAI pour orchestrer des agents IA spécialisés.

## 🚀 Technologies

- Python 3.10.13
- FastAPI 0.110.2
- CrewAI 0.20.2
- Google Gemini AI
- Supabase (PostgreSQL)
- ChromaDB (Vector Database)

## 📋 Prérequis

- Python 3.10.13 ou supérieur
- pip (gestionnaire de paquets Python)
- Clé API Google Gemini
- Compte Supabase

## 🔧 Installation

1. Cloner le repository
```bash
git clone [URL_DU_REPO]
cd tifawAIne-backend
```

2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer les variables d'environnement
- Copier `.env.example` vers `.env`
- Remplir les variables d'environnement nécessaires

## 🏃‍♂️ Démarrage

```bash
uvicorn app.main:app --reload
```

Le serveur sera accessible à l'adresse : http://localhost:8000

## 📚 Documentation API

La documentation Swagger est disponible à : http://localhost:8000/docs

## 🧪 Tests

```bash
pytest
```

## 📁 Structure du Projet

```
tifawAIne-backend/
│
├── .env                         # Variables d'environnement
├── requirements.txt             # Dépendances Python
├── README.md                    # Ce fichier
│
├── app/                         # Code source principal
│   ├── main.py                  # Point d'entrée FastAPI
│   ├── api/                     # Routes API
│   ├── agents/                  # Agents IA
│   ├── orchestrator/            # Orchestration des agents
│   ├── models/                  # Modèles Pydantic
│   ├── services/                # Services métier
│   └── utils/                   # Utilitaires
│
├── data/                        # Données
│   └── cv_samples/             # Exemples de CV
│
└── docs/                        # Documentation
```

## 📝 Licence

[À DÉFINIR]

## 👥 Auteurs

[À DÉFINIR] 