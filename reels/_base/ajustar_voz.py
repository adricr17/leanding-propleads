#!/usr/bin/env python3
"""Acorta los silencios entre frases de una voz en off sin acelerarla, y recalcula escenas.json.

Uso: python3 reels/_base/ajustar_voz.py <carpeta> <voz_origen.mp3> frases.json
frases.json: {"pausa": 0.25, "velocidad": 1.0, "omitir": [1],
              "frases": [[inicio, fin, escena], ...]}   (tiempos de la voz original, escena 1..N)
Escribe <carpeta>/voz.mp3 y actualiza inicio/fin de <carpeta>/escenas.json.
"""
import json, os, subprocess, sys
carpeta, origen, cfg_ruta = sys.argv[1:4]
cfg = json.load(open(cfg_ruta))
pausa, vel = cfg.get('pausa', 0.25), cfg.get('velocidad', 1.0)
frases = [f for i, f in enumerate(cfg['frases']) if i not in cfg.get('omitir', [])]
trozos, t, inicios = [], 0.0, {}
for i, (a, b, esc) in enumerate(frases):
    a0 = max(0, a - 0.04)
    b0 = b + 0.06
    if i + 1 < len(frases):
        hueco = frases[i + 1][0] - b
        b0 = b + min(hueco, pausa)          # el silencio que queda tras la frase
    else:
        b0 = b + 0.7                         # cola final
    inicios.setdefault(esc, t)
    trozos.append((a0, b0)); t += b0 - a0
total = t
filtro = ''.join(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[t{i}];" for i, (a, b) in enumerate(trozos))
filtro += ''.join(f'[t{i}]' for i in range(len(trozos))) + f'concat=n={len(trozos)}:v=0:a=1,atempo={vel}[a]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', origen, '-filter_complex', filtro, '-map', '[a]',
                '-c:a', 'libmp3lame', '-q:a', '2', os.path.join(carpeta, 'voz.mp3')], check=True)
esc_ruta = os.path.join(carpeta, 'escenas.json')
escenas = json.load(open(esc_ruta))
n = len(escenas)
for k in range(1, n + 1):
    escenas[k - 1]['inicio'] = round(inicios[k] / vel, 2) if k > 1 else 0.0
    escenas[k - 1]['fin'] = round((inicios[k + 1] if k < n else total) / vel, 2)
json.dump(escenas, open(esc_ruta, 'w'), ensure_ascii=False, indent=1)
print(carpeta, 'duración', round(total / vel, 2), [round(e['fin'] - e['inicio'], 2) for e in escenas])
