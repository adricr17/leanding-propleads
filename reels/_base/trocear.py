#!/usr/bin/env python3
"""Parte las escenas de un reel en cortes de como mucho N segundos para un montaje más dinámico.

Uso: python3 reels/_base/trocear.py <carpeta_reel> [--max 2.0] [--sin-subtitulos]
Lee <carpeta>/escenas_original.json (si no existe, copia ahí escenas.json) y reescribe escenas.json.
Cada escena se divide en partes iguales. Los planos salen, por orden, de:
  1. la imagen o clip de la escena;
  2. la imagen alternativa imagenes/NNb.png, si existe;
  3. recortes más cerrados de la imagen (o del clip, con "punch-in").
"""
import json, math, os, shutil, sys
from PIL import Image

carpeta = sys.argv[1]
maximo = float(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 2.0
orig = os.path.join(carpeta, 'escenas_original.json')
if not os.path.exists(orig):
    shutil.copy(os.path.join(carpeta, 'escenas.json'), orig)
escenas = json.load(open(orig))

# Encuadres cerrados: (fracción del ancho, centro x, centro y) y punto de zoom
CERRADOS = [(0.62, 0.5, 0.5, [0.5, 0.45, 1.10]), (0.55, 0.5, 0.38, [0.5, 0.55, 1.10])]
PUNCH = ["crop=iw*0.72:ih*0.72,scale=1080:1920", "crop=iw*0.6:ih*0.6:iw*0.2:ih*0.15,scale=1080:1920"]
FOCOS = [[0.5, 0.5, 1.10], [0.45, 0.42, 1.12], [0.55, 0.58, 1.12]]

def recorte(img, k):
    w, h = Image.open(img).size
    f, cx, cy, foco = CERRADOS[k % len(CERRADOS)]
    cw, ch = w * f, h * f
    x0 = min(max(0, w * cx - cw / 2), w - cw); y0 = min(max(0, h * cy - ch / 2), h - ch)
    return [round(x0), round(y0), round(x0 + cw), round(y0 + ch)], foco

nuevas = []
for i, e in enumerate(escenas, 1):
    dur = e['fin'] - e['inicio']
    n = max(1, math.ceil(dur / maximo - 0.02))
    base = {k: v for k, v in e.items() if k not in ('inicio', 'fin')}
    if not e.get('video') and 'imagen' not in base:
        base['imagen'] = f'{i:02d}.png'
    planos = [dict(base)]
    alt = f'{i:02d}b.png'
    if not e.get('video') and os.path.exists(os.path.join(carpeta, 'imagenes', alt)) and alt != base.get('imagen'):
        planos.append(dict(base, imagen=alt))
    k = 0
    while len(planos) < n:
        if e.get('video'):
            planos.append(dict(base, filtro=PUNCH[k % len(PUNCH)]))
        else:
            img = os.path.join(carpeta, 'imagenes', base['imagen'])
            r, foco = recorte(img, k)
            planos.append(dict(base, recorte=r, foco=foco))
        k += 1
    paso = dur / n
    for j in range(n):
        p = dict(planos[j])
        p['inicio'] = round(e['inicio'] + j * paso, 3)
        p['fin'] = round(e['inicio'] + (j + 1) * paso, 3) if j < n - 1 else e['fin']
        p['escena_voz'] = i
        if e.get('video') and j:
            p['desde'] = round(j * paso, 3)
        if not e.get('video') and 'foco' not in p:
            p['foco'] = FOCOS[j % len(FOCOS)]
        if '--sin-subtitulos' in sys.argv:
            p['sin_subtitulo'] = True
        nuevas.append(p)
json.dump(nuevas, open(os.path.join(carpeta, 'escenas.json'), 'w'), ensure_ascii=False, indent=1)
print(carpeta, len(escenas), 'escenas ->', len(nuevas), 'cortes; el más largo', round(max(p['fin'] - p['inicio'] for p in nuevas), 2), 's')
