// Categories, subcategories and product names for menus and lists; one request shared by every
// component on the page (same key), resolved during server rendering.
export const useCatalogNav = () =>
  useFetch('/api/catalog/nav', { key: 'catalog-nav', default: () => [] as any[] })
