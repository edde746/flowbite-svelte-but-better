<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  export let data: any = {};
</script>

<li
  class="block cursor-pointer py-2 px-4 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white"
  on:click={() => dispatch('click', data)}
>
  <slot />
</li>
