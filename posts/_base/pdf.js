// Genera un PDF (una página de 1080x1350 por diapositiva) para importarlo en Canva.
// Uso: node posts/_base/pdf.js posts/tanda2/bingo.html [más html...]  → bingo.pdf junto al html
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const file of process.argv.slice(2)) {
    const abs = path.resolve(file);
    await page.goto('file://' + abs);
    await page.addStyleTag({ content: '@page { size: 1080px 1350px; margin: 0 } body { background: none } .slide { margin: 0 !important; break-after: page; }' });
    await page.evaluate(() => document.fonts.ready);
    const out = abs.replace(/\.html$/, '.pdf');
    await page.pdf({ path: out, width: '1080px', height: '1350px', printBackground: true });
    console.log(path.relative(process.cwd(), out));
  }
  await browser.close();
})();
