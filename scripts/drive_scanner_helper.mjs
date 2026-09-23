import https from 'https';

export function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

export function extractDriveItems(html) {
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
            if (arr[35] && Array.isArray(arr[35]) && arr[35][0]) {
              const val = arr[35][0][0];
              name = Array.isArray(val) ? val[0] : val;
            }
            if (typeof name === 'string') {
              name = name.trim();
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

export async function getAllImagesInFolder(folderId) {
  const html = await fetchUrl('https://drive.google.com/drive/folders/' + folderId);
  const items = extractDriveItems(html);
  
  let files = [];
  for (const item of items) {
    if (item.isFolder) {
      console.log(`  -> Found subfolder: ${item.name} (${item.id})`);
      // Recursively fetch subfolder
      const subHtml = await fetchUrl('https://drive.google.com/drive/folders/' + item.id);
      const subItems = extractDriveItems(subHtml);
      for (const sub of subItems) {
        if (!sub.isFolder && (sub.mime.startsWith('image/') || sub.name?.match(/\.(png|jpe?g|webp)$/i))) {
          files.push({ ...sub, isComponent: true });
        }
      }
    } else if (item.mime?.startsWith('image/') || item.name?.match(/\.(png|jpe?g|webp)$/i)) {
      files.push({ ...item, isComponent: false });
    }
  }
  return files;
}
