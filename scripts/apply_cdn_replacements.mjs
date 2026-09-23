import fs from 'fs';
import path from 'path';

const urlMap = JSON.parse(fs.readFileSync('./scripts/cdn_url_map.json', 'utf8'));

// Also make sure hero-bg is mapped
urlMap['/images/hero/hero-bg.jpg'] = 'https://electrocreative-cdn.b-cdn.net/bestolex/about/showroom-v2.jpg';

const filesToUpdate = [
  'pages/services.vue',
  'pages/training.vue',
  'pages/contact.vue',
  'data/articles.json',
  'server/api/blog/index.post.ts',
  'server/utils/blogStorage.ts',
  'pages/index.vue',
  'pages/products/category/[id].vue',
  'pages/products/index.vue',
  'pages/blog/index.vue',
  'pages/blog/[id].vue'
];

for (const relPath of filesToUpdate) {
  if (!fs.existsSync(relPath)) continue;
  let content = fs.readFileSync(relPath, 'utf8');
  let changed = false;

  for (const [localPath, cdnUrl] of Object.entries(urlMap)) {
    if (content.includes(localPath)) {
      content = content.replaceAll(localPath, cdnUrl);
      changed = true;
      console.log(`Replaced ${localPath} -> CDN in ${relPath}`);
    }
  }

  if (changed) {
    fs.writeFileSync(relPath, content, 'utf8');
    console.log(`Updated file: ${relPath}`);
  }
}

console.log('Replacement script completed.');
