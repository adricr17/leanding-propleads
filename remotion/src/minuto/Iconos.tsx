import React from 'react';

// Iconos planos propios (100x100): contorno negro, rellenos hueso/blanco/morado. Nada de recursos de terceros.
const N = '#111111', B = '#FFFFFF', M = '#9925AE', H = '#EFEBE4', P = '#F1C6A2', A = '#3FA9F5', V = '#2DBE6C', R = '#E63A2E';
const s = {stroke: N, strokeWidth: 5, strokeLinejoin: 'round' as const, strokeLinecap: 'round' as const};

export const ICONOS: Record<string, React.ReactNode> = {
  botella: <g {...s}><rect x={34} y={10} width={32} height={14} rx={3} fill={N} /><path d="M30 24 L70 24 L76 40 L76 88 Q76 92 72 92 L28 92 Q24 92 24 88 L24 40 Z" fill={B} /><path d="M24 56 L76 56 L76 88 Q76 92 72 92 L28 92 Q24 92 24 88 Z" fill={M} /></g>,
  libro: <g {...s}><rect x={18} y={14} width={64} height={74} rx={6} fill={B} /><path d="M30 32 L70 32 M30 46 L70 46 M30 60 L58 60" /><rect x={18} y={14} width={12} height={74} fill={M} /></g>,
  ue: <g><circle cx={50} cy={50} r={40} fill="#1F3B99" stroke={N} strokeWidth={5} />{Array.from({length: 12}).map((_, i) => { const a = (i / 12) * Math.PI * 2; return <circle key={i} cx={50 + Math.cos(a) * 26} cy={50 + Math.sin(a) * 26} r={4} fill="#FFD43B" />; })}</g>,
  azul: <g {...s}><path d="M50 12 Q78 46 78 64 Q78 88 50 88 Q22 88 22 64 Q22 46 50 12 Z" fill={A} /></g>,
  verde: <g {...s}><path d="M50 12 Q78 46 78 64 Q78 88 50 88 Q22 88 22 64 Q22 46 50 12 Z" fill={V} /></g>,
  prohibido: <g {...s} strokeWidth={9} stroke={R}><circle cx={50} cy={50} r={38} fill="none" /><path d="M24 24 L76 76" /></g>,
  ok: <g {...s}><circle cx={50} cy={50} r={38} fill={V} /><path d="M32 52 L45 64 L70 38" stroke={B} strokeWidth={9} fill="none" /></g>,
  lupa: <g {...s}><circle cx={42} cy={42} r={24} fill={B} /><path d="M60 60 L84 84" strokeWidth={12} /></g>,
  reloj: <g {...s}><circle cx={50} cy={50} r={38} fill={B} /><path d="M50 26 L50 50 L66 60" strokeWidth={7} fill="none" /></g>,
  lapiz: <g {...s}><path d="M22 78 L30 56 L66 20 L80 34 L44 70 Z" fill="#FFD43B" /><path d="M22 78 L30 56 L44 70 Z" fill={P} /><path d="M60 26 L74 40" /></g>,
  guantes: <g {...s}><path d="M30 90 L30 50 L26 28 Q26 22 32 22 Q36 22 36 30 L38 44 L38 16 Q38 10 44 10 Q50 10 50 16 L50 42 L52 14 Q52 8 58 8 Q64 8 64 14 L62 44 L66 22 Q66 16 72 16 Q78 18 76 26 L72 56 L72 90 Z" fill={N} /></g>,
  aguja: <g {...s}><rect x={40} y={10} width={20} height={56} rx={6} fill={M} /><path d="M50 66 L50 92" strokeWidth={4} /><rect x={36} y={26} width={28} height={10} fill={N} /></g>,
  basura: <g {...s}><path d="M24 30 L76 30 L70 90 L30 90 Z" fill={B} /><path d="M18 30 L82 30 M40 20 L60 20 M40 44 L42 78 M58 44 L56 78" /></g>,
  estrella: <g {...s}><path d="M50 10 L61 38 L90 40 L67 58 L75 88 L50 71 L25 88 L33 58 L10 40 L39 38 Z" fill="#FFD43B" /></g>,
  deshacer: <g {...s}><rect x={10} y={22} width={80} height={56} rx={10} fill={B} /><path d="M38 40 L26 50 L38 60 M26 50 L66 50 Q76 50 76 60" fill="none" strokeWidth={7} /><path d="M18 18 L82 82" stroke={R} strokeWidth={8} /></g>,
  regla: <g {...s}><rect x={8} y={36} width={84} height={28} rx={4} fill="#FFD43B" /><path d="M20 36 L20 50 M32 36 L32 46 M44 36 L44 50 M56 36 L56 46 M68 36 L68 50 M80 36 L80 46" /></g>,
  dm: <g {...s}><path d="M14 22 L86 22 L86 70 L40 70 L24 86 L26 70 L14 70 Z" fill={M} /><path d="M30 40 L70 40 M30 54 L58 54" stroke={B} /></g>,
  balanza: <g {...s}><path d="M50 14 L50 86 M30 86 L70 86 M18 30 L82 30" strokeWidth={6} /><path d="M18 30 L8 56 L28 56 Z M82 30 L72 56 L92 56 Z" fill={B} /></g>,
  calendario: <g {...s}><rect x={12} y={18} width={76} height={70} rx={8} fill={B} /><rect x={12} y={18} width={76} height={20} rx={8} fill={M} /><path d="M30 10 L30 26 M70 10 L70 26" strokeWidth={7} /><path d="M26 54 L38 54 M46 54 L58 54 M66 54 L76 54 M26 70 L38 70 M46 70 L58 70" /></g>,
  gota: <g {...s}><path d="M50 10 Q80 50 80 64 Q80 90 50 90 Q20 90 20 64 Q20 50 50 10 Z" fill={A} /></g>,
  jabon: <g {...s}><rect x={16} y={40} width={68} height={44} rx={14} fill="#FFB3D1" /><circle cx={34} cy={28} r={8} fill={B} /><circle cx={54} cy={20} r={6} fill={B} /><circle cx={70} cy={30} r={7} fill={B} /></g>,
  piel: <g {...s}><rect x={10} y={20} width={80} height={20} fill={P} /><rect x={10} y={40} width={80} height={24} fill={P} opacity={0.75} /><rect x={10} y={64} width={80} height={20} fill={P} opacity={0.5} /><path d="M30 52 L40 50 M56 54 L66 52" stroke={M} strokeWidth={6} /></g>,
  rascar: <g {...s}><path d="M30 86 L30 46 L24 26 Q24 20 30 20 Q34 20 36 28 L40 42 L40 14 Q40 8 46 8 Q52 8 52 14 L52 40 L56 16 Q56 10 62 10 Q68 12 66 18 L62 44 L70 30 Q74 26 78 30 Q80 34 76 40 L66 62 L66 86 Z" fill={P} /><path d="M10 10 L90 90" stroke={R} strokeWidth={8} /></g>,
  crema: <g {...s}><path d="M30 30 L70 30 L74 86 L26 86 Z" fill={B} /><rect x={38} y={14} width={24} height={16} fill={M} /><path d="M36 54 L64 54" /></g>,
  sol: <g {...s}><circle cx={50} cy={50} r={20} fill="#FFD43B" />{Array.from({length: 8}).map((_, i) => { const a = (i / 8) * Math.PI * 2; return <path key={i} d={`M${50 + Math.cos(a) * 30} ${50 + Math.sin(a) * 30} L${50 + Math.cos(a) * 42} ${50 + Math.sin(a) * 42}`} />; })}</g>,
  olas: <g {...s} fill="none"><path d="M8 40 Q20 28 32 40 Q44 52 56 40 Q68 28 80 40 Q86 46 92 40" stroke={A} strokeWidth={8} /><path d="M8 64 Q20 52 32 64 Q44 76 56 64 Q68 52 80 64 Q86 70 92 64" stroke={A} strokeWidth={8} /></g>,
  dni: <g {...s}><rect x={8} y={20} width={84} height={60} rx={8} fill={B} /><circle cx={32} cy={46} r={10} fill={P} /><path d="M20 68 Q32 56 44 68" fill={P} /><path d="M54 38 L82 38 M54 50 L82 50 M54 62 L72 62" /></g>,
  firma: <g {...s}><rect x={14} y={10} width={72} height={80} rx={6} fill={B} /><path d="M26 28 L74 28 M26 40 L74 40 M26 52 L60 52" /><path d="M26 74 Q34 60 40 72 Q46 82 52 68 Q58 60 70 72" stroke={M} strokeWidth={5} fill="none" /></g>,
  padres: <g {...s}><circle cx={32} cy={30} r={13} fill={P} /><circle cx={68} cy={30} r={13} fill={P} /><path d="M12 88 Q14 50 32 50 Q50 50 52 88 Z" fill={M} /><path d="M48 88 Q50 50 68 50 Q86 50 88 88 Z" fill={N} /></g>,
  laser: <g {...s}><rect x={14} y={10} width={30} height={40} rx={6} fill={N} /><path d="M29 50 L60 86" stroke={R} strokeWidth={8} /><circle cx={64} cy={88} r={8} fill={R} stroke="none" /></g>,
  rayo: <g {...s}><path d="M58 8 L26 54 L48 54 L40 92 L76 42 L54 42 Z" fill="#FFD43B" /></g>,
  goma: <g {...s} fill="none"><path d="M16 50 Q50 20 84 50 Q50 80 16 50 Z" stroke="#C8763A" strokeWidth={9} /></g>,
  amarillo: <g {...s}><path d="M50 12 Q78 46 78 64 Q78 88 50 88 Q22 88 22 64 Q22 46 50 12 Z" fill="#FFD43B" /></g>,
  rojo: <g {...s}><path d="M50 12 Q78 46 78 64 Q78 88 50 88 Q22 88 22 64 Q22 46 50 12 Z" fill={R} /></g>,
  negro: <g {...s}><path d="M50 12 Q78 46 78 64 Q78 88 50 88 Q22 88 22 64 Q22 46 50 12 Z" fill={N} /></g>,
  tatuaje: <g {...s}><path d="M20 90 Q22 40 30 20 L70 20 Q78 40 80 90 Z" fill={P} /><path d="M40 44 Q50 34 60 44 Q50 58 40 44 Z M50 50 L50 72" stroke={M} strokeWidth={6} fill="none" /></g>,
};

export const Icono: React.FC<{nombre: string; size?: number}> = ({nombre, size = 220}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{overflow: 'visible'}}>{ICONOS[nombre] ?? null}</svg>
);
