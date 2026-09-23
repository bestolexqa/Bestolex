import fs from 'fs';
import path from 'path';

function walkDir(dir, fileList = []) {
  for (const it of fs.readdirSync(dir)) {
    if (['node_modules', '.git', '.nuxt', '.output', 'dist'].includes(it)) continue;
    const full = path.join(dir, it);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      walkDir(full, fileList);
    } else if (it.endsWith('.vue') || it.endsWith('.ts') || it.endsWith('.json')) {
      fileList.push(full);
    }
  }
  return fileList;
}

const allFiles = walkDir('.');
const localRefs = new Map();

for (const f of allFiles) {
  const content = fs.readFileSync(f, 'utf8');
  // Look for /images/... or /logo...
  const regex = /['"`](\/images\/[^'"`]+)['"`]/g;
  let m;
  while ((m = regex.exec(content)) !== null) {
    const list = localRefs.get(m[1]) || [];
    list.push(f);
    localRefs.set(m[1], list);
  }
}

console.log(`Found ${localRefs.size} unique /images/ references across project:`);
for (const [img, files] of localRefs.entries()) {
  console.log(`  ${img} -> referenced in ${files.length} files:`);
  files.forEach(f => console.log(`     ${f}`));
}
