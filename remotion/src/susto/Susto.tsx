import React from 'react';
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, staticFile} from 'remotion';
import {cargaFuentes} from '../estilo/fuentes';
import {Destello, Tinte} from '../estilo/Destello';
import {Ficha, RotuloEntrada} from '../estilo/Rotulos';
import {Palabra, Subtitulos} from '../estilo/Subtitulos';
import {ESTILO} from '../estilo/tokens';
import {FPS, framesDe, PLANOS} from './edicion';
import fuente from './palabras_fuente.json';

cargaFuentes();

type PalabraFuente = Palabra & {src: string};

// Pasa los tiempos del clip de origen a la línea de tiempo del montaje (los planos pueden cambiar sin rehacer nada).
const aMontaje = (palabras: PalabraFuente[]): Palabra[] => {
  const out: Palabra[] = [];
  let t = 0;
  for (const p of PLANOS) {
    const ini = t / FPS;
    for (const w of palabras) {
      if (w.src === p.src && w.inicio >= p.desde && w.inicio < p.hasta) {
        out.push({...w, inicio: ini + w.inicio - p.desde, fin: ini + Math.min(w.fin, p.hasta) - p.desde});
      }
    }
    t += framesDe(p);
  }
  return out;
};
const PALABRAS = aMontaje(fuente as PalabraFuente[]);

export const Susto: React.FC = () => {
  let t = 0;
  const bloques = PLANOS.map((p, i) => {
    const desde = t;
    t += framesDe(p);
    return {p, i, desde, dur: framesDe(p)};
  });
  return (
    <AbsoluteFill style={{background: '#000'}}>
      {bloques.map(({p, i, desde, dur}) => (
        <Sequence key={i} from={desde} durationInFrames={dur}>
          {p.src !== 'negro' && (
            <AbsoluteFill style={{transform: `scale(${p.zoom ?? 1})`, filter: p.bn ? 'grayscale(1) contrast(1.25)' : 'saturate(0.85)'}}>
              <OffthreadVideo src={staticFile(p.src)} startFrom={Math.round(p.desde * FPS)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
            </AbsoluteFill>
          )}
          {p.destelloAntes && <Tinte frames={ESTILO.tinteSegundos * FPS} />}
          {p.ficha && (
            <Sequence from={4}>
              <Ficha rol={p.ficha[0]} nombre={p.ficha[1]} />
            </Sequence>
          )}
          {p.efecto && <Audio src={staticFile(`sfx/${p.efecto[0]}`)} volume={p.efecto[1]} />}
        </Sequence>
      ))}
      {/* destellos centrados en el corte */}
      {bloques.filter(({p}) => p.destelloAntes).map(({desde, i}) => (
        <Sequence key={`d${i}`} from={desde - 3} durationInFrames={ESTILO.destelloFrames + 1}>
          <Destello />
        </Sequence>
      ))}
      <Sequence from={0} durationInFrames={Math.round(1.0 * FPS)}>
        <RotuloEntrada arriba="El susto" abajo="A SIZ0" />
      </Sequence>
      <Subtitulos palabras={PALABRAS} />
    </AbsoluteFill>
  );
};
