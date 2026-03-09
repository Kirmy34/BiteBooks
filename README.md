# BiteBooks

BiteBooks is your personal digital cookbook. It's a beginner-friendly full-stack web application designed for adding, viewing, searching, and organizing your favorite recipes. In the future, we plan to include shopping list and meal planning utilities as well.

This project is a great introduction to full-stack development, using a Django backend and a Vue.js frontend, all containerized with Docker.

## Getting Started

Follow these steps to set up and run the project locally using Docker.

### 1. Clone the repository

Open your terminal and run:

```bash
git clone https://github.com/Kirmy34/BiteBooks.git
cd BiteBooks
```

### 2. Build the images

Build the Docker images for the frontend, backend, and database:

```bash
docker compose build
```

### 3. Run the project

Start the containers in detached mode:

```bash
docker compose up -d
```

Once the containers are running, you can access the application at:
- **Frontend:** [http://localhost:5173](http://localhost:5173)
- **Backend API:** [http://localhost:8000](http://localhost:8000)
- **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 4. Open in VS Code and Attach to Containers

To develop directly inside the containers using VS Code:

1.  Open frontend/backend folder in VS Code.
2.  Install the **Dev Containers** extension if you haven't already.
3.  Click the green "Remote Window" button in the bottom-left corner or press `F1` and select "Dev Containers: Reopen in Container".
4.  Choose either the `frontend` or `backend` container to attach to.

Happy cooking (and coding)!
