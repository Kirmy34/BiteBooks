<script setup lang="ts">
import RecipeCard from '../components/RecipeCard.vue'
import BaseButton from '../components/BaseButton.vue'

const dummyRecipes = [
  // ... existing dummy recipes
  {
    id: 1,
    title: 'Spaghetti Carbonara',
    description: 'A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.',
    tags: ['Italian', 'Pasta', 'Dinner']
  },
  {
    id: 2,
    title: 'Chicken Avocado Salad',
    description: 'A fresh and healthy salad with grilled chicken, creamy avocado, and a lemon vinaigrette.',
    tags: ['Healthy', 'Salad', 'Lunch']
  },
  {
    id: 3,
    title: 'Fluffy Pancakes',
    description: 'Golden-brown, light and fluffy pancakes perfect for a weekend breakfast.',
    tags: ['Breakfast', 'Sweet']
  }
]
</script>

<template>
  <div class="container mx-auto p-6">
    <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Your Recipes</h1>
        <p class="mt-2 text-gray-600">Browse and manage your personal cookbook.</p>
      </div>
      <div class="mt-4 md:mt-0 flex gap-2">
        <BaseButton variant="outline">Filter</BaseButton>
        <BaseButton variant="primary">Add Recipe</BaseButton>
      </div>
    </div>

    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
      <RecipeCard
        v-for="recipe in dummyRecipes"
        :key="recipe.id"
        :title="recipe.title"
        :description="recipe.description"
        :tags="recipe.tags"
      />
    </div>
  </div>
</template>
