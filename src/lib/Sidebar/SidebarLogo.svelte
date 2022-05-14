<script lang="ts">
  import classNames from 'classnames';
  import { getContext } from 'svelte';
  import type { Writable } from 'svelte/store';

  export let href: string;
  export let img: string;
  export let imgAlt: string;

  const collapsed = getContext<Writable<boolean>>('collapsed');
</script>

<a
  {...$$props}
  class={classNames(
    'mb-5 flex items-center',
    {
      'pl-2': !$collapsed,
      'justify-center': $collapsed,
    },
    $$props.class
  )}
  {href}
>
  <img
    alt={imgAlt}
    class={classNames(
      {
        'mr-3': !$collapsed,
      },
      'h-6 sm:h-7 object-contain'
    )}
    src={img}
  />
  <span
    class={classNames(
      $collapsed === true ? 'sr-only' : 'self-center whitespace-nowrap text-xl font-semibold dark:text-white'
    )}
    data-testid="sidebar-logo"
  >
    <slot />
  </span>
</a>
