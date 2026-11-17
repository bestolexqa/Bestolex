import { defineEventHandler, readMultipartFormData, createError } from 'h3'

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const formData = await readMultipartFormData(event)
  
  if (!formData || formData.length === 0) {
    throw createError({ statusCode: 400, message: 'No file uploaded' })
  }

  const results = []

  for (const item of formData) {
    if (item.name === 'file' && item.filename) {
      // Create a clean, unique filename
      const timestamp = Date.now()
      const safeFilename = item.filename.replace(/[^a-zA-Z0-9.-]/g, '_').toLowerCase()
      const fileName = `bestolex-${timestamp}-${safeFilename}`

      // Bunny Storage Configuration
      const storageZone = config.bunnyStorageZoneName || 'electrocreative-zone'
      const accessKey = config.bunnyStorageAccessKey || ''
      const baseUrl = (config.bunnyStorageBaseUrl || 'https://storage.bunnycdn.com').replace(/\/$/, '')
      const pullZoneUrl = (config.public.bunnyPullZoneUrl || 'https://electrocreative-cdn.b-cdn.net').replace(/\/$/, '')

      if (!accessKey) {
        throw createError({ statusCode: 500, message: 'Storage is not configured' })
      }
      const allowedTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/avif', 'image/gif']
      if (!allowedTypes.includes(item.type || '')) {
        throw createError({ statusCode: 415, message: 'Only image uploads are allowed' })
      }
      if (item.data.length > 8 * 1024 * 1024) {
        throw createError({ statusCode: 413, message: 'Image is larger than 8 MB' })
      }

      try {
        await $fetch(`${baseUrl}/${storageZone}/${fileName}`, {
          method: 'PUT',
          headers: {
            AccessKey: accessKey,
            'Content-Type': item.type || 'application/octet-stream'
          },
          body: item.data
        })

        results.push({
          url: `${pullZoneUrl}/${fileName}`,
          name: fileName
        })
      } catch (err: any) {
        console.error('Bunny CDN Upload Error:', err)
        throw createError({ statusCode: 500, message: 'Failed to upload image to Bunny CDN' })
      }
    }
  }

  return {
    success: true,
    url: results[0]?.url,
    urls: results.map(r => r.url)
  }
})
