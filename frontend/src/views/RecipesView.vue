<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import RecipeCard from '../components/RecipeCard.vue'
import BaseButton from '../components/BaseButton.vue'

// Define the shape of our recipe data based on the RecipeListSerializer
interface Tag {
  id: number
  name: string
}

interface Recipe {
  id: number
  name: string
  description: string
  tags: Tag[]
  created_at: string
}

const recipes = ref<Recipe[]>([])
const isLoading = ref(true)
const error = ref<string | null>(null)

const fetchRecipes = async () => {
  isLoading.value = true
  error.value = null
  try {
    const response = await axios.get('http://localhost:8000/api/recipes/')
    recipes.value = response.data
  } catch (err) {
    console.error('Error fetching recipes:', err)
    error.value = 'Failed to load recipes. Please make sure the backend server is running.'
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchRecipes()
})
</script>

<template>
  <div class="container mx-auto p-6">
    <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Your Recipes</h1>
        <p class="mt-2 text-gray-600">Browse and manage your personal cookbook.</p>
      </div>
      <div class="mt-4 md:mt-0 flex gap-2">
        <BaseButton variant="outline" @click="fetchRecipes">Refresh</BaseButton>
        <BaseButton variant="primary">Add Recipe</BaseButton>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-12">
      <div class="h-12 w-12 animate-spin rounded-full border-4 border-orange-200 border-t-orange-600"></div>
      <p class="mt-4 text-gray-500">Fetching your recipes...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="rounded-lg bg-red-50 p-6 text-center border border-red-100">
      <p class="text-red-600 font-medium">{{ error }}</p>
      <BaseButton variant="outline" class="mt-4" @click="fetchRecipes">Try Again</BaseButton>
    </div>

    <!-- Empty State -->
    <div v-else-if="recipes.length === 0" class="rounded-xl bg-white border-2 border-dashed border-gray-200 p-12 text-center">
      <h3 class="text-lg font-medium text-gray-900">No recipes found</h3>
      <p class="mt-2 text-gray-500">Start by adding your first recipe to the collection.</p>
      <BaseButton variant="primary" class="mt-6">Add Recipe</BaseButton>
    </div>

    <!-- Recipe Grid -->
    <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <RecipeCard
        v-for="recipe in recipes"
        :key="recipe.id"
        :id="recipe.id"
        :name="recipe.name"
        :description="recipe.description"
        :tags="recipe.tags"
      />
    </div>
  </div>
</template>
