import https from 'https';

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

function extractDriveItems(html) {
  const callbacks = [...html.matchAll(/AF_initDataCallback\((\{.*?\})\);<\/script>/gs)];
  const items = [];

  for (const cb of callbacks) {
    try {
      const obj = (new Function('return ' + cb[1]))();
      if (!obj || !obj.data) continue;

      function findItems(arr) {
        if (!arr || typeof arr !== 'object') return;
        if (Array.isArray(arr) && arr.length >= 36) {
          if (Array.isArray(arr[0]) && arr[0][0] === null && typeof arr[0][1] === 'string' && arr[0][1].length > 20) {
            const id = arr[0][1];
            const mime = arr[4];
            let name = null;
            if (arr[35] && Array.isArray(arr[35]) && arr[35][0] && Array.isArray(arr[35][0])) {
              name = arr[35][0][0];
            }
            items.push({ id, mime, name, isFolder: mime === 'application/vnd.google-apps.folder' });
          }
        }
        for (const k of Object.keys(arr)) {
          findItems(arr[k]);
        }
      }

      findItems(obj.data);
    } catch (e) {
      // ignore
    }
  }

  const map = new Map();
  for (const it of items) {
    if (!map.has(it.id)) map.set(it.id, it);
  }
  return Array.from(map.values());
}

async function main() {
  const subfolderId = '1Q3hJ_u-CGaKd5z_Hd-pQoGt25LIjJ4IY';
  const html = await fetchUrl('https://drive.google.com/drive/folders/' + subfolderId);
  const items = extractDriveItems(html);
  console.log('Subfolder items:');
  console.log(items);
}

main().catch(console.error);
