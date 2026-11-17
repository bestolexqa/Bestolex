import fs from 'fs';
import path from 'path';

const STORAGE_ZONE_NAME = 'electrocreative-zone';
const ACCESS_KEY = process.env.BUNNY_STORAGE_ACCESS_KEY;
const PULL_ZONE = 'electrocreative-cdn.b-cdn.net';
const BASE_STORAGE_URL = 'https://storage.bunnycdn.com';

const filesToDownload = [
  {
    name: '1.png',
    title: 'Steel Press 50T - Main 3D View',
    driveId: '1MtmMMLTaVKLt__bW7R_9MpettPMG6zhr',
    isMain: true
  },
  {
    name: '2.png',
    title: 'Steel Press 50T - Side View',
    driveId: '1uNW4q4W5TF2q6Tybi3C0wH6xt9PX2pgZ'
  },
  {
    name: '3.png',
    title: 'Steel Press 50T - Front View',
    driveId: '1kinwSLjT3J1HqIqxHusPqdypNWYIBPFI'
  },
  {
    name: 'component-discharge-door.png',
    title: 'Discharge Door',
    driveId: '1rBb_cuJ9f00N8b97wC3W2oTamZhshnnP'
  },
  {
    name: 'component-electric-motor.png',
    title: 'Electric Motor',
    driveId: '1-epeOVU69JJlAOm2HEILZOMToF8dzbkW'
  },
  {
    name: 'component-electrical-panel.png',
    title: 'Electrical Panel',
    driveId: '130J_sGw_24qNSrKEAsfsewpND6WvEJQA'
  },
  {
    name: 'component-hydraulic-gauge.png',
    title: 'Hydraulic Gauge',
    driveId: '1kZh9-ONruzU0AxkeFRxNr32QCjm3lKyY'
  },
  {
    name: 'component-hydraulic-pump.png',
    title: 'Hydraulic Pump',
    driveId: '1cwSXEBx8idMqEzififnkO9LFIcUlX9jF'
  },
  {
    name: 'component-manual-control-valve.png',
    title: 'Manual Control Valve',
    driveId: '1MzPeJMyusEVy7HfvUuXW7aDLHHmhOgio'
  },
  {
    name: 'component-movable-pusher.png',
    title: 'Movable Pusher',
    driveId: '1UqD4S2sCn5LljEMcGU1CrL9vrkqOXYfG'
  },
  {
    name: 'component-upper-loading-door.png',
    title: 'Upper Loading Door',
    driveId: '1cZDdhcawel1_ULqfPI5Ht5PSdwE36ca_'
  }
];

async function downloadFromDrive(driveId) {
  const url = `https://drive.usercontent.google.com/download?id=${driveId}&export=download`;
  const res = await fetch(url);
  if (!res.ok) {
    // Fallback to uc?export=download
    const fallbackUrl = `https://drive.google.com/uc?export=download&id=${driveId}`;
    const fbRes = await fetch(fallbackUrl);
    if (!fbRes.ok) {
      throw new Error(`Failed to download ${driveId}: ${res.status} / ${fbRes.status}`);
    }
    return Buffer.from(await fbRes.arrayBuffer());
  }
  return Buffer.from(await res.arrayBuffer());
}

async function uploadToBunny(buffer, remotePath, mimeType) {
  const uploadUrl = `${BASE_STORAGE_URL}/${STORAGE_ZONE_NAME}/${remotePath}`;
  console.log(`Uploading to Bunny: ${uploadUrl}...`);

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
  const localTargetDir = 'f:/projects/bestolex/public/images/products/steel-press-50t';
  fs.mkdirSync(localTargetDir, { recursive: true });

  const cdnUrls = [];
  let mainCdnUrl = '';

  for (const item of filesToDownload) {
    console.log(`\nDownloading ${item.name} (${item.title}) from Drive ID ${item.driveId}...`);
    const buf = await downloadFromDrive(item.driveId);
    console.log(`Downloaded ${item.name}: ${buf.length} bytes`);

    // 1. Save locally
    const localPath = path.join(localTargetDir, item.name);
    fs.writeFileSync(localPath, buf);
    console.log(`Saved locally: ${localPath}`);

    // 2. Upload to Bunny CDN
    const remotePath = `bestolex/products/steel-press-50t/${item.name}`;
    const cdnUrl = await uploadToBunny(buf, remotePath, 'image/png');
    cdnUrls.push(cdnUrl);

    if (item.isMain) {
      mainCdnUrl = cdnUrl;
    }
  }

  // 3. Update data/products.json
  const productsFilePath = 'f:/projects/bestolex/data/products.json';
  const categories = JSON.parse(fs.readFileSync(productsFilePath, 'utf8'));

  let found = false;
  for (const cat of categories) {
    for (const prod of (cat.products || [])) {
      if (prod.id === 'steel-press-50t') {
        prod.cardImage = mainCdnUrl;
        prod.coverImage = mainCdnUrl;
        prod.image = mainCdnUrl;
        prod.images = cdnUrls;
        found = true;
        console.log(`\nUpdated steel-press-50t in products.json:`);
        console.log(`  cardImage: ${prod.cardImage}`);
        console.log(`  coverImage: ${prod.coverImage}`);
        console.log(`  total images in gallery: ${prod.images.length}`);
      }
    }
  }

  if (!found) {
    throw new Error('Product steel-press-50t not found in products.json');
  }

  fs.writeFileSync(productsFilePath, JSON.stringify(categories, null, 2), 'utf8');
  console.log('\nproducts.json successfully updated with all 11 new high-res professional images!');
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
