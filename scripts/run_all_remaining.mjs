import { execSync } from 'child_process';

const categories = ['docking-systems', 'waste-management'];

console.log('Starting remaining categories execution: docking-systems and waste-management...');

for (const cat of categories) {
  console.log(`\n===============================================================`);
  console.log(`>>> STARTING CATEGORY: ${cat} <<<`);
  console.log(`===============================================================`);
  execSync(`node scripts/upload_category_batch.mjs ${cat}`, { stdio: 'inherit' });
}

console.log('\n===============================================================');
console.log('ALL CATEGORIES UPLOADED & PRODUCTS.JSON UPDATED SUCCESSFULLY!');
console.log('===============================================================');

// Sound console beep
try {
  execSync('powershell -c "[System.Console]::Beep(900, 350); [System.Console]::Beep(1200, 400)"');
} catch (e) {
  // ignore
}
