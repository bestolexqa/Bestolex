import fs from 'fs';
import path from 'path';

const STORAGE_ZONE_NAME = 'electrocreative-zone';
const ACCESS_KEY = process.env.BUNNY_STORAGE_ACCESS_KEY;
const PULL_ZONE = 'electrocreative-cdn.b-cdn.net';
const BASE_STORAGE_URL = 'https://storage.bunnycdn.com';

const productsToFix = [
  {
    id: 'inflatable-dock-shelter',
    sabtechUrl: 'https://sabtech.com.sa/wp-content/uploads/2019/05/abrigos-muelle-hinchables-002-1.jpg',
    filename: 'card-fixed.jpg',
    mime: 'image/jpeg'
  },
  {
    id: 'retractable-dock-shelter',
    sabtechUrl: 'https://sabtech.com.sa/wp-content/uploads/2019/05/abrigo-muelle-retractil-003.jpg',
    filename: 'card-fixed.jpg',
    mime: 'image/jpeg'
  },
  {
    id: 'high-security-road-blocker-pas68',
    sabtechUrl: 'https://sabtech.com.sa/wp-content/uploads/2020/12/SAB_2063BG1.jpg',
    filename: 'card-fixed.jpg',
    mime: 'image/jpeg'
  },
  {
    id: 'above-ground-tyre-killer',
    sabtechUrl: 'https://sabtech.com.sa/wp-content/uploads/2021/08/DSC3344.jpg',
    filename: 'card-fixed.jpg',
    mime: 'image/jpeg'
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

  // 1. Fix the 4 mismatched products
  for (const item of productsToFix) {
    console.log(`\nFetching ${item.id} from ${item.sabtechUrl}...`);
    const res = await fetch(item.sabtechUrl);
    if (!res.ok) throw new Error(`Failed to fetch ${item.sabtechUrl}`);
    const buf = Buffer.from(await res.arrayBuffer());

    // Save locally
    const localDir = `f:/projects/bestolex/public/images/products/${item.id}`;
    fs.mkdirSync(localDir, { recursive: true });
    fs.writeFileSync(path.join(localDir, item.filename), buf);
    console.log(`Saved locally: ${localDir}/${item.filename}`);

    // Upload to Bunny
    const remotePath = `bestolex/products/${item.id}/${item.filename}`;
    const cdnUrl = await uploadFile(buf, remotePath, item.mime);

    // Update in data/products.json
    for (const cat of categories) {
      for (const prod of (cat.products || [])) {
        if (prod.id === item.id) {
          prod.cardImage = cdnUrl;
          console.log(`Updated cardImage for ${prod.id} -> ${cdnUrl}`);
        }
      }
      for (const sub of (cat.subcategories || [])) {
        for (const prod of (sub.products || [])) {
          if (prod.id === item.id) {
            prod.cardImage = cdnUrl;
            console.log(`Updated cardImage for subcat ${prod.id} -> ${cdnUrl}`);
          }
        }
      }
    }
  }

  // 2. Fix the trucks cards & category image (replace cropped cut-out with full uncropped realistic photos)
  const truckCards = {
    'garsite-10000-gallon-truck-1': 'https://electrocreative-cdn.b-cdn.net/bestolex/products/garsite-10000-gallon-truck-1/1.jpg',
    'garsite-10000-gallon-truck-2': 'https://electrocreative-cdn.b-cdn.net/bestolex/products/garsite-10000-gallon-truck-2/1.PNG',
    'garsite-10000-gallon-truck-3': 'https://electrocreative-cdn.b-cdn.net/bestolex/products/garsite-10000-gallon-truck-3/1.jpeg',
    'garsite-10000-gallon-truck-4': 'https://electrocreative-cdn.b-cdn.net/bestolex/products/garsite-10000-gallon-truck-4/1.jpeg'
  };

  for (const cat of categories) {
    if (cat.id === 'other-products') {
      // Update category image to uncropped full realistic photo
      cat.image = 'https://electrocreative-cdn.b-cdn.net/bestolex/products/garsite-10000-gallon-truck-1/1.jpg';
      console.log(`Updated other-products category image to full realistic photo`);
    }

    for (const prod of (cat.products || [])) {
      if (truckCards[prod.id]) {
        prod.cardImage = truckCards[prod.id];
        console.log(`Updated cardImage for truck ${prod.id} to full realistic photo: ${prod.cardImage}`);
      }
    }
  }

  fs.writeFileSync(productsFilePath, JSON.stringify(categories, null, 2), 'utf8');
  console.log('\nAll updates applied to data/products.json successfully!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
