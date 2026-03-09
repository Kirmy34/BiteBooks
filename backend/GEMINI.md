# BiteBooks Backend Context

This directory contains the Django-based backend API for the BiteBooks project.

## Technology Stack
- **Framework:** Django 6.0.2
- **API:** Django REST Framework (DRF)
- **Auth:** DRF Simple JWT
- **Database:** PostgreSQL 16
- **Environment:** `python-dotenv` for configuration

## Directory Structure
- `config/`: Core project settings, WSGI/ASGI, and root URL routing.
- `manage.py`: Django administrative CLI.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Production and development container definition.

## Local Development (No Docker)
1. Ensure Python 3.10+ is installed.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it: `source venv/bin/activate` (Linux) or `venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.
5. Run migrations: `python manage.py migrate`.
6. Start server: `python manage.py runserver`.

## Backend Conventions
- **API Design:** Use DRF's Class-Based Views (CBVs) and Serializers.
- **Settings:** Environment-specific settings must be loaded from `.env` via the `config.settings` module.
- **Auth:** All protected endpoints should use `IsAuthenticated` permission and JWT authentication.
- **Database:** Always use Django Migrations for schema changes.
