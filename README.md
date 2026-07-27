# EquipTrack
Backend portfolio project built with Django, DRF, PostgreSQL and Render.
EquipTrack è una web app sviluppata con Django per gestire veicoli, interventi di manutenzione e ricambi.  
Il progetto include autenticazione, pannello admin, API REST e deploy pubblico in produzione.

## Live Demo

Applicazione online: https://equiptrack-9mz7.onrender.com/

## Obiettivo del progetto

Questo progetto è stato realizzato come portfolio backend per mostrare competenze pratiche su:

- sviluppo web con Django
- progettazione di modelli relazionali
- creazione di API REST con Django REST Framework
- autenticazione e autorizzazione
- configurazione ambiente di produzione
- deploy su Render

## Funzionalità principali

- Gestione dei veicoli
- Gestione degli interventi di manutenzione
- Gestione dei ricambi
- Accesso autenticato alle funzionalità applicative
- Django Admin per la gestione rapida dei dati
- API REST per veicoli, interventi e ricambi
- Deploy in produzione con Gunicorn e WhiteNoise

## Stack tecnologico

| Area | Tecnologie |
|------|------------|
| Backend | Python, Django |
| API | Django REST Framework |
| Database | PostgreSQL / SQLite in locale |
| Deploy | Render |
| Web server | Gunicorn |
| Static files | WhiteNoise |
| Containerizzazione | Docker |

## Architettura del progetto

L'applicazione segue una struttura classica Django con separazione tra configurazione base e configurazione di produzione.  
La logica principale è organizzata nell'app `manutenzioni`, mentre la configurazione globale del progetto è contenuta nel package `equipTrack`.

### Componenti principali

- `equipTrack/` → configurazione del progetto
- `manutenzioni/` → modelli, viste, serializer, URL e logica applicativa
- `templates/` → template HTML
- `build.sh` → script di build per il deploy
- `requirements.txt` → dipendenze Python
- `Dockerfile` → configurazione container

## API disponibili

Gli endpoint REST principali sono:

- `/api/veicoli/`
- `/api/interventi/`
- `/api/ricambi/`

L’accesso alle API è protetto tramite autenticazione utente.

## Avvio in locale

### 1. Clonare il repository

```bash
git clone <https://github.com/bronx-l/equipTrack>
cd <equipTrack>
```

### 2. Creare e attivare l’ambiente virtuale

```bash
python -m venv .venv
source .venv/bin/activate
```

Su Windows:

```bash
.venv\Scripts\activate
```

### 3. Installare le dipendenze

```bash
pip install -r requirements.txt
```

### 4. Applicare le migrazioni

```bash
python manage.py migrate
```

### 5. Avviare il server di sviluppo

```bash
python manage.py runserver
```

## Variabili ambiente principali

Per la configurazione di produzione vengono usate variabili ambiente come:

```env
DJANGO_SECRET_KEY=
DJANGO_DEBUG=
DJANGO_ALLOWED_HOSTS=
DJANGO_CSRF_TRUSTED_ORIGINS=
DATABASE_URL=
```

## Deploy

L’applicazione è deployata su Render con configurazione production dedicata.  
Il progetto usa Gunicorn come application server e WhiteNoise per servire i file statici in produzione.

## Competenze dimostrate

Questo progetto mostra esperienza pratica in:

- sviluppo CRUD con Django
- progettazione database relazionale
- uso di Django REST Framework
- configurazione sicurezza base per produzione
- gestione variabili ambiente
- troubleshooting di deploy
- pubblicazione di un’app online funzionante

## Possibili sviluppi futuri

- Dashboard con statistiche sugli interventi
- Filtri avanzati su veicoli e manutenzioni
- Gestione ruoli utente più granulare
- Test automatici backend
- Documentazione API più completa
- Frontend separato con React o Next.js

## Autore

Progetto realizzato come esercizio portfolio per consolidare competenze backend con Django e deploy cloud.