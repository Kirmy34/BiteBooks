<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import BaseButton from '../components/BaseButton.vue'

const props = defineProps<{
  id: string
}>()

const router = useRouter()

interface Tag {
  id: number
  name: string
}

interface RecipeIngredient {
  ingredient: number
  ingredient_name: string
  quantity: number
  unit: string
}

interface Recipe {
  id: number
  name: string
  description: string
  instructions: string
  tags: Tag[]
  recipe_ingredients: RecipeIngredient[]
  created_at: string
}

const recipe = ref<Recipe | null>(null)
const isLoading = ref(true)
const error = ref<string | null>(null)

const fetchRecipeDetail = async () => {
  isLoading.value = true
  error.value = null
  try {
    const response = await axios.get(`http://localhost:8000/api/recipes/${props.id}/`)
    recipe.value = response.data
  } catch (err) {
    console.error('Error fetching recipe detail:', err)
    error.value = 'Failed to load recipe details. It may not exist or the server is down.'
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchRecipeDetail()
})

const goBack = () => {
  router.back()
}
</script>

<template>
  <div class="container mx-auto p-6 max-w-4xl">
    <!-- Navigation -->
    <div class="mb-8">
      <button 
        @click="goBack" 
        class="flex items-center text-sm font-medium text-gray-500 hover:text-orange-600 transition-colors"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Back to Recipes
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
      <div class="h-12 w-12 animate-spin rounded-full border-4 border-orange-200 border-t-orange-600"></div>
      <p class="mt-4 text-gray-500">Loading recipe details...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="rounded-lg bg-red-50 p-8 text-center border border-red-100">
      <p class="text-red-600 font-medium">{{ error }}</p>
      <BaseButton variant="outline" class="mt-4" @click="fetchRecipeDetail">Try Again</BaseButton>
    </div>

    <!-- Recipe Detail -->
    <div v-else-if="recipe" class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
      <!-- Header / Image Placeholder -->
      <div class="h-64 bg-orange-50 flex items-center justify-center text-orange-200 relative">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 022-2V6a2 2 0 02-2-2H6a2 2 0 02-2 2v12a2 2 0 022 2z" />
        </svg>
        <div class="absolute bottom-6 left-6 right-6">
          <div class="flex flex-wrap gap-2 mb-3">
            <span 
              v-for="tag in recipe.tags" 
              :key="tag.id"
              class="px-3 py-1 rounded-full bg-white/90 text-orange-700 text-xs font-bold backdrop-blur-sm shadow-sm"
            >
              {{ tag.name }}
            </span>
          </div>
          <h1 class="text-4xl font-extrabold text-gray-900 drop-shadow-sm bg-white/80 inline-block px-4 py-2 rounded-lg backdrop-blur-md">
            {{ recipe.name }}
          </h1>
        </div>
      </div>

      <div class="p-8 md:p-12">
        <p class="text-lg text-gray-600 italic leading-relaxed mb-10 border-l-4 border-orange-200 pl-6">
          {{ recipe.description || 'No description provided.' }}
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          <!-- Ingredients Section -->
          <div class="md:col-span-1">
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center">
              <span class="w-8 h-8 rounded-lg bg-orange-100 text-orange-600 flex items-center justify-center mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </span>
              Ingredients
            </h2>
            <ul class="space-y-4">
              <li 
                v-for="(item, index) in recipe.recipe_ingredients" 
                :key="index"
                class="flex justify-between items-center pb-3 border-b border-gray-50"
              >
                <span class="text-gray-700 font-medium">{{ item.ingredient_name }}</span>
                <span class="text-gray-500 text-sm bg-gray-50 px-2 py-1 rounded-md">
                  {{ item.quantity }} {{ item.unit }}
                </span>
              </li>
            </ul>
          </div>

          <!-- Instructions Section -->
          <div class="md:col-span-2">
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center">
              <span class="w-8 h-8 rounded-lg bg-orange-100 text-orange-600 flex items-center justify-center mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                </svg>
              </span>
              Instructions
            </h2>
            <div class="prose prose-orange max-w-none">
              <p class="whitespace-pre-line text-gray-700 leading-relaxed text-lg">
                {{ recipe.instructions }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
