# EquipTrack
# EquipTrack

[![Django Tests](https://github.com/TUO_USERNAME/TUO_REPO/actions/workflows/django-tests.yml/badge.svg)](https://github.com/TUO_USERNAME/TUO_REPO/actions/workflows/django-tests.yml)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![DRF](https://img.shields.io/badge/DRF-API-red)
![Status](https://img.shields.io/badge/status-in%20development-orange)
EquipTrack è una web application sviluppata con Django per gestire la manutenzione di veicoli, camper e macchine agricole.

## Obiettivo del progetto

Questo progetto è stato sviluppato come portfolio backend per mostrare competenze su:
- Django
- Django REST Framework
- progettazione di modelli relazionali
- autenticazione e permessi
- testing con pytest
- CI con GitHub Actions
- deploy con Docker e PostgreSQL

## Funzionalità principali

- Gestione veicoli associati a un proprietario
- Storico interventi di manutenzione
- Gestione ricambi
- Accesso autenticato con ruoli utente
- API REST per veicoli, interventi e ricambi
- Test automatici su modelli e API

## Stack tecnologico

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Pytest
- GitHub Actions

## Avvio in locale

```bash
git clone <repo-url>
cd equiptrack
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Avvio con Docker

```bash
docker compose up --build
docker compose exec web python manage.py migrate
```

## Test

```bash
pytest -v
```

## Roadmap

- Migliorare dashboard veicoli e interventi
- Aggiungere reminder tagliandi
- Integrare JWT authentication
- Aggiungere upload documenti
- Deploy pubblico su Render

## Stato del progetto

Progetto in sviluppo attivo, con focus su qualità del codice, struttura pulita e presentazione portfolio.