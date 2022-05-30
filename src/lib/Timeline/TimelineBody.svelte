<script lang="ts">
  import classNames from 'classnames';
</script>

<p {...$$props} class={classNames('mb-4 text-base font-normal text-gray-500 dark:text-gray-400', $$props.class)}>
  <slot />
</p>
