// Edición del susto a Siz0 (29/10/2026). Tiempos en segundos del clip de origen.
// v1 = preparación (8,3 s, 30 fps) · v2 = el susto (38,7 s, 24 fps; del 37 s en adelante es la cortinilla de CapCut y no se usa).
export type Plano = {
  src: 'v1.mp4' | 'v2.mp4' | 'negro';
  desde: number;
  hasta: number;
  bn?: boolean;          // blanco y negro (preparación)
  zoom?: number;         // punch-in seco
  ficha?: [string, string];
  destelloAntes?: boolean;
  efecto?: [string, number]; // [archivo de public/sfx, volumen] al empezar el plano
};

export const PLANOS: Plano[] = [
  {src: 'v1.mp4', desde: 0.0, hasta: 1.0, bn: true, efecto: ['trueno.mp3', 0.4]},
  {src: 'v1.mp4', desde: 1.55, hasta: 2.3, bn: true, zoom: 1.12, ficha: ['EL SUSTO', 'ANDREA']},
  {src: 'v1.mp4', desde: 2.5, hasta: 4.2, bn: true, ficha: ['LOS PLOMOS', 'ADRI']},
  {src: 'v1.mp4', desde: 6.4, hasta: 8.1, bn: true, zoom: 1.15},
  {src: 'v2.mp4', desde: 2.6, hasta: 4.4, destelloAntes: true, efecto: ['whoosh.mp3', 0.6], ficha: ['LA CÁMARA', 'URI']},
  {src: 'negro', desde: 0, hasta: 0.2, efecto: ['desenchufe.mp3', 0.8]},
  {src: 'v2.mp4', desde: 4.6, hasta: 6.6},
  {src: 'v2.mp4', desde: 7.6, hasta: 9.4, zoom: 1.12},
  {src: 'v2.mp4', desde: 10.3, hasta: 12.0, zoom: 1.12, ficha: ['LA VÍCTIMA', 'KIKE']},
  {src: 'v2.mp4', desde: 12.4, hasta: 14.5},
  {src: 'v2.mp4', desde: 18.0, hasta: 19.6, destelloAntes: true, efecto: ['impacto.mp3', 0.7]},
  {src: 'v2.mp4', desde: 19.6, hasta: 20.4},
  {src: 'v2.mp4', desde: 20.6, hasta: 24.2, ficha: ['OYÓ LOS GRITOS', 'MEI']},
  {src: 'v2.mp4', desde: 25.0, hasta: 27.3, destelloAntes: true, efecto: ['whoosh.mp3', 0.6]},
  {src: 'v2.mp4', desde: 28.7, hasta: 30.9, zoom: 1.15},
  {src: 'v2.mp4', desde: 32.0, hasta: 34.62},
  {src: 'v2.mp4', desde: 34.62, hasta: 36.6, zoom: 1.15},
];

export const FPS = 30;
export const framesDe = (p: Plano) => Math.round((p.hasta - p.desde) * FPS);
export const DURACION = PLANOS.reduce((s, p) => s + framesDe(p), 0);
