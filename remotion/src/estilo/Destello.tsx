import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

// Light leak de 6 fotogramas: naranja-rojo → blanco (pico en el central) → naranja (estilo.md §5).
export const Destello: React.FC = () => {
  const f = useCurrentFrame();
  const blanco = interpolate(f, [0, 3, 6], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const naranja = interpolate(f, [0, 2, 4, 6], [0.2, 0.9, 0.9, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 30% 40%, #FFB347 0%, #FF5A1F 55%, #B3122A 100%)', opacity: naranja, mixBlendMode: 'screen'}} />
      <AbsoluteFill style={{background: '#FFF8E8', opacity: blanco}} />
    </AbsoluteFill>
  );
};

// Tinte cálido tras el destello: degradado #FF5A1F→#FFB347 que se va apagando (estilo.md §7).
export const Tinte: React.FC<{frames: number}> = ({frames}) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [0, frames], [0.5, 0], {extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{background: 'linear-gradient(160deg, #FF5A1F 0%, #FFB347 70%, rgba(255,179,71,0) 100%)', opacity: o, mixBlendMode: 'soft-light'}} />;
};
