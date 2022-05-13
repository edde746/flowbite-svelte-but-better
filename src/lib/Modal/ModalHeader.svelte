<script lang="ts">
  import classNames from 'classnames';
  import { XOutline } from 'svelte-heros';
  import { context } from './ModalStore';
</script>

<div
  class={classNames('flex items-center justify-between rounded-t dark:border-gray-600', {
    'p-2': $context.popup,
    'border-b p-5': !$context.popup,
  })}
>
  <h3 class="text-xl font-medium text-gray-900 dark:text-white">
    <slot />
  </h3>
  <button
    class="ml-auto inline-flex items-center rounded-lg bg-transparent p-1.5 text-sm text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-white"
    type="button"
    on:click={() => $context.onClose()}
  >
    <XOutline className="h-5 w-5" />
  </button>
</div>
