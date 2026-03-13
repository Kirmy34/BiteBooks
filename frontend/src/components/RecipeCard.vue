<script setup lang="ts">
defineProps<{
  title: string
  description: string
  imageUrl?: string
  tags: string[]
}>()
</script>

<template>
  <article class="overflow-hidden rounded-xl border border-gray-100 bg-white shadow-sm transition hover:shadow-md">
    <img
      v-if="imageUrl"
      alt="Recipe image"
      :src="imageUrl"
      class="h-48 w-full object-cover"
    />
    <div v-else class="h-48 w-full bg-gray-200 flex items-center justify-center text-gray-400">
      No image
    </div>

    <div class="p-4 sm:p-6">
      <h3 class="text-lg font-bold text-gray-900">
        {{ title }}
      </h3>

      <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500">
        {{ description }}
      </p>

      <div class="mt-4 flex flex-wrap gap-1">
        <span
          v-for="tag in tags"
          :key="tag"
          class="whitespace-nowrap rounded-full bg-orange-100 px-2.5 py-0.5 text-xs text-orange-600"
        >
          {{ tag }}
        </span>
      </div>
    </div>
  </article>
</template>
