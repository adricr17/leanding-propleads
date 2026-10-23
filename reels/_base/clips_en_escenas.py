"""Sustituye en escenas.json las imágenes que ya tienen clip animado (clips/NN.mp4).

Cada aparición de NN.png pasa a ser un tramo seguido del clip ("desde" acumulado),
y a partir de la segunda se recorta un poco para que el corte se note.
Uso: python3 reels/_base/clips_en_escenas.py <carpeta_reel> [NN=clips/otro.mp4 ...]
"""
import json, os, sys

RECORTES = [None, 'crop=iw*0.72:ih*0.72,scale=1080:1920', 'crop=iw*0.6:ih*0.6:iw*0.2:ih*0.15,scale=1080:1920']

carpeta = sys.argv[1]
extra = dict(a.split('=', 1) for a in sys.argv[2:])
ruta = os.path.join(carpeta, 'escenas.json')
escenas = json.load(open(ruta))
usado = {}
for e in escenas:
    img = e.get('imagen', '')
    nn = img[:-4] if img.endswith('.png') else ''
    clip = extra.get(nn, f'clips/{nn}.mp4')
    if not nn or not os.path.exists(os.path.join(carpeta, clip)):
        continue
    k, desde = usado.get(nn, (0, 0.0))
    for c in ('imagen', 'foco', 'recorte'):
        e.pop(c, None)
    e['video'] = clip
    if desde:
        e['desde'] = round(desde, 3)
    if RECORTES[min(k, 2)]:
        e['filtro'] = RECORTES[min(k, 2)]
    usado[nn] = (k + 1, desde + e['fin'] - e['inicio'])
json.dump(escenas, open(ruta, 'w'), ensure_ascii=False, indent=1)
for nn, (k, d) in usado.items():
    print(f'{nn}: {k} tramos, {d:.2f} s de clip')
