<script lang="ts">
  import classNames from 'classnames';
  import { context } from './ModalStore';
</script>

<div
  class={classNames(
    'p-6',
    {
      'pt-0': $context.popup,
    },
    $$props.class
  )}
>
  <slot />
</div>
