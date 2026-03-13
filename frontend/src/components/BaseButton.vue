<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'outline'
  type?: 'button' | 'submit' | 'reset'
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  type: 'button'
})

const variants = {
  primary: 'bg-orange-600 text-white hover:bg-orange-700 focus-visible:outline-orange-600',
  secondary: 'bg-emerald-600 text-white hover:bg-emerald-700 focus-visible:outline-emerald-600',
  outline: 'bg-white text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50'
}

const baseClasses = 'inline-flex items-center rounded-md px-3.5 py-2.5 text-sm font-semibold shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 transition-all duration-200 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed'
</script>

<template>
  <button :type="type" :class="[baseClasses, variants[variant]]">
    <slot />
  </button>
</template>
