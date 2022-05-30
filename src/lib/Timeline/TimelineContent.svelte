<script lang="ts">
  import classNames from 'classnames';
  import { getContext } from 'svelte';
</script>

<div
  data-testid="timeline-content"
  {...$$props}
  class={classNames({ 'mt-3 sm:pr-8': getContext('horizontal') }, $$props.class)}
>
  <slot />
</div>
