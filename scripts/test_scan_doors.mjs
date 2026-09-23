import { getAllImagesInFolder } from './drive_scanner_helper.mjs';

async function main() {
  console.log('--- 1. High-speed Roll doors ---');
  const d1 = await getAllImagesInFolder('1LqvI9FAnV2IpaxJFtOTu2L0Gass1e5Xu');
  console.log(`Found ${d1.length} images:`);
  d1.forEach(f => console.log(`  - [${f.id}] ${f.name} (component: ${f.isComponent})`));

  console.log('\n--- 2. Industrial Sectional Doors ---');
  const d2 = await getAllImagesInFolder('1zxw8N3IO7AN9_tlkU9UyizFno3UFOBOd');
  console.log(`Found ${d2.length} images:`);
  d2.forEach(f => console.log(`  - [${f.id}] ${f.name} (component: ${f.isComponent})`));
}

main().catch(console.error);
