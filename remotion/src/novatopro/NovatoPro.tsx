import React from 'react';
import {AbsoluteFill, Audio, interpolate, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {cargaFuentes} from '../estilo/fuentes';
import {Chat} from './Chat';
import {Muneco} from './Muneco';
import {CIERRE, DURACION, EFECTOS, NOVATO, PRO, TAREA} from './guion';

cargaFuentes();
const NEGRO = '#111111', MORADO = '#9925AE', HUESO = '#EFEBE4';

const estadoEn = <T extends {desde: number}>(lista: T[], f: number) => [...lista].reverse().find((e) => f >= e.desde) ?? lista[0];

const Subtitulo: React.FC<{texto: string; pro?: boolean}> = ({texto, pro}) => (
  <div style={{position: 'absolute', left: 40, right: 40, bottom: 34, textAlign: 'center'}}>
    <span style={{fontFamily: 'Inter', fontSize: 56, lineHeight: 1.15, color: '#fff', background: pro ? MORADO : NEGRO, padding: '10px 26px', borderRadius: 18,
      boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone'}}>{texto}</span>
  </div>
);

const Panel: React.FC<{pro?: boolean}> = ({pro}) => {
  const f = useCurrentFrame();
  const d = pro ? PRO : NOVATO;
  const e = estadoEn(d.estados, f) as any;
  const bob = Math.sin(f / (pro ? 18 : 6)) * (pro ? 3 : 6);
  const temblor = e.temblor ? Math.sin(f * 2.3) * 6 : 0;
  const salto = e.salto ? Math.abs(Math.sin((f - e.desde) / 4)) * 40 * Math.max(0, 1 - (f - e.desde) / 60) : 0;
  const linea = d.lineas.find((l) => f >= l.desde && f < l.hasta);
  return (
    <AbsoluteFill style={{background: HUESO, overflow: 'hidden'}}>
      <div style={{position: 'absolute', left: 20, top: 150, transform: 'scale(1.05)', transformOrigin: 'left top'}}>
        <Muneco pro={pro} cara={e.cara} brazo={e.brazo ?? 'movil'} sudor={e.sudor} bob={bob} temblor={temblor} salto={salto} />
      </div>
      <div style={{position: 'absolute', right: 40, top: 110, transform: 'scale(1.0)'}}>
        <Chat burbujas={d.chat} visto={pro ? undefined : (d as typeof NOVATO).visto} vacio={CIERRE - 4} />
      </div>
      <div style={{position: 'absolute', left: 40, top: 36, fontFamily: 'Anton', fontSize: 54, letterSpacing: 3, color: '#fff', background: pro ? MORADO : NEGRO, padding: '2px 26px', borderRadius: 14}}>
        {pro ? 'PRO' : 'NOVATO'}
      </div>
      {linea && <Subtitulo texto={linea.texto} pro={pro} />}
    </AbsoluteFill>
  );
};

// Rótulo de la tarea: entra al principio y vuelve en los últimos fotogramas para cerrar el loop.
const Tarea: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entra = f < 30 ? spring({frame: f, fps, config: {damping: 11}}) : f >= CIERRE ? spring({frame: f - CIERRE, fps, config: {damping: 11}}) : 0;
  const sale = f < 30 ? interpolate(f, [22, 30], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}) : 1;
  if (entra <= 0.001 || (f >= 30 && f < CIERRE)) return null;
  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', pointerEvents: 'none'}}>
      <div style={{transform: `scale(${entra}) rotate(-3deg)`, opacity: sale, background: '#fff', border: `8px solid ${NEGRO}`, borderRadius: 26, padding: '18px 40px', boxShadow: `12px 12px 0 ${MORADO}`,
        fontFamily: 'Anton', fontSize: 110, lineHeight: 1, color: NEGRO, letterSpacing: 2}}>{TAREA}</div>
    </AbsoluteFill>
  );
};

export const NovatoPro: React.FC = () => (
  <AbsoluteFill style={{background: NEGRO}}>
    <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 952, overflow: 'hidden'}}><Panel /></div>
    <div style={{position: 'absolute', left: 0, right: 0, top: 968, height: 952, overflow: 'hidden'}}><Panel pro /></div>
    <Tarea />
    {[...NOVATO.lineas, ...PRO.lineas].map((l, i) => (
      <Sequence key={`v${i}`} from={l.desde} durationInFrames={l.hasta - l.desde + 10}>
        <Audio src={staticFile(`voces/np_ep01/${l.audio}.wav`)} volume={1} />
      </Sequence>
    ))}
    {EFECTOS.map(([a, desde, vol], i) => (
      <Sequence key={i} from={desde} durationInFrames={Math.max(1, Math.min(90, DURACION - desde))}>
        <Audio src={staticFile(`sfx/${a}`)} volume={vol} />
      </Sequence>
    ))}
  </AbsoluteFill>
);
