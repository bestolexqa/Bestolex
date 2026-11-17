import fs from 'fs';
import path from 'path';

const STORAGE_ZONE_NAME = 'electrocreative-zone';
const ACCESS_KEY = process.env.BUNNY_STORAGE_ACCESS_KEY;
const PULL_ZONE = 'electrocreative-cdn.b-cdn.net';
const BASE_STORAGE_URL = 'https://storage.bunnycdn.com';

async function uploadToBunny(filePath, remotePath) {
  const buf = fs.readFileSync(filePath);
  const ext = path.extname(filePath).toLowerCase();
  const mime = ext === '.png' ? 'image/png' : (ext === '.webp' ? 'image/webp' : 'image/jpeg');

  const uploadUrl = `${BASE_STORAGE_URL}/${STORAGE_ZONE_NAME}/${remotePath}`;
  const res = await fetch(uploadUrl, {
    method: 'PUT',
    headers: {
      AccessKey: ACCESS_KEY,
      'Content-Type': mime
    },
    body: buf
  });

  if (!res.ok) {
    throw new Error(`Upload failed for ${remotePath}: ${res.status}`);
  }

  const cdnUrl = `https://${PULL_ZONE}/${remotePath}`;
  console.log(`Uploaded: ${cdnUrl}`);
  return cdnUrl;
}

const filesToUpload = [
  // Categories
  { local: 'public/images/categories/docking-systems.jpg', remote: 'bestolex/categories/docking-systems.jpg' },
  { local: 'public/images/categories/waste-management.jpg', remote: 'bestolex/categories/waste-management.jpg' },
  { local: 'public/images/categories/perimeter-protection.jpg', remote: 'bestolex/categories/perimeter-protection.jpg' },
  { local: 'public/images/categories/industrial-doors.jpg', remote: 'bestolex/categories/industrial-doors.jpg' },

  // News / Blog
  { local: 'public/images/news/news1.jpg', remote: 'bestolex/news/news1.jpg' },
  { local: 'public/images/news/news2.jpg', remote: 'bestolex/news/news2.jpg' },
  { local: 'public/images/news/news3.jpg', remote: 'bestolex/news/news3.jpg' },

  // Services hero
  { local: 'public/images/services/srv1.png', remote: 'bestolex/services/srv1.png' },

  // Training
  { local: 'public/images/training/bench.jpg', remote: 'bestolex/training/bench.jpg' },
  { local: 'public/images/training/power-unit.jpg', remote: 'bestolex/training/power-unit.jpg' },
  { local: 'public/images/training/mobile.jpg', remote: 'bestolex/training/mobile.jpg' },
  { local: 'public/images/training/diagnostics.jpg', remote: 'bestolex/training/diagnostics.jpg' },
  { local: 'public/images/training/instructor.jpg', remote: 'bestolex/training/instructor.jpg' },
  { local: 'public/images/training/cutaway.jpg', remote: 'bestolex/training/cutaway.jpg' },
  { local: 'public/images/training/pumps.jpg', remote: 'bestolex/training/pumps.jpg' },
  { local: 'public/images/training/cylinders.jpg', remote: 'bestolex/training/cylinders.jpg' },
  { local: 'public/images/training/valves.jpg', remote: 'bestolex/training/valves.jpg' },
  { local: 'public/images/training/circuits.jpg', remote: 'bestolex/training/circuits.jpg' },
  { local: 'public/images/training/components.jpg', remote: 'bestolex/training/components.jpg' }
];

async function main() {
  console.log('Uploading remaining non-product images to Bunny CDN...');
  const urlMap = {};

  for (const item of filesToUpload) {
    if (fs.existsSync(item.local)) {
      const cdnUrl = await uploadToBunny(item.local, item.remote);
      // Map local path e.g. '/images/training/bench.jpg' -> cdnUrl
      const localWebPath = item.local.replace('public', '');
      urlMap[localWebPath] = cdnUrl;
    } else {
      console.warn(`File not found locally: ${item.local}`);
    }
  }

  console.log('\nURL Mapping generated:');
  console.log(JSON.stringify(urlMap, null, 2));

  // Also upload hero-bg fallback if exists
  const heroPath = 'public/images/about/showroom-v2.jpg';
  const cdnHero = 'https://electrocreative-cdn.b-cdn.net/bestolex/about/showroom-v2.jpg';
  urlMap['/images/hero/hero-bg.jpg'] = cdnHero;

  fs.writeFileSync('scripts/cdn_url_map.json', JSON.stringify(urlMap, null, 2), 'utf8');
}

main().catch(console.error);
