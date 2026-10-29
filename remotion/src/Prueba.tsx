import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

export const Prueba: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{background: '#111', justifyContent: 'center', alignItems: 'center'}}>
      <div style={{color: '#FF8A1F', fontSize: 140, fontFamily: 'sans-serif', fontWeight: 900, opacity: interpolate(f, [0, 15], [0, 1])}}>
        PHARAON
      </div>
    </AbsoluteFill>
  );
};
