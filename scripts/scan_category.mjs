import { getAllImagesInFolder } from './drive_scanner_helper.mjs';

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

async function scanCategory(catName) {
  const prods = allProducts.filter(p => p.cat === catName);
  console.log(`\n=== Scanning ${catName} (${prods.length} products) ===`);
  for (const p of prods) {
    const images = await getAllImagesInFolder(p.driveId);
    console.log(`Product [${p.id}] -> ${images.length} images:`);
    images.forEach(img => {
      console.log(`  - ${img.isComponent ? '[COMP] ' : '[MAIN] '} ${img.name}`);
    });
  }
}

async function main() {
  const cat = process.argv[2] || 'industrial-doors';
  await scanCategory(cat);
}

main().catch(console.error);
