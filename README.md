# EquipTrack | Fleet & Maintenance Management System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-%2346E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

EquipTrack è un'applicazione backend production-ready sviluppata in Python/Django per ottimizzare la gestione delle flotte aziendali, tracciare gli interventi di manutenzione e monitorare l'inventario dei ricambi.

Progettato con un'architettura RESTful, il sistema espone API sicure e scalabili, dimostrando l'intero ciclo di vita dello sviluppo software: dalla modellazione del database relazionale fino al deploy in ambiente cloud.

🔗 **Live Demo:** [https://equiptrack-9mz7.onrender.com/](https://equiptrack-9mz7.onrender.com/)  
_Note: il caricamento iniziale potrebbe richiedere qualche secondo a causa del piano cloud gratuito._

## Technical Competencies Highlight

Questo progetto è stato sviluppato per dimostrare solidità nelle seguenti aree dell'ingegneria del software:

- **Backend Engineering**: sviluppo di logiche di business e architetture CRUD con Django
- **API Design**: progettazione e implementazione di API RESTful tramite Django REST Framework
- **Database Management**: modellazione relazionale e gestione delle migrazioni su PostgreSQL
- **Security & Authentication**: implementazione di autenticazione e autorizzazione per la protezione degli endpoint
- **DevOps & Cloud**: containerizzazione con Docker, gestione delle variabili d'ambiente e continuous deployment su Render con Gunicorn e WhiteNoise

## Tech Stack

| Categoria | Tecnologie Utilizzate |
|-----------|------------------------|
| Core & Framework | Python 3, Django, Django REST Framework |
| Database | PostgreSQL (produzione), SQLite (sviluppo locale) |
| Server & Static Files | Gunicorn, WhiteNoise |
| Infrastruttura & Deploy | Render, Docker |
| Version Control | Git, GitHub |

## Core Architecture & Features

Il codice segue i principi della separazione degli interessi (Separation of Concerns), mantenendo la logica di business disaccoppiata dalla configurazione di sistema.

### Funzionalità principali

- **Gestione Veicoli**: tracciamento dell'intero ciclo di vita della flotta aziendale
- **Registro Manutenzioni**: logging e programmazione degli interventi tecnici
- **Gestione Inventario**: monitoraggio dei ricambi e delle disponibilità
- **Admin Dashboard**: interfaccia Django Admin per la gestione rapida dei dati

### Architettura del repository

```text
📦 equipTrack-root
 ┣ 📂 equipTrack/      # Configurazione globale, WSGI/ASGI e routing principale
 ┣ 📂 manutenzioni/    # Core app: modelli ORM, viste, serializers e URL REST
 ┣ 📂 templates/       # Template HTML
 ┣ 📜 build.sh         # Script di build per automazione deploy
 ┣ 📜 Dockerfile       # Configurazione container
 ┗ 📜 requirements.txt # Dipendenze Python
```

## API Reference

Gli endpoint sono protetti da autenticazione e restituiscono risposte in formato JSON.

- `GET /api/veicoli/` — Recupera l'elenco dei veicoli
- `GET /api/interventi/` — Restituisce lo storico degli interventi tecnici
- `GET /api/ricambi/` — Mostra l'inventario dei ricambi

## Local Development Setup

### 1. Clona il repository

```bash
git clone https://github.com/bronx-l/equipTrack.git
cd equipTrack
```

### 2. Crea e attiva l'ambiente virtuale

```bash
# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

```bash
# Windows
.venv\Scripts\activate
```

### 3. Installa le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Configura le variabili d'ambiente

Crea un file `.env` nella root del progetto prendendo spunto dalla sezione seguente.

### 5. Applica le migrazioni e avvia il server

```bash
python manage.py migrate
python manage.py runserver
```

## Environment Variables

L'applicazione è progettata per usare configurazione tramite variabili d'ambiente.

```env
DJANGO_SECRET_KEY=your_secure_secret_key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=equiptrack-9mz7.onrender.com,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=https://equiptrack-9mz7.onrender.com
DATABASE_URL=postgres://user:password@host:port/dbname
```

## Roadmap

Per avvicinare ulteriormente il progetto a un prodotto enterprise-grade:

- **Automated Testing**: unit ed end-to-end testing con pytest
- **API Documentation**: integrazione Swagger/OpenAPI con drf-spectacular
- **Role-Based Access Control**: permessi granulari per ruoli differenti
- **Frontend Decoupled**: SPA in React o Next.js che consumi le API
- **Analytics & Dashboarding**: reportistica su costi di manutenzione e downtime

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author
l-bronx
Realizzato come progetto portfolio backend, con attenzione a deploy, sicurezza, pulizia architetturale e manutenibilità del codice.