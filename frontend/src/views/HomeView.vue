<script setup lang="ts">
import { useRouter } from 'vue-router'
import BaseButton from '../components/BaseButton.vue'

const router = useRouter()

const navigateTo = (path: string) => {
  router.push(path)
}
</script>

<template>
  <div class="flex min-h-[calc(100vh-73px)] flex-col items-center justify-center bg-gray-50 px-6 py-12 text-center">
    <div class="max-w-2xl">
      <h1 class="text-5xl font-extrabold tracking-tight text-gray-900 sm:text-6xl">
        Your Personal <span class="text-orange-600">Cookbook</span>
      </h1>
      <p class="mt-6 text-lg leading-8 text-gray-600">
        Organize your favorite recipes, manage your ingredients, and plan your next delicious meal with BiteBooks.
      </p>
      
      <div class="mt-12 flex flex-col items-center justify-center gap-6 sm:flex-row">
        <button 
          @click="navigateTo('/recipes')"
          class="group relative flex h-48 w-full flex-col items-center justify-center overflow-hidden rounded-2xl bg-white p-8 shadow-sm ring-1 ring-gray-200 transition-all hover:shadow-xl hover:ring-orange-500 sm:w-64"
        >
          <div class="mb-4 rounded-full bg-orange-100 p-3 text-orange-600 transition-transform group-hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <span class="text-xl font-bold text-gray-900">Browse Recipes</span>
          <span class="mt-2 text-sm text-gray-500 text-center">View and search your collection</span>
        </button>

        <button 
          @click="navigateTo('/ingredients')"
          class="group relative flex h-48 w-full flex-col items-center justify-center overflow-hidden rounded-2xl bg-white p-8 shadow-sm ring-1 ring-gray-200 transition-all hover:shadow-xl hover:ring-emerald-500 sm:w-64"
        >
          <div class="mb-4 rounded-full bg-emerald-100 p-3 text-emerald-600 transition-transform group-hover:scale-110">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3" />
            </svg>
          </div>
          <span class="text-xl font-bold text-gray-900">Ingredients</span>
          <span class="mt-2 text-sm text-gray-500 text-center">Manage your pantry stock</span>
        </button>
      </div>

      <div class="mt-16">
        <BaseButton variant="outline" @click="navigateTo('/recipes')">
          Quick Start Guide
        </BaseButton>
      </div>
    </div>
  </div>
</template>
