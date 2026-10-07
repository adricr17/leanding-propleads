#!/usr/bin/env python3
"""Monta un reel 1080x1920 a partir de imágenes numeradas, escenas y (opcional) voz y música.

Uso: python3 reels/_base/montar.py <carpeta_reel> [--sin-voz]
La carpeta necesita imagenes/01.png..NN.png y escenas.json:
  [{"inicio": 0.0, "fin": 3.0, "texto": "Tu cuerpo lleva años…", "clave": ["eliminar"]}, ...]
  Una escena puede llevar "video": "clips/01.mp4" (clip animado) en vez de imagen.
Opcional: voz.mp3, musica.mp3 y reel.json ({"velocidad": 1.1, "musica": 0.22}).
Los tiempos de escenas.json son los de la voz ya acelerada.
Salida: <carpeta_reel>/<NOMBRE_CARPETA>.mp4
"""
import json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FUENTE = os.path.join(BASE, '..', '..', 'posts', '_base', 'fuentes', 'DMSans-700.ttf')
W, H, FPS = 1080, 1920, 30
BLANCO, CIAN, ROJO = (255, 255, 255, 255), (64, 224, 240, 255), (235, 40, 40, 255)

def subtitulo(texto, claves, ruta, activa=None):
    """PNG transparente con el texto en 2-3 líneas centradas.
    Sin `activa`: las palabras clave en cian. Con `activa` (índice): solo esa palabra en rojo."""
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FUENTE, 62)
    palabras, lineas, actual = texto.split(), [], []
    for p in palabras:
        prueba = ' '.join(actual + [p])
        if d.textlength(prueba, font=f) > W - 180 and actual:
            lineas.append(actual); actual = [p]
        else:
            actual.append(p)
    if actual: lineas.append(actual)
    alto = 78
    y = int(H * 0.60) - (len(lineas) * alto) // 2
    claves = [c.lower() for c in claves]
    n = 0
    for linea in lineas:
        ancho = d.textlength(' '.join(linea), font=f)
        x = (W - ancho) / 2
        for i, p in enumerate(linea):
            limpia = p.strip('.,:;¿?¡!…').lower()
            if activa is None:
                color = CIAN if limpia in claves else BLANCO
            else:
                color = ROJO if n == activa else BLANCO
            n += 1
            d.text((x, y), p, font=f, fill=color, stroke_width=5, stroke_fill=(0, 0, 0, 170))
            x += d.textlength(p + ' ', font=f)
        y += alto
    img.save(ruta)

def main(carpeta, sin_voz=False):
    carpeta = os.path.abspath(carpeta)
    escenas = json.load(open(os.path.join(carpeta, "escenas.json")))
    cfg_ruta = os.path.join(carpeta, 'reel.json')
    cfg = json.load(open(cfg_ruta)) if os.path.exists(cfg_ruta) else {}
    voz = os.path.join(carpeta, 'voz.mp3')
    musica = os.path.join(carpeta, 'musica.mp3')
    tmp = tempfile.mkdtemp()
    pal_ruta = os.path.join(carpeta, 'palabras.json')
    palabras = json.load(open(pal_ruta)) if os.path.exists(pal_ruta) else None
    clips = []
    for i, e in enumerate(escenas, 1):
        img = os.path.join(carpeta, 'imagenes', e.get('imagen', f'{i:02d}.png'))
        dur = e['fin'] - e['inicio']
        frames = max(1, round(dur * FPS))
        sub = os.path.join(tmp, f'sub{i:02d}.png')
        # Karaoke: con palabras.json, el texto de la escena sale de las palabras de la voz
        # y cada palabra se pone en rojo mientras suena
        pals = [p for p in (palabras or []) if p['escena'] == i]
        resaltes = []
        if pals:
            texto = ' '.join(p['texto'] for p in pals)
            subtitulo(texto, [], sub)
            for k, p in enumerate(pals):
                a = max(0.0, p['inicio'] - e['inicio'])
                b = (pals[k + 1]['inicio'] - e['inicio']) if k + 1 < len(pals) else min(dur, p['fin'] - e['inicio'] + 0.25)
                r = os.path.join(tmp, f'sub{i:02d}_{k:02d}.png')
                subtitulo(texto, [], r, activa=k)
                resaltes.append((r, a, b))
        else:
            subtitulo(e.get('texto', ''), e.get('clave', []), sub)
        out = os.path.join(tmp, f'clip{i:02d}.mp4')
        if e.get('video'):
            # Clip animado: se encaja a 1080x1920 y se corta a la duración de la escena
            entrada = ['-i', os.path.join(carpeta, e['video'])]
            base = f"[0:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1[b];"
        else:
            # Zoom lento 100 -> 108 % centrado sobre la imagen escalada a 2x para que no tiemble
            entrada = ['-loop', '1', '-i', img]
            zoom = f"zoompan=z='1+0.08*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}"
            base = f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase:flags=lanczos,crop={W*2}:{H*2},{zoom}[b];"
        filtro = base + "[b][1:v]overlay=0:0[c0];"
        extra = []
        for k, (r, a, b) in enumerate(resaltes):
            extra += ['-loop', '1', '-i', r]
            filtro += f"[c{k}][{k+2}:v]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'[c{k+1}];"
        filtro += f"[c{len(resaltes)}]fade=t=in:st=0:d=0.15,format=yuv420p[v]"
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + entrada + ['-loop', '1', '-i', sub] + extra + [
                        '-filter_complex', filtro, '-map', '[v]', '-frames:v', str(frames), '-r', str(FPS),
                        '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', out], check=True)
        clips.append(out)
    lista = os.path.join(tmp, 'clips.txt')
    open(lista, 'w').write(''.join(f"file '{c}'\n" for c in clips))
    nombre = os.path.basename(os.path.normpath(carpeta)) + ('_SIN_VOZ' if sin_voz else '')
    salida = os.path.join(carpeta, f'{nombre}.mp4')
    total = escenas[-1]['fin']
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista]
    partes, etiquetas = [], []
    n = 1
    if os.path.exists(voz) and not sin_voz:
        cmd += ['-i', voz]
        partes.append(f"[{n}:a]atempo={cfg.get('velocidad', 1.0)},apad[a{n}]")
        etiquetas.append(f'[a{n}]'); n += 1
    if os.path.exists(musica):
        # La música se repite si hace falta y se funde al final
        cmd += ['-stream_loop', '-1', '-i', musica]
        vol = cfg.get('musica', 0.22) if etiquetas else 0.6
        partes.append(f"[{n}:a]volume={vol},afade=t=in:d=0.5,afade=t=out:st={max(0, total-1.5)}:d=1.5[a{n}]")
        etiquetas.append(f'[a{n}]'); n += 1
    if etiquetas:
        mezcla = ''.join(etiquetas)
        partes.append(f"{mezcla}amix=inputs={len(etiquetas)}:duration=longest:normalize=0,atrim=0:{total},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
        cmd += ['-filter_complex', ';'.join(partes), '-map', '0:v', '-map', '[a]', '-c:a', 'aac', '-profile:a', 'aac_low', '-b:a', '192k', '-ac', '2', '-ar', '44100']
    cmd += ['-c:v', 'copy', '-movflags', '+faststart', salida]
    subprocess.run(cmd, check=True)
    print(salida)

if __name__ == '__main__':
    main(sys.argv[1], '--sin-voz' in sys.argv)
