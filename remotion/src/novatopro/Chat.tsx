import React from 'react';
import {interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

// Pantalla de DM simplificada: cabecera con @pharaonstudio y burbujas que aparecen con un «pop».
export type Burbuja = {desde: number; texto?: string; lineas?: string[]; mia?: boolean; tipo?: 'texto' | 'audio' | 'foto'; lineaCada?: number};
const NEGRO = '#111111', MORADO = '#9925AE', HUESO = '#EFEBE4';

const Pop: React.FC<{desde: number; children: React.ReactNode; mia?: boolean}> = ({desde, children, mia}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  if (f < desde) return null;
  const s = spring({frame: f - desde, fps, config: {damping: 12, stiffness: 220}});
  return <div style={{alignSelf: mia ? 'flex-end' : 'flex-start', transform: `scale(${s})`, transformOrigin: mia ? 'right bottom' : 'left bottom', marginTop: 12}}>{children}</div>;
};

export const Chat: React.FC<{burbujas: Burbuja[]; visto?: number; vacio?: number}> = ({burbujas, visto, vacio}) => {
  const f = useCurrentFrame();
  const opa = vacio !== undefined ? interpolate(f, [vacio, vacio + 8], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 1;
  return (
    <div style={{width: 480, height: 640, background: '#fff', border: `7px solid ${NEGRO}`, borderRadius: 44, overflow: 'hidden', display: 'flex', flexDirection: 'column', boxShadow: '10px 10px 0 #111'}}>
      <div style={{background: NEGRO, color: '#fff', fontFamily: 'SpaceMono', fontSize: 24, padding: '18px 22px', letterSpacing: 1}}>@pharaonstudio</div>
      <div style={{flex: 1, minHeight: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', padding: '14px 18px 20px', opacity: opa}}>
        {burbujas.map((b, i) => {
          const fondo = b.mia ? NEGRO : HUESO, color = b.mia ? '#fff' : NEGRO;
          let cont: React.ReactNode = b.texto;
          if (b.lineas) cont = b.lineas.map((l, k) => (f >= b.desde + k * (b.lineaCada ?? 6) ? <div key={k}>✔ {l}</div> : null));
          if (b.tipo === 'audio') {
            const ancho = interpolate(f, [b.desde, b.desde + 40], [60, 300], {extrapolateRight: 'clamp'});
            cont = (
              <div style={{display: 'flex', alignItems: 'center', gap: 12}}>
                🎤 <div style={{height: 10, width: ancho, background: `repeating-linear-gradient(90deg,#fff 0 6px,transparent 6px 11px)`}} /> 3:47
              </div>
            );
          }
          if (b.tipo === 'foto') {
            cont = (
              <div style={{width: 200, height: 150, borderRadius: 16, background: HUESO, border: '4px solid #fff', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <svg width={110} height={110} viewBox="0 0 100 100"><circle cx={50} cy={42} r={22} fill="none" stroke={MORADO} strokeWidth={6} /><path d="M50 64 L50 96 M50 80 Q36 72 30 80" stroke={NEGRO} strokeWidth={6} fill="none" /><path d="M40 40 Q50 28 60 40 Q50 50 40 40" fill={MORADO} /></svg>
              </div>
            );
          }
          return (
            <Pop key={i} desde={b.desde} mia={b.mia}>
              <div style={{background: b.tipo === 'foto' ? MORADO : fondo, color, fontFamily: 'DMSans', fontWeight: 700, fontSize: 30, lineHeight: 1.3, padding: b.tipo === 'foto' ? 8 : '12px 20px', borderRadius: 26, maxWidth: 400}}>{cont}</div>
            </Pop>
          );
        })}
        {visto !== undefined && f >= visto && <div style={{alignSelf: 'flex-end', fontFamily: 'DMSans', fontSize: 22, color: '#888', marginTop: 6}}>Visto</div>}
      </div>
    </div>
  );
};
