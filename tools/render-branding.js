// Renders brand/assets/src/*.html to brand/assets/*.png with the preinstalled Playwright Chromium.
// Usage: node tools/render-branding.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const src = path.join(__dirname, '..', 'brand', 'assets', 'src');
  const out = path.join(src, '..');
  const b = await chromium.launch();
  async function shot(file, w, h, png) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.join(src, file));
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(out, png) });
    await p.close();
  }
  await shot('logo.html', 800, 800, 'logo.png');      // banner embeds logo.png, so render it first
  await shot('banner.html', 2560, 1440, 'banner.png');
  await b.close();
})();
