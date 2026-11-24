import { collectPaths, NEW_CDN_HOST, NEW_STORAGE_ZONE } from '~~/server/utils/cdnMigration'

/** Lists what is due to be migrated. Admin-only via the admin guard. */
export default defineEventHandler(async () => {
  const paths = await collectPaths()
  return {
    zone: NEW_STORAGE_ZONE,
    cdn: NEW_CDN_HOST,
    keyConfigured: Boolean(process.env.BUNNY_NEW_STORAGE_KEY),
    total: paths.length,
    paths
  }
})
