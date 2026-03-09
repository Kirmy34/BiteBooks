# BiteBooks Frontend Context

This directory contains the Vue-based user interface for the BiteBooks project.

## Technology Stack
- **Framework:** Vue.js 3 (Vite)
- **Styling:** Tailwind CSS 4
- **Language:** TypeScript
- **Package Manager:** npm

## Directory Structure
- `src/`: Main source code (App.vue, main.ts).
- `public/`: Static assets.
- `package.json`: Dependency and script management.
- `vite.config.ts`: Vite build tool configuration.

## Local Development (No Docker)
1. Ensure Node.js (v18+) is installed.
2. Install dependencies: `npm install`.
3. Start the dev server: `npm run dev`.
4. Build for production: `npm run build`.

## Frontend Conventions
- **Components:** Use Single-File Components (SFCs) with `<script setup lang="ts">`.
- **Styling:** Leverage Tailwind's utility classes for rapid and consistent UI development.
- **Typing:** Enforce strict TypeScript types to prevent runtime errors.
- **Naming:** Follow Vue's style guide for component and file naming (PascalCase for components).
- **Communication:** Connect to the backend API via standard `fetch` or `axios` utilizing the `VITE_API_URL` environment variable.
