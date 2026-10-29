import React from 'react';
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, staticFile} from 'remotion';
import {cargaFuentes} from '../estilo/fuentes';
import {Destello, Tinte} from '../estilo/Destello';
import {Ficha, RotuloEntrada} from '../estilo/Rotulos';
import {Palabra, Subtitulos} from '../estilo/Subtitulos';
import {ESTILO} from '../estilo/tokens';
import {FPS, framesDe, PLANOS} from './edicion';
import palabras from './palabras.json';

cargaFuentes();

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
      <Subtitulos palabras={palabras as Palabra[]} />
    </AbsoluteFill>
  );
};
