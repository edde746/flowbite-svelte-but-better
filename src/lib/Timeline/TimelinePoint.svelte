<script lang="ts">
  import classNames from 'classnames';
  import { getContext, type SvelteComponent } from 'svelte';

  export let icon: typeof SvelteComponent | null = null;
</script>

<div
  data-testid="timeline-point"
  {...$$props}
  class={classNames({ 'flex items-center': getContext('horizontal') }, $$props.class)}
>
  <slot />
  {#if icon}
    <span
      class="absolute -left-3 flex h-6 w-6 items-center justify-center rounded-full bg-blue-200 ring-8 ring-white dark:bg-blue-900 dark:ring-gray-900"
    >
      <svelte:component this={icon} aria-hidden class="h-3 w-3 text-blue-600 dark:text-blue-300" />
    </span>
  {:else}
    <div
      class="absolute -left-1.5 mt-1.5 h-3 w-3 rounded-full border border-white bg-gray-200 dark:border-gray-900 dark:bg-gray-700"
    />
  {/if}
  {#if getContext('horizontal')}
    <div class="hidden h-0.5 w-full bg-gray-200 dark:bg-gray-700 sm:flex" />
  {/if}
</div>
