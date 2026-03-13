<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white border-b border-gray-200">
      <nav class="container mx-auto flex items-center gap-8 px-6 py-4">
        <RouterLink to="/" class="text-xl font-bold text-orange-600">BiteBooks</RouterLink>
        <div class="flex gap-6">
          <RouterLink 
            to="/" 
            class="text-sm font-medium text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600"
          >
            Home
          </RouterLink>
          <RouterLink 
            to="/recipes" 
            class="text-sm font-medium text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600"
          >
            Recipes
          </RouterLink>
          <RouterLink 
            to="/ingredients" 
            class="text-sm font-medium text-gray-600 hover:text-orange-600 transition-colors"
            active-class="text-orange-600"
          >
            Ingredients
          </RouterLink>
        </div>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="bg-white border-t border-gray-200 mt-12">
      <div class="container mx-auto px-6 py-4 text-center text-sm text-gray-500">
        &copy; Made with ❤️
      </div>
    </footer>
  </div>
</template>

<style>
/* Global resets or overrides if needed */
</style>
