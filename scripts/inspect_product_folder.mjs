import https from 'https';
import fs from 'fs';

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

async function main() {
  const folderId = '1LqvI9FAnV2IpaxJFtOTu2L0Gass1e5Xu'; // High-speed Roll doors
  const html = await fetchUrl('https://drive.google.com/drive/folders/' + folderId);
  fs.writeFileSync('scripts/sample_folder.html', html, 'utf-8');

  // Find all file occurrences
  const imageNames = [...html.matchAll(/([a-zA-Z0-9_\-\s]+\.(?:png|jpg|jpeg|webp|pdf))/gi)].map(m => m[1]);
  console.log('Image names found:', Array.from(new Set(imageNames)));

  // Find all ssk patterns
  const sskList = [...html.matchAll(/ssk=['"][^'"]*?([a-zA-Z0-9_-]{28,35})/g)].map(m => m[1]);
  console.log('SSK IDs:', Array.from(new Set(sskList)));
}

main().catch(console.error);
