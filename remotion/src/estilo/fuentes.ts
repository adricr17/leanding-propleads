import {continueRender, delayRender, staticFile} from 'remotion';

// Fuentes del estilo PHARAON (ver estilo.md). Se cargan una vez antes de renderizar.
const FUENTES: [string, string][] = [
  ['Inter', 'fuentes/Inter-ExtraBold.otf'],
  ['Anton', 'fuentes/Anton-Regular.ttf'],
  ['SpaceMono', 'fuentes/SpaceMono-700.ttf'],
  ['SerifCursiva', 'fuentes/FreeSerifBoldItalic.ttf'],
];

let cargadas = false;
export const cargaFuentes = () => {
  if (cargadas || typeof document === 'undefined') return;
  cargadas = true;
  const h = delayRender('fuentes');
  Promise.all(
    FUENTES.map(([familia, ruta]) => {
      const f = new FontFace(familia, `url(${staticFile(ruta)})`);
      document.fonts.add(f);
      return f.load();
    }),
  ).then(() => continueRender(h));
};
