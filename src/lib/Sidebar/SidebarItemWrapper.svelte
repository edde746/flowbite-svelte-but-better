<script lang="ts">
  import { Tooltip } from '$lib';
  import { getContext } from 'svelte';
</script>

<li data-testid="sidebar-item">
  {#if getContext('collapsed') === true}
    <Tooltip data-testid="sidebar-item-tooltip" placement="right">
      <slot />
      <div slot="content">
        <slot name="tooltip" />
      </div>
    </Tooltip>
  {:else}
    <slot />
  {/if}
</li>
