import { fetchUrl, extractDriveItems } from './drive_scanner_helper.mjs';

async function main() {
  const folderId = '158Lc5EhRk9Zx_WVpS_3iF3bYgagD4HYV';
  const html = await fetchUrl('https://drive.google.com/drive/folders/' + folderId);
  const items = extractDriveItems(html);
  console.log('Loading Systems Folders:');
  items.forEach(it => console.log(`[${it.id}] ${it.name} (isFolder: ${it.isFolder})`));
}

main().catch(console.error);
