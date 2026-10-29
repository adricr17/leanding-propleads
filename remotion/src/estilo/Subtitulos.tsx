import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {ESTILO} from './tokens';

// acento = naranja y 2,2× (cifras) · color = naranja al tamaño normal (palabra clave) · quien = nombre de quien habla
export type Palabra = {texto: string; inicio: number; fin: number; acento?: boolean; color?: boolean; meme?: boolean; quien?: string};

// Una palabra cada vez, sin animación (estilo.md §2). Se mantiene hasta la siguiente si el hueco < 0,35 s.
export const Subtitulos: React.FC<{palabras: Palabra[]; y?: number}> = ({palabras, y = ESTILO.subtitulo.yCentro}) => {
  const t = useCurrentFrame() / useVideoConfig().fps;
  const i = palabras.findIndex((p, k) => {
    const sig = palabras[k + 1];
    const fin = sig && sig.inicio - p.fin < 0.35 ? sig.inicio : p.fin + 0.1;
    return t >= p.inicio && t < fin;
  });
  if (i < 0) return null;
  const p = palabras[i];
  const color = p.meme ? ESTILO.amarilloMeme : p.acento || p.color ? ESTILO.naranja : ESTILO.blanco;
  const tamano = p.meme ? 64 : p.acento ? ESTILO.subtitulo.tamanoAcento : ESTILO.subtitulo.tamano;
  return (
    <AbsoluteFill style={{alignItems: 'center'}}>
      <div
        style={{
          position: 'absolute',
          top: `${y * 100}%`,
          transform: 'translateY(-50%)',
          fontFamily: p.meme ? 'Inter' : 'Inter',
          fontSize: tamano,
          lineHeight: 1,
          color,
          textAlign: 'center',
          padding: '0 60px',
          textShadow: `0 0 10px ${color}73, 0 4px 6px rgba(0,0,0,.6), 0 0 2px rgba(0,0,0,.6)`,
        }}
      >
        {p.quien && (
          <div style={{position: 'absolute', bottom: '100%', left: 0, right: 0, fontFamily: 'SpaceMono', fontSize: 34, letterSpacing: 4, color: ESTILO.naranja, marginBottom: 16, textShadow: '0 3px 6px rgba(0,0,0,.7)'}}>
            {p.quien}
          </div>
        )}
        {p.texto}
      </div>
    </AbsoluteFill>
  );
};
