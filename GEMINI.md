# BiteBooks: Context & Instructions

BiteBooks is a full-stack digital cookbook application designed for managing and organizing recipes. This file provides architectural context and development guidelines for the project.

## ⚠️ Critical Command Execution Rule
*   **DO NOT** attempt to run `python`, `manage.py`, or `npm` commands directly using shell tools.
*   The agent is not running inside the devcontainer/environment where these tools are installed.
*   **ALWAYS** provide the specific command to the user and ask them to run it in their terminal.

## Project Overview

*   **Goal:** A personal cookbook web application (BiteBooks) for adding, viewing, searching, and organizing recipes.
*   **Architecture:** Decoupled full-stack application with a Django REST API backend and a Vue.js frontend.
*   **Backend Tech Stack:**
    *   **Framework:** Django 6.0.2+ with Django REST Framework (DRF).
    *   **Authentication:** Simple JWT (JSON Web Tokens).
    *   **Database:** PostgreSQL 16.
    *   **Tools:** `python-dotenv`, `django-cors-headers`.
*   **Frontend Tech Stack:**
    *   **Framework:** Vue 3 (Composition API).
    *   **Build Tool:** Vite + TypeScript.
    *   **Styling:** Tailwind CSS 4.x.

## Backend Progress (`recipes` app)
The core recipe management system is implemented:
*   **Models:** `Ingredient`, `Tag`, `Recipe`, and `RecipeIngredient` (through-table for quantities/units).
*   **API Endpoints:**
    *   `/api/ingredients/`: CRUD for ingredients.
    *   `/api/tags/`: CRUD for categorization tags.
    *   `/api/recipes/`: Optimized CRUD for recipes with nested writable support for ingredients and tags.
*   **Optimizations:** Implemented `prefetch_related` in `RecipeViewSet` to resolve N+1 query performance issues.
*   **Data Integrity:** Wrapped complex writes in `atomic` transactions and added nested ingredient creation logic.

## Directory Structure

*   `backend/`: Django project root.
    *   `config/`: Main Django settings and URL configurations.
    *   `recipes/`: Core application containing models, serializers, and views.
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

### Manual Commands (For the User to Run)

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
    python manage.py makemigrations
    python manage.py migrate
    ```

## Development Conventions

*   **API Design:** Use DRF ViewSets. Prefer nested writable serializers for complex relationships.
*   **Performance:** Use `select_related` or `prefetch_related` to avoid N+1 queries.
*   **Styling:** Prefer Tailwind CSS utility classes in Vue components.
*   **Environment Variables:** Store sensitive configurations in the root `.env` file.
*   **Testing:**
    *   Backend: Use Django's built-in test framework.
    *   Frontend: Setup Vitest for unit testing components.
