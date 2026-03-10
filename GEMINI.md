# BiteBooks: Context & Instructions

BiteBooks is a full-stack digital cookbook application designed for managing and organizing recipes. This file provides architectural context and development guidelines for the project.

## Project Overview

*   **Goal:** A personal cookbook web application (BiteBooks) for adding, viewing, searching, and organizing recipes.
*   **Architecture:** Decoupled full-stack application with a Django REST API backend and a Vue.js frontend.
*   **Backend Tech Stack:**
    *   **Framework:** Django 6.0.2 with Django REST Framework (DRF).
    *   **Authentication:** Simple JWT (JSON Web Tokens).
    *   **Database:** PostgreSQL 16.
    *   **Tools:** `python-dotenv` for environment management, `django-cors-headers` for frontend-backend communication.
*   **Frontend Tech Stack:**
    *   **Framework:** Vue 3 (Composition API).
    *   **Build Tool:** Vite + TypeScript.
    *   **Styling:** Tailwind CSS 4.x.
*   **Environment:**
    *   Development uses Docker/Devcontainers with a dedicated PostgreSQL service.

## Directory Structure

*   `backend/`: Django project root.
    *   `config/`: Main Django settings and URL configurations.
    *   `manage.py`: Django management CLI.
    *   `requirements.txt`: Python dependencies.
*   `frontend/`: Vue.js project root.
    *   `src/`: Application source code (Vue components, assets, etc.).
    *   `package.json`: NPM dependencies and scripts.
*   `.devcontainer/`: Configuration for the VS Code development container.

## Building and Running

### Development Setup (Docker)

The project is pre-configured to run in a Devcontainer. Upon opening the workspace in VS Code (with Remote Containers extension):
1.  The `db` service (Postgres) will start automatically.
2.  Python and Node dependencies are installed via `postCreateCommand`.

### Manual Commands

*   **Backend Server:**
    ```bash
    cd backend
    python manage.py runserver
    ```
*   **Frontend Server:**
    ```bash
    cd frontend
    npm run dev
    ```
*   **Database Migrations:**
    ```bash
    cd backend
    python manage.py makemigrations
    python manage.py migrate
    ```

## Development Conventions

*   **API Design:** Use Django REST Framework (DRF) with Class-Based Views (CBVs) or ViewSets.
*   **Styling:** Prefer Tailwind CSS utility classes in Vue components. Use `style.css` only for global overrides.
*   **Environment Variables:** All sensitive configurations (DB credentials, Secret Keys) should be stored in the root `.env` file and accessed via `os.environ` or `dotenv`.
*   **Testing:**
    *   Backend: Use Django's built-in test framework (`python manage.py test`).
    *   Frontend: (Placeholder) Setup Vitest for unit testing components.
