import fs from 'fs';
import path from 'path';

const STORAGE_ZONE_NAME = 'electrocreative-zone';
const ACCESS_KEY = 'fdbaf174-b9f2-4453-93bbfa08f649-6912-41c6';
const PULL_ZONE = 'electrocreative-cdn.b-cdn.net';
const BASE_STORAGE_URL = 'https://storage.bunnycdn.com';

const newDir = 'C:/Users/PC/.gemini/antigravity-ide/brain/e987ab83-416f-4276-99c5-74533c0171ec/.user_uploaded';

const mappings = [
  {
    id: 'garsite-10000-gallon-truck-1',
    file: 'media_1790137170027.png',
    name: 'Truck 1 (Front View 241 Garsite)'
  },
  {
    id: 'garsite-10000-gallon-truck-2',
    file: 'media_1790137174359.png',
    name: 'Truck 2 (Front View Ramp Star)'
  },
  {
    id: 'garsite-10000-gallon-truck-3',
    file: 'media_1790137165503.png',
    name: 'Truck 3 (Side View Flammable F-61)'
  },
  {
    id: 'garsite-10000-gallon-truck-4',
    file: 'media_1790137148014.png',
    name: 'Truck 4 (Rear View Clear Exit)'
  }
];

async function uploadFile(buffer, remotePath, mimeType) {
  const uploadUrl = `${BASE_STORAGE_URL}/${STORAGE_ZONE_NAME}/${remotePath}`;
  console.log(`Uploading to ${uploadUrl}...`);

  const response = await fetch(uploadUrl, {
    method: 'PUT',
    headers: {
      AccessKey: ACCESS_KEY,
      'Content-Type': mimeType
    },
    body: buffer
  });

  if (!response.ok) {
    throw new Error(`Upload failed: ${response.status} ${response.statusText}`);
  }

  const cdnUrl = `https://${PULL_ZONE}/${remotePath}`;
  console.log(`Success: ${cdnUrl}`);
  return cdnUrl;
}

async function main() {
  const productsFilePath = 'f:/projects/bestolex/data/products.json';
  const categories = JSON.parse(fs.readFileSync(productsFilePath, 'utf8'));

  const uploadedCdnUrls = {};

  for (const item of mappings) {
    console.log(`\nProcessing ${item.id} - ${item.name}...`);
    const filePath = path.join(newDir, item.file);
    const buf = fs.readFileSync(filePath);

    // 1. Save locally in public/images/products/${item.id}
    const localDir = `f:/projects/bestolex/public/images/products/${item.id}`;
    fs.mkdirSync(localDir, { recursive: true });
    fs.writeFileSync(path.join(localDir, 'card-v3.png'), buf);
    console.log(`Saved locally: ${localDir}/card-v3.png`);

    // 2. Upload to Bunny CDN
    const remotePath = `bestolex/products/${item.id}/card-v3.png`;
    const cdnUrl = await uploadFile(buf, remotePath, 'image/png');
    uploadedCdnUrls[item.id] = cdnUrl;

    // 3. Update products.json for this truck
    for (const cat of categories) {
      for (const prod of (cat.products || [])) {
        if (prod.id === item.id) {
          prod.cardImage = cdnUrl;
          // Ensure it's also in images gallery
          if (!prod.images) prod.images = [];
          if (!prod.images.includes(cdnUrl)) {
            prod.images.unshift(cdnUrl);
          }
          console.log(`Updated ${prod.id} cardImage to ${cdnUrl}`);
        }
      }
    }
  }

  // Update Category image for other-products (Heavy Machinery & Equipment)
  for (const cat of categories) {
    if (cat.id === 'other-products') {
      // Use Truck 1 iconic image
      cat.image = uploadedCdnUrls['garsite-10000-gallon-truck-1'];
      console.log(`Updated other-products category image to ${cat.image}`);
    }
  }

  fs.writeFileSync(productsFilePath, JSON.stringify(categories, null, 2), 'utf8');
  console.log('\nAll 4 trucks and category updated in products.json successfully!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
