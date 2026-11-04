#!/usr/bin/env python3
"""Corta la toma única de ElevenLabs de un episodio en una voz por escena y actualiza tiempos.ts.

Uso: python3 voces.py <ep_id> <n_escenas>   (lee tomas/<ep_id>.mp3)
Corta por los n-1 silencios más largos. Escribe remotion/public/voces/minuto/<ep_id>/eNN.wav
y la duración de cada escena (voz + MARGEN) en remotion/src/minuto/tiempos.ts.
"""
import json, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
TIEMPOS = RAIZ / 'remotion/src/minuto/tiempos.ts'
MARGEN = 0.45  # s de aire tras la frase (el subtítulo usa dur-10 fotogramas)

ep, n = sys.argv[1], int(sys.argv[2])
toma = AQUI / 'tomas' / f'{ep}.mp3'
out = RAIZ / 'remotion/public/voces/minuto' / ep
out.mkdir(parents=True, exist_ok=True)

log = subprocess.run(['ffmpeg', '-i', str(toma), '-af', 'silencedetect=noise=-38dB:d=0.35', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
ini = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
fin = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', log)]
dur = float(re.search(r'Duration: (\d+):(\d+):([\d.]+)', log).groups()[2]) + \
      60 * int(re.search(r'Duration: (\d+):(\d+)', log).group(2))
sil = [(a, b) for a, b in zip(ini, fin) if a > 0.3 and b < dur - 0.2]
if len(sil) < n - 1:
    sys.exit(f'Solo {len(sil)} silencios para {n} escenas')
cortes = sorted(sorted(sil, key=lambda s: s[1] - s[0], reverse=True)[:n - 1])

trozos, t0 = [], 0.0
for a, b in cortes:
    trozos.append((t0, a + 0.08)); t0 = max(a + 0.08, b - 0.12)
trozos.append((t0, dur))

segs = []
for i, (a, b) in enumerate(trozos, 1):
    f = out / f'e{i:02d}.wav'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(toma), '-ss', f'{a:.3f}', '-to', f'{b:.3f}',
                    '-af', 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,afade=t=in:d=0.01',
                    '-ar', '44100', '-ac', '1', str(f)], check=True)
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)],
                             capture_output=True, text=True).stdout)
    segs.append(round(d + MARGEN, 2))
    print(f'e{i:02d}: {d:.2f}s')

actual = {}
m = re.search(r'TIEMPOS: Record<string, number\[\]> = (\{.*\});', TIEMPOS.read_text(), re.S)
if m:
    actual = json.loads(m.group(1))
actual[ep] = segs
TIEMPOS.write_text('// Duración (s) de cada escena según su frase de voz. GENERADO por reels/EN_1_MINUTO/voces.py; vacío = 4 s por escena.\n'
                   f'export const TIEMPOS: Record<string, number[]> = {json.dumps(actual)};\n')
print(f'Total {ep}: {sum(segs):.1f}s')
