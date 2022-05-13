<script lang="ts">
  import classNames from 'classnames';
  import { setContext } from 'svelte';

  export let collapsed: boolean = false;
  $: setContext('collapsed', collapsed);
</script>

<aside aria-label="Sidebar" {...$$props} class={classNames('h-full', collapsed ? 'w-16' : 'w-64')}>
  <div
    class={classNames(
      'h-full overflow-y-auto overflow-x-hidden rounded bg-white py-4 px-3 dark:bg-gray-800',
      $$props.class
    )}
  >
    <slot />
  </div>
</aside>
