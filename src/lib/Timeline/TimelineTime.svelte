<script lang="ts">
  import classNames from 'classnames';
</script>

<time
  {...$$props}
  class={classNames('mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500', $$props.class)}
>
  <slot />
</time>
