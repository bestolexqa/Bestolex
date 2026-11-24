import fs from 'fs';
import path from 'path';
import { getAllImagesInFolder } from './drive_scanner_helper.mjs';

const STORAGE_ZONE_NAME = 'electrocreative-zone';
const ACCESS_KEY = process.env.BUNNY_STORAGE_ACCESS_KEY;
const PULL_ZONE = 'cdn.bestolex.com';
const BASE_STORAGE_URL = 'https://storage.bunnycdn.com';

const arabicTranslations = {
  'بستم غاز لتسهيل فتح الباب العلوي': 'gas-lift-cylinder',
  'صمام لقفل فتحة تصريف السوائل': 'liquid-drain-valve',
  'صندوق الكهرباء': 'control-panel-box',
  'مانع رجوع النفايات': 'waste-retainer',
  'هوك التحميل قابل للفك والتركيب': 'removable-hooklift',
  'لوحة التحكم': 'control-panel',
  'مفتاح تعديل إرتفاع البالة': 'bale-height-switch',
  'نظام متطور الهيدروليك': 'hydraulic-system',
  'نفايات القوارير و العلب': 'cans-bottles-waste'
};

const allProducts = [
  // Industrial Doors
  { cat: 'industrial-doors', id: 'high-speed-doors', driveId: '1LqvI9FAnV2IpaxJFtOTu2L0Gass1e5Xu' },
  { cat: 'industrial-doors', id: 'industrial-sectional-doors', driveId: '1zxw8N3IO7AN9_tlkU9UyizFno3UFOBOd' },

  // Perimeter Protection
  { cat: 'perimeter-protection', id: 'above-ground-tyre-killer', driveId: '1ZSOngI6q6fY5JCQuho2idWZnKrVkA9nu' },
  { cat: 'perimeter-protection', id: 'road-bollard', driveId: '1Anq0MCMGbvKvrfTldFvM7N8tbFi_GwBj' },
  { cat: 'perimeter-protection', id: 'high-security-road-blocker-pas68', driveId: '12m8cDfgsKEueLngFvW6v0GVtVExE7XX5' },
  { cat: 'perimeter-protection', id: 'high-security-shallow-road-blocker-pas68', driveId: '1f0nDDg88oAGKUv1DPmo8l1hkPdDU6PjS' },
  { cat: 'perimeter-protection', id: 'road-blocker', driveId: '1OYJBq9yHDKVVfnbYs4kj9m6q0p1nWNmq' },
  { cat: 'perimeter-protection', id: 'surface-mount-hydraulic-road-blocker', driveId: '1oAlxZML2BX3xKwskbnmBmc_6nrk4ytXk' },
  { cat: 'perimeter-protection', id: 'turnstiles', driveId: '1If4UG0kRXV5H80Bdv3471IHH1uvKX0kn' },
  { cat: 'perimeter-protection', id: 'tyre-killer', driveId: '1MhKfeUZHzfRF_HA77PaYZPfPH_ZbXzra' },
  { cat: 'perimeter-protection', id: 'under-vehicle-surveillance-system', driveId: '1biFREoyTPkJFFnNfSY9fEDWn44yBwa73' },

  // Loading Systems
  { cat: 'docking-systems', id: 'hydraulic-dock-leveler', driveId: '1pze3d3sw2B1t1aEpFH86ybcDxwOk-IoO' },
  { cat: 'docking-systems', id: 'inflatable-dock-shelter', driveId: '1SlLjpgdmRd_8vPKYYh1oUJPg5Uk_Mx8P' },
  { cat: 'docking-systems', id: 'dock-leveler-inkema', driveId: '1z_wpIQh3FgcGGCDfbzUkifWNS15QKtWU' },
  { cat: 'docking-systems', id: 'manual-loading-bridges', driveId: '1QvS6Jf5smMoiR4Gx4sHbBkYtZKCtpS0W' },
  { cat: 'docking-systems', id: 'minidock', driveId: '1GjMadtbZzhl8dBjnVLsPAe3yNPjsSy0g' },
  { cat: 'docking-systems', id: 'mobile-loading-dock', driveId: '1-b9wANlZxhXcsDZV3OtnGw4hl0iANFW_' },
  { cat: 'docking-systems', id: 'movable-dock-ramp', driveId: '1Js9KDSKcznPkhH12MUHdgd4Qidk2lYWf' },
  { cat: 'docking-systems', id: 'movable-scissors-lifts', driveId: '1TThXH131Gc7wSSOwxFx0uZIpH3AyraS4' },
  { cat: 'docking-systems', id: 'retractable-dock-shelter', driveId: '1PXjOey5ZU-l0CG9q6Vv6I0g_KbXKs0D0' },
  { cat: 'docking-systems', id: 'scissors-lift', driveId: '1CAqLoatSDKw2uQOtKiGVsIYq6QCjM0e2' },
  { cat: 'docking-systems', id: 'wheelchair-lift', driveId: '1UCgNvBqfYcoGn2EHuEVm6NtYuuaw_2J7' },

  // Waste & Recycling
  { cat: 'waste-management', id: 'pringer-compactor', driveId: '1LydHAq1xlQ7uroOXxPnvJta8Xo-6cJD8' },
  { cat: 'waste-management', id: 'persi-compactor', driveId: '1q1sxUcDLJKN8t_Zg3yF3Z3Fn5OUKywSA' },
  { cat: 'waste-management', id: 'auto-horizontal-baler', driveId: '1JeWOdt6lf55aHXh8BPwN_QA6wv72H_aU' },
  { cat: 'waste-management', id: 'horizontal-plastic-baler-70', driveId: '1BWxsUYOPISPp39u4CThGMPF4lbUgD2M_' },
  { cat: 'waste-management', id: 'solar-bin-waste-compactor', driveId: '1sW_EHh35vHgr5v2oBkZqCOvw6q6v1qY2' },
  { cat: 'waste-management', id: 'textile-baler', driveId: '1tVRiNrRjt55ZlsRrTrvTo1eymZlzUWpM' },
  { cat: 'waste-management', id: 'can-bottle-baler-80', driveId: '1ZQ48YQbsou3hknw2rgd2S7H7XlQHKVGv' },
  { cat: 'waste-management', id: 'cardboard-plastic-baler-100', driveId: '1ODtDd2B44x8tbiMCJqqraCz2tK3WSHZL' },
  { cat: 'waste-management', id: 'cardboard-plastic-baler-200', driveId: '1aAgwQhVO5uiSXO3ggp0jQHjJUgQDEJIE' },
  { cat: 'waste-management', id: 'cardboard-plastic-baler-500', driveId: '1TX5OUTa1GkMm8FvX8XRj-c9oCChH5C75' },
  { cat: 'waste-management', id: 'vertical-garbage-compactor-2cy', driveId: '1d_wDBYqolWimrN4jvI8hxbOMSQBU3G3J' }
];

