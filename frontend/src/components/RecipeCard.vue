<script setup lang="ts">
import { RouterLink } from 'vue-router'

interface Tag {
  id: number
  name: string
}

defineProps<{
  id: number
  name: string
  description: string
  tags: Tag[]
}>()
</script>

<template>
  <RouterLink :to="{ name: 'recipe-detail', params: { id: id } }" class="group block h-full">
    <article class="flex flex-col overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition group-hover:shadow-md group-hover:border-orange-200 h-full">
    <!-- Placeholder for recipe image -->
    <div class="h-48 w-full bg-orange-50 flex items-center justify-center text-orange-200">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 022-2V6a2 2 0 02-2-2H6a2 2 0 02-2 2v12a2 2 0 022 2z" />
      </svg>
    </div>

    <div class="flex flex-1 flex-col p-4 sm:p-6">
      <h3 class="text-lg font-bold text-gray-900 line-clamp-1">
        {{ name }}
      </h3>

      <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500 flex-1">
        {{ description || 'No description provided.' }}
      </p>

      <div class="mt-4 flex flex-wrap gap-1">
        <span
          v-for="tag in tags"
          :key="tag.id"
          class="whitespace-nowrap rounded-full bg-orange-100 px-2.5 py-0.5 text-xs font-medium text-orange-700"
        >
          {{ tag.name }}
        </span>
      </div>
    </div>
  </article>
  </RouterLink>
</template>
