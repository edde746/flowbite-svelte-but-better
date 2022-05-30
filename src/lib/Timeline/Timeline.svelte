<script lang="ts">
  import classNames from 'classnames';
  import { setContext } from 'svelte';

  export let horizontal: boolean = false;
  $: setContext('horizontal', horizontal);
</script>

<ol
  data-testid="timeline-component"
  class={classNames({
    'relative border-l border-gray-200 dark:border-gray-700': !horizontal,
    'items-center sm:flex': horizontal,
  })}
>
  <slot />
</ol>
