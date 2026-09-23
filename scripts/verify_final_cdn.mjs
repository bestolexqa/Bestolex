import fs from 'fs';

const categories = JSON.parse(fs.readFileSync('data/products.json', 'utf8'));

let totalProducts = 0;
let totalImages = 0;
let sabtechRemaining = 0;
let bunnyImages = 0;

for (const cat of categories) {
  console.log(`\nCategory: [${cat.id}] - Products: ${cat.products.length}`);
  for (const prod of cat.products) {
    totalProducts++;
    const count = prod.images ? prod.images.length : 0;
    totalImages += count;
    
    // Check if sabtech remains
    const allUrls = [prod.cardImage, prod.coverImage, prod.image, ...(prod.images || [])].filter(Boolean);
    const hasSabtech = allUrls.some(u => u.includes('sabtech'));
    if (hasSabtech) sabtechRemaining++;

    const isBunny = prod.image && prod.image.includes('b-cdn.net');
    if (isBunny) bunnyImages++;

    console.log(`  - [${prod.id}] images: ${count} | primary: ${prod.image?.slice(0, 70)}...`);
  }
}

console.log('\n=======================================');
console.log(`Total Products: ${totalProducts}`);
console.log(`Total Images in Galleries: ${totalImages}`);
console.log(`Products with Bunny CDN primary: ${bunnyImages}`);
console.log(`Products with old sabtech URLs remaining: ${sabtechRemaining}`);
console.log('=======================================');
