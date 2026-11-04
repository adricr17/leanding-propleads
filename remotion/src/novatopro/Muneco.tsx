import React from 'react';

// Muñeco 2D plano: cabeza blanca con contorno negro, ojos grandes, cuerpo negro. Mismo dibujo para los dos;
// el PRO lleva gafas y párpados a media asta (tranquilo). Caja de 420x560.
export type Cara = 'normal' | 'nervioso' | 'mira' | 'feliz' | 'aburrido' | 'sorpresa';
const NEGRO = '#111111', BLANCO = '#FFFFFF', MORADO = '#9925AE';

export const Muneco: React.FC<{
  pro?: boolean; cara?: Cara; bob?: number; temblor?: number; salto?: number; brazo?: 'movil' | 'medir' | 'cafe' | 'abajo'; sudor?: boolean;
}> = ({pro = false, cara = 'normal', bob = 0, temblor = 0, salto = 0, brazo = 'movil', sudor = false}) => {
  const ox = temblor, oy = bob - salto;
  const ojoAlto = cara === 'sorpresa' ? 44 : cara === 'aburrido' || pro ? 22 : cara === 'nervioso' ? 38 : 34;
  const pupX = cara === 'mira' ? 0 : cara === 'nervioso' ? 6 : 4;
  const boca = {
    normal: 'M180 232 Q210 248 240 232', nervioso: 'M182 240 Q196 228 210 240 Q224 252 238 238',
    mira: 'M186 238 L234 238', feliz: 'M172 226 Q210 274 248 226 Z', aburrido: 'M188 238 L232 236',
    sorpresa: 'M196 230 Q210 262 224 230 Q210 222 196 230 Z',
  }[cara];
  return (
    <svg width={420} height={560} viewBox="0 0 420 560" style={{overflow: 'visible'}}>
      <g transform={`translate(${ox} ${oy})`} strokeLinecap="round" strokeLinejoin="round">
        {/* cuerpo */}
        <path d="M110 560 L120 330 Q210 290 300 330 L310 560 Z" fill={pro ? MORADO : NEGRO} stroke={NEGRO} strokeWidth={8} />
        {/* cabeza */}
        <circle cx={210} cy={190} r={128} fill={BLANCO} stroke={NEGRO} strokeWidth={9} />
        {/* ojos */}
        {[160, 260].map((x) => (
          <g key={x}>
            <ellipse cx={x} cy={180} rx={30} ry={ojoAlto} fill={BLANCO} stroke={NEGRO} strokeWidth={7} />
            <circle cx={x + pupX} cy={182 + (pro ? 6 : 0)} r={cara === 'sorpresa' ? 10 : 14} fill={NEGRO} />
            {(pro || cara === 'aburrido') && <path d={`M${x - 32} ${180 - ojoAlto + 14} L${x + 32} ${180 - ojoAlto + 14}`} stroke={NEGRO} strokeWidth={9} />}
          </g>
        ))}
        {/* gafas del PRO */}
        {pro && (
          <g fill="none" stroke={NEGRO} strokeWidth={9}>
            <rect x={118} y={150} width={84} height={62} rx={14} />
            <rect x={218} y={150} width={84} height={62} rx={14} />
            <path d="M202 172 L218 172 M118 170 L86 160 M302 170 L334 160" />
          </g>
        )}
        <path d={boca} fill={cara === 'feliz' || cara === 'sorpresa' ? NEGRO : 'none'} stroke={NEGRO} strokeWidth={8} />
        {sudor && <path d="M322 120 Q336 146 322 160 Q308 146 322 120 Z" fill="#7FC8FF" stroke={NEGRO} strokeWidth={5} />}
        {/* brazos */}
        {brazo === 'movil' && (
          <g>
            <path d="M290 360 Q350 380 330 300" fill="none" stroke={NEGRO} strokeWidth={26} />
            <rect x={300} y={232} width={58} height={92} rx={12} fill={NEGRO} />
            <rect x={308} y={242} width={42} height={66} rx={6} fill={pro ? MORADO : BLANCO} />
          </g>
        )}
        {brazo === 'medir' && (
          <g>
            <path d="M290 370 L420 330" fill="none" stroke={NEGRO} strokeWidth={30} />
            <rect x={322} y={306} width={86} height={46} rx={6} fill="none" stroke={MORADO} strokeWidth={6} strokeDasharray="12 8" transform="rotate(-17 365 329)" />
          </g>
        )}
        {brazo === 'cafe' && (
          <g>
            <path d="M290 370 Q330 330 310 290" fill="none" stroke={NEGRO} strokeWidth={26} />
            <rect x={282} y={232} width={64} height={70} rx={10} fill={BLANCO} stroke={NEGRO} strokeWidth={7} />
            <path d="M346 248 Q372 262 346 282" fill="none" stroke={NEGRO} strokeWidth={7} />
            <path d="M300 220 Q306 204 300 190 M322 220 Q328 204 322 190" fill="none" stroke={NEGRO} strokeWidth={5} opacity={0.6} />
          </g>
        )}
      </g>
    </svg>
  );
};
