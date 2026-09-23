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

async function getFolderInfo(id) {
  try {
    const html = await fetchUrl('https://drive.google.com/drive/folders/' + id);
    const titleMatch = html.match(/<title>([^<]+)<\/title>/);
    const title = titleMatch ? titleMatch[1].replace(' - Google Drive', '').replace(/[\u202A\u202C\u200F\u200E]/g, '').trim() : 'Unknown';
    
    const sskMatches = [...html.matchAll(/ssk=['"][^'"]*?([a-zA-Z0-9_-]{28,35})/g)].map(m => m[1]);
    const cleanIds = Array.from(new Set(sskMatches.map(i => i.replace(/-0$/, '')))).filter(i => i !== id);
    
    return { id, title, childIds: cleanIds };
  } catch (err) {
    return { id, title: 'Error: ' + err.message, childIds: [] };
  }
}

async function main() {
  console.log('--- Scanning Loading Systems ---');
  const loading = [
    '1pze3d3sw2B1t1aEpFH86ybcDxwOk-IoO',
    '1SlLjpgdmRd_8vPKYYh1oUJPg5Uk_Mx8P',
    '1z_wpIQh3FgcGGCDfbzUkifWNS15QKtWU',
    '1QvS6Jf5smMoiR4Gx4sHbBkYtZKCtpS0W',
    '1GjMadtbZzhl8dBjnVLsPAe3yNPjsSy0g',
    '1-b9wANlZxhXcsDZV3OtnGw4hl0iANFW_',
    '1Js9KDSKcznPkhH12MUHdgd4Qidk2lYWf',
    '1TThXH131Gc7wSSOwxFx0uZIpH3AyraS4',
    '1PXjOey5ZU-l0CG9q6Vv6I0g_KbXKs0D0',
    '1CAqLoatSDKw2uQOtKiGVsIYq6QCjM0e2',
    '1UCgNvBqfYcoGn2EHuEVm6NtYuuaw_2J7'
  ];
  for (const id of loading) {
    const info = await getFolderInfo(id);
    console.log(`Product Folder [${info.title}] (ID: ${id}) has ${info.childIds.length} items`);
  }

  console.log('\n--- Scanning Waste & Recycling ---');
  const waste = [
    '1LydHAq1xlQ7uroOXxPnvJta8Xo-6cJD8',
    '1q1sxUcDLJKN8t_Zg3yF3Z3Fn5OUKywSA',
    '1JeWOdt6lf55aHXh8BPwN_QA6wv72H_aU',
    '1BWxsUYOPISPp39u4CThGMPF4lbUgD2M_',
    '1sW_EHh35vHgr5v2oBkZqCOvw6q6v1qY2',
    '1W17aUF9UrfRjTX-B5FpIckQ-755Rxm36',
    '1tVRiNrRjt55ZlsRrTrvTo1eymZlzUWpM',
    '1ZQ48YQbsou3hknw2rgd2S7H7XlQHKVGv',
    '1ODtDd2B44x8tbiMCJqqraCz2tK3WSHZL',
    '1aAgwQhVO5uiSXO3ggp0jQHjJUgQDEJIE',
    '1TX5OUTa1GkMm8FvX8XRj-c9oCChH5C75',
    '1d_wDBYqolWimrN4jvI8hxbOMSQBU3G3J'
  ];
  for (const id of waste) {
    const info = await getFolderInfo(id);
    console.log(`Product Folder [${info.title}] (ID: ${id}) has ${info.childIds.length} items`);
  }
}

main().catch(console.error);
