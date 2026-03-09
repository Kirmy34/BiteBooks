# BiteBooks Project Overview

BiteBooks is a full-stack web application designed to be your personal digital cookbook. It allows you to add, view, search, and organize your favorite recipes in one place. This project is designed as a beginner-friendly introduction to full-stack development.

## Future Roadmap
- [ ] Shopping list utility.
- [ ] Meal planning functionality.

## Core Infrastructure
- **Orchestration:** Docker Compose
- **Database:** PostgreSQL 16
- **Storage:** Persistent volumes for database data
- **Configuration:** Managed via a root `.env` file

## Project Structure
- `/`: Root directory with infrastructure and orchestrator settings.
- `backend/`: Django REST API project (see `backend/GEMINI.md` for details).
- `frontend/`: Vue.js web application (see `frontend/GEMINI.md` for details).
- `db_data/`: (Ignored) Local persistent database storage.

## Building and Running (Docker Only)

To build and start all services (Frontend, Backend, and DB):

```bash
docker-compose up --build
```

- **Frontend:** [http://localhost:5173](http://localhost:5173)
- **Backend API:** [http://localhost:8000](http://localhost:8000)
- **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Development Workflow
- Global configuration and secrets should be managed in the root `.env`.
- For domain-specific information, refer to the `GEMINI.md` files in the respective directories.

## High-Level TODOs
- [ ] Create initial Django apps for project features.
- [ ] Set up API endpoints in `backend/`.
- [ ] Integrate frontend with backend API.
- [ ] Implement user authentication flows.
