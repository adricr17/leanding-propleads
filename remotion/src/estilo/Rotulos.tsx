import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {ESTILO} from './tokens';

const sombra = (c: string) => `0 0 14px ${c}80, 0 5px 8px rgba(0,0,0,.65)`;

// Rótulo de entrada: línea 1 serif cursiva escrita letra a letra (2 letras/fotograma), línea 2 condensada (estilo.md §3).
export const RotuloEntrada: React.FC<{arriba: string; abajo: string}> = ({arriba, abajo}) => {
  const f = useCurrentFrame();
  const letras = Math.min(arriba.length, Math.floor(f * 2));
  const abajoVisible = f >= Math.ceil(arriba.length / 2) + 1;
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', flexDirection: 'column'}}>
      <div style={{fontFamily: 'SerifCursiva', fontSize: 150, color: ESTILO.naranja, textShadow: sombra(ESTILO.naranja), lineHeight: 1, marginTop: -120}}>
        {arriba.slice(0, letras)}
      </div>
      <div style={{fontFamily: 'Anton', fontSize: 210, color: '#fff', textShadow: sombra('#000'), lineHeight: 1, marginTop: 10, opacity: abajoVisible ? 1 : 0}}>
        {abajo}
      </div>
    </AbsoluteFill>
  );
};

// Ficha de cómplice: «LOS PLOMOS» en mono naranja + nombre en condensada blanca, abajo a la izquierda.
export const Ficha: React.FC<{rol: string; nombre: string}> = ({rol, nombre}) => {
  const f = useCurrentFrame();
  const x = interpolate(f, [0, 4], [-40, 0], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: 70, bottom: 330, transform: `translateX(${x}px)`}}>
        <div style={{fontFamily: 'SpaceMono', fontSize: 40, letterSpacing: 4, color: ESTILO.naranja, textShadow: sombra('#000')}}>{rol}</div>
        <div style={{fontFamily: 'Anton', fontSize: 150, lineHeight: 0.95, color: '#fff', textShadow: sombra('#000')}}>{nombre}</div>
      </div>
    </AbsoluteFill>
  );
};