async function downloadFromDrive(driveId, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const url = `https://drive.usercontent.google.com/download?id=${driveId}&export=download`;
      const res = await fetch(url);
      if (res.ok) {
        return Buffer.from(await res.arrayBuffer());
      }
      const fallbackUrl = `https://drive.google.com/uc?export=download&id=${driveId}`;
      const fbRes = await fetch(fallbackUrl);
      if (fbRes.ok) {
        return Buffer.from(await fbRes.arrayBuffer());
      }
    } catch (e) {
      if (attempt === retries) throw e;
      await new Promise(r => setTimeout(r, 1000 * attempt));
    }
  }
  throw new Error(`Failed to download Drive file ${driveId} after ${retries} attempts`);
}

async function uploadToBunny(buffer, remotePath, mimeType) {
  const uploadUrl = `${BASE_STORAGE_URL}/${STORAGE_ZONE_NAME}/${remotePath}`;
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

  return `https://${PULL_ZONE}/${remotePath}`;
}

function normalizeExtension(filename, mime) {
  const extMatch = filename.match(/\.(png|jpe?g|webp)$/i);
  if (extMatch) {
    const ext = extMatch[1].toLowerCase();
    return ext === 'jpeg' ? 'jpg' : ext;
  }
  if (mime === 'image/jpeg') return 'jpg';
  if (mime === 'image/webp') return 'webp';
  return 'png';
}

function sanitizeItemName(item, index, existingNames) {
  const ext = normalizeExtension(item.name || '', item.mime || 'image/png');
  const baseRaw = (item.name || '').replace(/\.(png|jpe?g|webp)$/i, '').trim();

  let targetName = '';

  if (item.isComponent) {
    let cleanBase = arabicTranslations[baseRaw];
    if (!cleanBase) {
      cleanBase = baseRaw
        .toLowerCase()
        .replace(/[\u202A\u202C\u200F\u200E]/g, '')
        .replace(/[^\w\s-]/g, '')
        .trim()
        .replace(/\s+/g, '-');
    }
    if (!cleanBase || cleanBase.length < 2) {
      cleanBase = `part-${index + 1}`;
    }
    targetName = `component-${cleanBase}.${ext}`;
  } else {
    // Main image
    const numMatch = baseRaw.match(/(?:^|\D)(\d+)$/);
    if (numMatch) {
      targetName = `${numMatch[1]}.${ext}`;
    } else {
      let cleanBase = baseRaw
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .trim()
        .replace(/\s+/g, '-');
      targetName = cleanBase ? `${cleanBase}.${ext}` : `${index + 1}.${ext}`;
    }
  }

  // Ensure unique name
  let finalName = targetName;
  let counter = 2;
  while (existingNames.has(finalName)) {
    const nameWithoutExt = targetName.replace(new RegExp(`\\.${ext}$`), '');
    finalName = `${nameWithoutExt}-${counter}.${ext}`;
    counter++;
  }
  existingNames.add(finalName);

  return finalName;
}

