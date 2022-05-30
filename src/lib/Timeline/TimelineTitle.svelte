<script lang="ts">
  import classNames from 'classnames';
</script>

<h3 {...$$props} class={classNames('text-lg font-semibold text-gray-900 dark:text-white', $$props.class)}>
  <slot />
</h3>
