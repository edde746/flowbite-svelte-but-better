<script lang="ts">
  import classNames from 'classnames';
  import { getContext } from 'svelte';
</script>

<li
  data-testid="timeline-item"
  {...$$props}
  class={classNames(
    { 'mb-10 ml-6': !getContext('horizontal'), 'relative mb-6 sm:mb-0': getContext('horizontal') },
    $$props.class
  )}
>
  <slot />
</li>