async function processProduct(prodConfig) {
  console.log(`\n==================================================`);
  console.log(`Processing Product: [${prodConfig.id}] (${prodConfig.cat})`);
  console.log(`Drive Folder: https://drive.google.com/drive/folders/${prodConfig.driveId}`);

  const rawItems = await getAllImagesInFolder(prodConfig.driveId);
  console.log(`Found total ${rawItems.length} items`);

  // Separate main images and component images
  const mainItems = rawItems.filter(i => !i.isComponent);
  const compItems = rawItems.filter(i => i.isComponent);

  const existingNames = new Set();
  const processedFiles = [];

  // Process main images first
  mainItems.forEach((item, idx) => {
    const safeName = sanitizeItemName(item, idx, existingNames);
    processedFiles.push({ ...item, safeName, priority: 1 });
  });

  // Process components
  compItems.forEach((item, idx) => {
    const safeName = sanitizeItemName(item, idx, existingNames);
    processedFiles.push({ ...item, safeName, priority: 2 });
  });

  // Sort files: numerical main images first (1.png, 2.png, ...), then other mains, then components
  processedFiles.sort((a, b) => {
    if (a.priority !== b.priority) return a.priority - b.priority;
    const numA = parseInt(a.safeName);
    const numB = parseInt(b.safeName);
    if (!isNaN(numA) && !isNaN(numB)) return numA - numB;
    return a.safeName.localeCompare(b.safeName);
  });

  const localTargetDir = path.join('f:/projects/bestolex/public/images/products', prodConfig.id);
  fs.mkdirSync(localTargetDir, { recursive: true });

  const cdnUrls = [];
  let mainCdnUrl = '';

  for (let i = 0; i < processedFiles.length; i++) {
    const file = processedFiles[i];
    console.log(`  [${i + 1}/${processedFiles.length}] Downloading ${file.name} -> ${file.safeName}...`);
    const buf = await downloadFromDrive(file.id);

    // Save locally
    const localPath = path.join(localTargetDir, file.safeName);
    fs.writeFileSync(localPath, buf);

    // Upload to Bunny CDN
    const remotePath = `bestolex/products/${prodConfig.id}/${file.safeName}`;
    const mime = file.mime || (file.safeName.endsWith('.jpg') ? 'image/jpeg' : 'image/png');
    const cdnUrl = await uploadToBunny(buf, remotePath, mime);
    cdnUrls.push(cdnUrl);

    if (i === 0) {
      mainCdnUrl = cdnUrl;
    }
  }

  // Update data/products.json
  const productsFilePath = 'f:/projects/bestolex/data/products.json';
  const categories = JSON.parse(fs.readFileSync(productsFilePath, 'utf8'));

  let found = false;
  for (const cat of categories) {
    for (const prod of (cat.products || [])) {
      if (prod.id === prodConfig.id) {
        prod.cardImage = mainCdnUrl;
        prod.coverImage = mainCdnUrl;
        prod.image = mainCdnUrl;
        prod.images = cdnUrls;
        found = true;
        console.log(`  Updated ${prod.id} in products.json:`);
        console.log(`    Primary Image: ${mainCdnUrl}`);
        console.log(`    Total Images in Gallery: ${cdnUrls.length}`);
      }
    }
  }

  if (!found) {
    console.warn(`WARNING: Product ${prodConfig.id} not found in products.json!`);
  } else {
    fs.writeFileSync(productsFilePath, JSON.stringify(categories, null, 2), 'utf8');
  }

  console.log(`Successfully completed ${prodConfig.id}!`);
}

async function main() {
  const targetCategory = process.argv[2];
  if (!targetCategory) {
    console.error('Usage: node upload_category_batch.mjs <category_id>');
    process.exit(1);
  }

  const prods = allProducts.filter(p => p.cat === targetCategory);
  if (prods.length === 0) {
    console.error(`No products found for category: ${targetCategory}`);
    process.exit(1);
  }

  console.log(`Starting upload batch for category [${targetCategory}] (${prods.length} products)...`);
  const startTime = Date.now();

  for (let idx = 0; idx < prods.length; idx++) {
    const p = prods[idx];
    console.log(`\n>>> Product ${idx + 1} of ${prods.length}: ${p.id} <<<`);
    await processProduct(p);
  }

  const totalTime = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n==================================================`);
  console.log(`All ${prods.length} products for [${targetCategory}] processed successfully in ${totalTime}s!`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
