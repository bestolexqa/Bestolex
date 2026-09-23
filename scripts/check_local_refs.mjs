import fs from 'fs';
import path from 'path';

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    if (['node_modules', '.git', '.nuxt', '.output', 'dist', 'public', 'scripts'].includes(file)) return;
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat && stat.isDirectory()) {
      results = results.concat(walk(full));
    } else {
      results.push(full);
    }
  });
  return results;
}

const files = walk('.');
let foundAny = false;
for (const file of files) {
  const content = fs.readFileSync(file, 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    if (line.includes('"/images/') || line.includes("'/images/")) {
      console.log(`FOUND in ${file}:${idx+1} -> ${line.trim()}`);
      foundAny = true;
    }
  });
}

if (!foundAny) {
  console.log('SUCCESS: ZERO local /images/ references remain in the entire codebase!');
}
