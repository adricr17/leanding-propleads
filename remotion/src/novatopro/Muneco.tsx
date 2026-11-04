import React from 'react';

// Personajes 2D planos «un pelín realistas» (rediseño del 04/11/2026): proporciones de persona, piel, pelo, cejas y manos.
// NOVATO: pelo despeinado con remolino, sudadera blanca XXL con las mangas tapando medio puño, cordones desiguales,
//         cuello flaco, hombros caídos y dientes de conejo.
// PRO: pelo corto con degradado, barba de tres días, gafas, camiseta morada ajustada y antebrazo tatuado. Caja de 420x560.
export type Cara = 'normal' | 'nervioso' | 'mira' | 'feliz' | 'aburrido' | 'sorpresa';
const NEGRO = '#111111', BLANCO = '#FFFFFF', MORADO = '#9925AE', PIEL = '#F1C6A2', PIEL_SOMBRA = '#E0AA84', PELO_N = '#3B2A20', BARBA = 'rgba(17,17,17,.16)';
const T = 6; // grosor del contorno

export const Muneco: React.FC<{
  pro?: boolean; cara?: Cara; bob?: number; temblor?: number; salto?: number; brazo?: 'movil' | 'medir' | 'cafe' | 'abajo'; sudor?: boolean;
}> = ({pro = false, cara = 'normal', bob = 0, temblor = 0, salto = 0, brazo = 'movil', sudor = false}) => {
  const ox = temblor, oy = bob - salto;
  const ropa = pro ? MORADO : BLANCO;
  // postura: el NOVATO va encorvado (cabeza adelantada y más baja)
  const cabeza = pro ? 'translate(0 0)' : 'translate(-6 14) rotate(-4 210 200)';
  // ojos
  const ojoAlto = {normal: 15, nervioso: 19, mira: 16, feliz: 7, aburrido: 8, sorpresa: 23}[cara];
  const pupX = cara === 'mira' ? 0 : cara === 'nervioso' ? 5 : 3;
  // cejas: [izquierda, derecha]
  const cejas = {
    normal: ['M146 148 Q166 140 186 146', 'M234 146 Q254 140 274 148'],
    nervioso: ['M146 140 Q168 130 188 146', 'M232 146 Q252 130 274 140'],
    mira: ['M146 146 L186 146', 'M234 146 L274 146'],
    feliz: ['M146 142 Q166 130 186 140', 'M234 140 Q254 130 274 142'],
    aburrido: ['M148 156 L186 154', 'M234 154 L272 156'],
    sorpresa: ['M146 132 Q166 120 186 130', 'M234 130 Q254 120 274 132'],
  }[cara];
  const dientes = !pro && (cara === 'nervioso' || cara === 'feliz' || cara === 'sorpresa');
  const boca = {
    normal: 'M188 254 Q210 266 232 254', nervioso: 'M186 256 Q210 246 234 258 Q210 272 186 256 Z',
    mira: 'M192 258 L228 258', feliz: 'M178 248 Q210 292 242 248 Z', aburrido: 'M192 258 L230 256',
    sorpresa: 'M198 250 Q210 278 222 250 Q210 242 198 250 Z',
  }[cara];
  const bocaRellena = cara === 'feliz' || cara === 'sorpresa' || cara === 'nervioso';

  return (
    <svg width={420} height={560} viewBox="0 0 420 560" style={{overflow: 'visible'}}>
      <g transform={`translate(${ox} ${oy})`} strokeLinecap="round" strokeLinejoin="round">
        {/* cuello */}
        <path d={pro ? 'M182 290 L182 348 L238 348 L238 290 Z' : 'M192 300 L190 360 L226 360 L224 300 Z'} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
        {/* torso */}
        {pro ? (
          <g>
            <path d="M92 560 L104 372 Q150 342 186 340 Q210 356 234 340 Q270 342 316 372 L328 560 Z" fill={MORADO} stroke={NEGRO} strokeWidth={T} />
            <path d="M186 340 Q210 368 234 340" fill="none" stroke={NEGRO} strokeWidth={T} />
          </g>
        ) : (
          <g>
            {/* sudadera XXL, hombros caídos */}
            <path d="M54 560 Q58 420 120 378 Q160 356 190 352 L228 352 Q262 356 300 378 Q362 420 366 560 Z" fill={BLANCO} stroke={NEGRO} strokeWidth={T} />
            <path d="M150 372 Q208 420 270 372" fill="none" stroke={NEGRO} strokeWidth={T} />
            {/* cordones desiguales */}
            <path d="M190 392 L184 446 M228 392 L236 484" stroke={NEGRO} strokeWidth={5} fill="none" />
            <circle cx={184} cy={450} r={6} fill={NEGRO} /><circle cx={236} cy={488} r={6} fill={NEGRO} />
            {/* bolsillo canguro */}
            <path d="M128 560 L148 496 L272 496 L292 560" fill="none" stroke={NEGRO} strokeWidth={T} />
          </g>
        )}

        {/* cabeza */}
        <g transform={cabeza}>
          {/* orejas */}
          <ellipse cx={112} cy={204} rx={17} ry={27} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
          <ellipse cx={308} cy={204} rx={17} ry={27} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
          {/* cara */}
          <path d="M114 186 Q114 72 210 70 Q306 72 306 186 Q306 300 210 304 Q114 300 114 186 Z" fill={PIEL} stroke={NEGRO} strokeWidth={T} />
          {pro && <path d="M128 230 Q140 300 210 304 Q280 300 292 230 Q286 280 210 288 Q134 280 128 230 Z" fill={BARBA} />}
          {/* pelo */}
          {pro ? (
            <path d="M114 168 Q110 76 210 66 Q312 76 306 168 Q296 118 262 108 Q210 96 158 108 Q124 118 114 168 Z" fill={NEGRO} stroke={NEGRO} strokeWidth={T} />
          ) : (
            <g>
              <path d="M112 176 Q96 112 132 84 L128 62 L156 78 L166 46 L190 72 L212 40 L230 70 L258 48 L262 80 L292 70 L290 98 Q322 124 308 178 Q296 132 264 118 Q236 132 206 116 Q178 132 150 118 Q124 132 112 176 Z" fill={PELO_N} stroke={NEGRO} strokeWidth={T} />
              {/* remolino */}
              <path d="M214 42 Q232 14 250 30 Q236 26 230 44" fill={PELO_N} stroke={NEGRO} strokeWidth={5} />
            </g>
          )}
          {/* cejas */}
          {cejas.map((d, i) => <path key={i} d={d} fill="none" stroke={pro ? NEGRO : PELO_N} strokeWidth={pro ? 9 : 8} />)}
          {/* ojos */}
          {[166, 254].map((x) => (
            <g key={x}>
              <ellipse cx={x} cy={180} rx={19} ry={ojoAlto} fill={BLANCO} stroke={NEGRO} strokeWidth={5} />
              {ojoAlto > 9 && <circle cx={x + pupX} cy={182} r={cara === 'sorpresa' ? 6 : 8} fill={NEGRO} />}
              {(pro || cara === 'aburrido') && <path d={`M${x - 20} ${180 - ojoAlto + 5} L${x + 20} ${180 - ojoAlto + 5}`} stroke={NEGRO} strokeWidth={6} />}
            </g>
          ))}
          {/* gafas del PRO */}
          {pro && (
            <g fill="none" stroke={NEGRO} strokeWidth={7}>
              <rect x={136} y={154} width={62} height={52} rx={12} />
              <rect x={222} y={154} width={62} height={52} rx={12} />
              <path d="M198 172 Q210 164 222 172 M136 172 L116 168 M284 172 L304 168" />
            </g>
          )}
          {/* nariz */}
          <path d="M212 192 Q198 224 206 230 Q212 234 220 230" fill="none" stroke={PIEL_SOMBRA} strokeWidth={6} />
          {/* boca */}
          <path d={boca} fill={bocaRellena ? '#5A1E1E' : 'none'} stroke={NEGRO} strokeWidth={6} />
          {dientes && <rect x={201} y={cara === 'feliz' ? 250 : 252} width={18} height={12} rx={2} fill={BLANCO} stroke={NEGRO} strokeWidth={3} />}
          {!pro && (
            /* pecas */
            <g fill={PIEL_SOMBRA}>{[[150, 212], [162, 220], [146, 224], [262, 212], [274, 220], [258, 224]].map(([x, y], i) => <circle key={i} cx={x} cy={y} r={3.5} />)}</g>
          )}
          {sudor && <path d="M320 118 Q336 148 320 162 Q304 148 320 118 Z" fill="#7FC8FF" stroke={NEGRO} strokeWidth={4} />}
        </g>

        {/* brazos */}
        {brazo === 'movil' && (pro ? (
          <g>
            <path d="M304 384 Q356 430 344 352" fill="none" stroke={NEGRO} strokeWidth={58} />
            <path d="M304 384 Q356 430 344 352" fill="none" stroke={MORADO} strokeWidth={46} />
            <path d="M344 360 L336 286" stroke={NEGRO} strokeWidth={36} /><path d="M344 360 L336 286" stroke={PIEL} strokeWidth={24} />
            {/* tatuaje del antebrazo */}
            <path d="M334 340 Q346 330 340 318 M332 306 L344 302" stroke={NEGRO} strokeWidth={3} fill="none" />
            <rect x={302} y={206} width={62} height={98} rx={12} fill={NEGRO} />
            <rect x={309} y={216} width={48} height={74} rx={6} fill={MORADO} />
            <circle cx={334} cy={292} r={18} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
          </g>
        ) : (
          <g>
            {/* manga larga que tapa medio puño */}
            <path d="M296 392 Q364 450 344 324" fill="none" stroke={NEGRO} strokeWidth={56} />
            <path d="M296 392 Q364 450 344 324" fill="none" stroke={BLANCO} strokeWidth={44} />
            <rect x={306} y={210} width={58} height={92} rx={12} fill={NEGRO} />
            <rect x={313} y={219} width={44} height={70} rx={6} fill={BLANCO} />
            <path d="M318 300 Q338 312 358 300" stroke={NEGRO} strokeWidth={4} fill={PIEL} />
          </g>
        ))}
        {brazo === 'medir' && (
          <g>
            <path d="M300 384 L364 376" stroke={NEGRO} strokeWidth={50} /><path d="M300 384 L364 376" stroke={MORADO} strokeWidth={38} />
            <path d="M364 376 L452 352" stroke={NEGRO} strokeWidth={36} /><path d="M364 376 L452 352" stroke={PIEL} strokeWidth={24} />
            <circle cx={462} cy={350} r={18} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
            <rect x={378} y={344} width={64} height={34} rx={6} fill="none" stroke={MORADO} strokeWidth={6} strokeDasharray="10 7" transform="rotate(-15 410 361)" />
          </g>
        )}
        {brazo === 'cafe' && (
          <g>
            <path d="M304 384 Q356 430 340 348" stroke={NEGRO} strokeWidth={58} fill="none" />
            <path d="M304 384 Q356 430 340 348" stroke={MORADO} strokeWidth={46} fill="none" />
            <path d="M340 356 L326 300" stroke={NEGRO} strokeWidth={36} /><path d="M340 356 L326 300" stroke={PIEL} strokeWidth={24} />
            <path d="M330 340 Q342 330 336 318" stroke={NEGRO} strokeWidth={3} fill="none" />
            <rect x={286} y={232} width={64} height={70} rx={10} fill={BLANCO} stroke={NEGRO} strokeWidth={T} />
            <path d="M350 248 Q376 262 350 282" fill="none" stroke={NEGRO} strokeWidth={T} />
            <circle cx={322} cy={300} r={18} fill={PIEL} stroke={NEGRO} strokeWidth={T} />
            <path d="M304 220 Q310 204 304 190 M326 220 Q332 204 326 190" fill="none" stroke={NEGRO} strokeWidth={4} opacity={0.5} />
          </g>
        )}
      </g>
    </svg>
  );
};
