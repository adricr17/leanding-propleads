// Renderiza cada .slide de un HTML a PNG de 1080x1350.
// Uso: node posts/_base/render.js posts/tanda2/bingo.html [más html...]
// Salida: carpeta con el nombre del html, junto a él (bingo/01.png, 02.png...).
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const file of process.argv.slice(2)) {
    const abs = path.resolve(file);
    const outDir = abs.replace(/\.html$/, '');
    fs.rmSync(outDir, { recursive: true, force: true });
    fs.mkdirSync(outDir, { recursive: true });
    await page.goto('file://' + abs);
    await page.evaluate(() => document.fonts.ready);
    const slides = await page.$$('.slide');
    for (let i = 0; i < slides.length; i++) {
      await slides[i].screenshot({ path: path.join(outDir, String(i + 1).padStart(2, '0') + '.png') });
    }
    console.log(`${path.relative(process.cwd(), abs)}: ${slides.length} diapositivas`);
  }
  await browser.close();
})();
