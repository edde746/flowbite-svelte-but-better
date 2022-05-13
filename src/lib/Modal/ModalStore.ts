import { writable } from 'svelte/store';

export const context = writable({ onClose: () => {}, popup: false });
