import https from 'https';

function fetchFolder(id) {
  return new Promise((resolve, reject) => {
    https.get('https://drive.google.com/drive/folders/' + id, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

const folderIds = [
  '1-lc_A-Z6XWfZwtAvgwgk6y7J7BL_P6D3',
  '158Lc5EhRk9Zx_WVpS_3iF3bYgagD4HYV',
  '12r1MT8yDJFCextTAQW4VEd8ksYQzd7qo',
  '1EUoc1lVOYw1BkYHFK92WND9LzYk6jk9A'
];

async function main() {
  for (const id of folderIds) {
    const html = await fetchFolder(id);
    const titleMatch = html.match(/<title>([^<]+)<\/title>/);
    const title = titleMatch ? titleMatch[1].replace(' - Google Drive', '') : 'Unknown';

    const sskMatches = [...html.matchAll(/ssk=['"][^'"]*?([a-zA-Z0-9_-]{28,35})/g)].map(m => m[1]);
    const cleanIds = Array.from(new Set(sskMatches.map(i => i.replace(/-0$/, '')))).filter(i => i !== id);
    console.log(`\nFolder [${title}] (ID: ${id}):`);
    console.log(`Child IDs (${cleanIds.length}):`, cleanIds);
  }
}

main().catch(console.error);
