import React from 'react';
import {AbsoluteFill, Audio, interpolate, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {cargaFuentes} from '../estilo/fuentes';
import {Episodio, Escena, Item} from './episodios';
import {Icono} from './Iconos';
import {TIEMPOS} from './tiempos';

cargaFuentes();
const N = '#111111', M = '#9925AE', H = '#EFEBE4', R = '#E63A2E', V = '#2DBE6C';
export const FPS = 30;
const POR_DEFECTO = 4; // s por escena si aún no hay voz

// duración de cada escena en fotogramas (de la voz si existe; si no, 4 s)
export const duraciones = (ep: Episodio) => {
  const t = TIEMPOS[ep.id];
  return ep.escenas.map((_, i) => Math.round((t?.[i] ?? POR_DEFECTO) * FPS));
};
export const duracionTotal = (ep: Episodio) => duraciones(ep).reduce((a, b) => a + b, 0);

const marcado = (t: string) => t.split(/(<a>.*?<\/a>)/).map((p, i) =>
  p.startsWith('<a>') ? <span key={i} style={{color: '#fff', background: M, padding: '0 12px', borderRadius: 10, boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone'}}>{p.slice(3, -4)}</span> : <span key={i}>{p}</span>);

const Pop: React.FC<{t: number; dur: number; x: number; y: number; children: React.ReactNode}> = ({t, dur, x, y, children}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const desde = Math.round(t * dur);
  if (f < desde) return null;
  const s = spring({frame: f - desde, fps, config: {damping: 11, stiffness: 180}});
  const flota = Math.sin((f - desde) / 22) * 4;
  return <div style={{position: 'absolute', left: x, top: y + flota, transform: `translate(-50%,-50%) scale(${s})`}}>{children}</div>;
};

const Pieza: React.FC<{it: Item; dur: number}> = ({it, dur}) => {
  const t = it.t ?? 0;
  if (it.k === 'icono') return <Pop t={t} dur={dur} x={it.x} y={it.y}><Icono nombre={it.i} size={it.s ?? 240} /></Pop>;
  if (it.k === 'tarjeta') {
    const bg = it.color === 'morado' ? M : it.color === 'negro' ? N : '#fff';
    const fg = it.color === 'morado' || it.color === 'negro' ? '#fff' : N;
    return (
      <Pop t={t} dur={dur} x={it.x} y={it.y}>
        <div style={{width: it.w ?? 420, background: bg, color: fg, border: `6px solid ${N}`, borderRadius: 26, boxShadow: `10px 10px 0 ${N}`, padding: '22px 26px', textAlign: 'center'}}>
          <div style={{fontFamily: 'Anton', fontSize: 64, lineHeight: 1.05, letterSpacing: 1}}>{it.texto}</div>
          {it.sub && <div style={{fontFamily: 'SpaceMono', fontSize: 28, marginTop: 6, opacity: 0.85}}>{it.sub}</div>}
        </div>
      </Pop>
    );
  }
  if (it.k === 'numero') {
    return (
      <Pop t={t} dur={dur} x={it.x} y={it.y}>
        <div style={{background: '#fff', border: `6px solid ${N}`, borderRadius: 30, boxShadow: `12px 12px 0 ${M}`, padding: '20px 44px', textAlign: 'center'}}>
          <div style={{fontFamily: 'Anton', fontSize: 190, lineHeight: 1, color: M}}>{it.n}</div>
          <div style={{fontFamily: 'SpaceMono', fontSize: 40, letterSpacing: 4, color: N}}>{it.sub.toUpperCase()}</div>
        </div>
      </Pop>
    );
  }
  const c = it.color === 'verde' ? V : it.color === 'morado' ? M : R;
  return (
    <Pop t={t} dur={dur} x={it.x} y={it.y}>
      <div style={{transform: 'rotate(-6deg)', border: `8px solid ${c}`, color: c, background: 'rgba(255,255,255,.85)', borderRadius: 16, padding: '6px 28px', fontFamily: 'Anton', fontSize: 78, letterSpacing: 3}}>{it.texto}</div>
    </Pop>
  );
};

// subtítulo de la frase, con la palabra que suena resaltada (reparto por sílabas: la voz TTS va a ritmo uniforme)
const silabas = (w: string) => Math.max(1, (w.toLowerCase().match(/[aeiouáéíóúü]+/g) ?? []).length);
const Subtitulo: React.FC<{voz: string; dur: number}> = ({voz, dur}) => {
  const f = useCurrentFrame();
  const palabras = voz.split(' ');
  const pesos = palabras.map(silabas);
  const total = pesos.reduce((a, b) => a + b, 0);
  const util = dur - 10; // la voz acaba antes del final de la escena
  let acc = 0, activa = palabras.length - 1;
  for (let i = 0; i < palabras.length; i++) { acc += pesos[i]; if (f < (acc / total) * util) { activa = i; break; } }
  return (
    <div style={{position: 'absolute', left: 70, right: 70, top: 1400, textAlign: 'center', fontFamily: 'Inter', fontSize: 52, lineHeight: 1.35, color: N}}>
      {palabras.map((w, i) => (
        <span key={i} style={{padding: '0 6px', borderRadius: 8, color: i === activa ? '#fff' : i < activa ? N : 'rgba(17,17,17,.45)', background: i === activa ? R : 'transparent'}}>{w} </span>
      ))}
    </div>
  );
};

const Barra: React.FC<{total: number}> = ({total}) => {
  const f = useCurrentFrame();
  const p = Math.min(1, f / total);
  return (
    <div style={{position: 'absolute', left: 120, right: 120, top: 1690, height: 10, background: 'rgba(17,17,17,.15)', borderRadius: 5}}>
      <div style={{width: `${p * 100}%`, height: '100%', background: R, borderRadius: 5}} />
      <div style={{position: 'absolute', left: `${p * 100}%`, top: -17, width: 44, height: 44, marginLeft: -22, borderRadius: 22, background: '#fff', border: `5px solid ${N}`, fontFamily: 'SpaceMono', fontSize: 16, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        {Math.max(0, Math.ceil((total - f) / FPS))}
      </div>
    </div>
  );
};

const EscenaVista: React.FC<{e: Escena; dur: number}> = ({e, dur}) => {
  const f = useCurrentFrame();
  const entra = interpolate(f, [0, 6], [0.92, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: 60, right: 60, top: 250, textAlign: 'center', transform: `scale(${entra})`, fontFamily: 'Anton', fontSize: 92, lineHeight: 1.12, color: N, textTransform: 'uppercase'}}>{marcado(e.titulo)}</div>
      {e.items.map((it, i) => <Pieza key={i} it={it} dur={dur} />)}
      <Subtitulo voz={e.voz} dur={dur} />
    </AbsoluteFill>
  );
};

export const Minuto: React.FC<{ep: Episodio}> = ({ep}) => {
  const ds = duraciones(ep);
  const total = ds.reduce((a, b) => a + b, 0);
  const conVoz = Boolean(TIEMPOS[ep.id]);
  let t = 0;
  return (
    <AbsoluteFill style={{background: `radial-gradient(circle at 50% 40%, #FFF8EC 0%, ${H} 70%)`}}>
      <div style={{position: 'absolute', left: 0, right: 0, top: 120, textAlign: 'center', fontFamily: 'SpaceMono', fontSize: 30, letterSpacing: 6, color: N}}>
        PHARAON · <span style={{color: M}}>EN 1 MINUTO</span>
      </div>
      {ep.escenas.map((e, i) => {
        const desde = t;
        t += ds[i];
        return (
          <Sequence key={i} from={desde} durationInFrames={ds[i]}>
            <EscenaVista e={e} dur={ds[i]} />
            {conVoz && <Audio src={staticFile(`voces/minuto/${ep.id}/e${String(i + 1).padStart(2, '0')}.wav`)} />}
            <Audio src={staticFile('sfx/whoosh.mp3')} volume={0.18} />
          </Sequence>
        );
      })}
      <Barra total={total} />
    </AbsoluteFill>
  );
};
