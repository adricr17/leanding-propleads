"""Subtítulos palabra a palabra (estilo «una palabra cada vez», como los vídeos de Uri) y efectos de sonido.

Uso: python3 reels/_base/subtitular.py <carpeta>
La carpeta lleva:
  original.(mov|mp4)  vídeo ya montado (con su voz)
  palabras.json       [{"w": "palabra", "a": inicio, "b": fin}, ...]
  subs.json           estilo y extras:
    {"acento": ["100€"],                       palabras en cian y más grandes
     "titulo": {"arriba": "Halloween", "abajo": "WEEK", "hasta": 1.9},   rótulo de entrada (opcional)
     "efectos": [["trueno.mp3", 0.0, 0.5], ...]}   [archivo de reels/_base/sfx, segundo, volumen]
Salida: <carpeta>/SUBTITULADO_movil.mp4 (1080x1920).
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SFX = f'{R}/reels/_base/sfx'
W, H = 1080, 1920
BLANCO, CIAN = (255, 255, 255), (34, 225, 238)
F_PALABRA = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
F_CURSIVA = '/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf'
F_CONDENSADA = f'{R}/posts/_base/fuentes/Anton-Regular.ttf'
Y_TEXTO = 0.55   # altura del subtítulo (fracción de la pantalla), a la altura del pecho


def limpia(w):
    w = w.strip('.,;:!?¿¡«»"')
    return w if w[:1].isupper() and w.lower() not in ('como', 'y', 'aquí', 'ponéis', 'tenéis', 'nos') else w.lower()


def texto_con_sombra(base, xy, t, f, col, glow=True):
    """Texto blanco con sombra oscura difusa y un brillo suave del mismo color (como la referencia)."""
    capa = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    d.text((xy[0] + 3, xy[1] + 4), t, font=f, fill=(0, 0, 0, 200), anchor='mm')
    sombra = capa.filter(ImageFilter.GaussianBlur(6))
    base.alpha_composite(sombra)
    if glow:
        g = Image.new('RGBA', base.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).text(xy, t, font=f, fill=col + (110,), anchor='mm')
        base.alpha_composite(g.filter(ImageFilter.GaussianBlur(9)))
    ImageDraw.Draw(base).text(xy, t, font=f, fill=col + (255,), anchor='mm', stroke_width=2, stroke_fill=(0, 0, 0, 160))


def capa_palabra(w, acento, escala):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    grande = acento
    size = int((150 if grande else 96) * escala)
    f = ImageFont.truetype(F_PALABRA, size)
    while ImageDraw.Draw(im).textlength(w, font=f) > W - 120:
        size -= 6
        f = ImageFont.truetype(F_PALABRA, size)
    texto_con_sombra(im, (W // 2, int(H * Y_TEXTO)), w, f, CIAN if grande else BLANCO)
    return im


def capa_titulo(arriba, abajo):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    texto_con_sombra(im, (W // 2 - 40, int(H * 0.47)), arriba, ImageFont.truetype(F_CURSIVA, 150), CIAN)
    texto_con_sombra(im, (W // 2 + 30, int(H * 0.47) + 165), abajo.upper(), ImageFont.truetype(F_CONDENSADA, 190), BLANCO, glow=False)
    return im


def main(carpeta):
    src = next(f'{carpeta}/{n}' for n in ('original.mov', 'original.mp4') if os.path.exists(f'{carpeta}/{n}'))
    P = json.load(open(f'{carpeta}/palabras.json'))
    cfg = json.load(open(f'{carpeta}/subs.json'))
    acento = set(cfg.get('acento', []))
    tit = cfg.get('titulo')
    info = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate',
                           '-show_entries', 'format=duration', '-of', 'json', src], capture_output=True, text=True).stdout
    info = json.loads(info)
    num, den = map(int, info['streams'][0]['r_frame_rate'].split('/'))
    fps, dur = num / den, float(info['format']['duration'])

    # cada palabra se queda hasta que empieza la siguiente (si el hueco es corto)
    tramos = []
    for i, p in enumerate(P):
        fin = P[i + 1]['a'] if i + 1 < len(P) and P[i + 1]['a'] - p['b'] < 0.35 else p['b'] + 0.12
        tramos.append((p['a'], fin, limpia(p['w']), p['w'].strip('.,') in acento))
    cache = {}
    titulo = capa_titulo(tit['arriba'], tit['abajo']) if tit else None

    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-vf', f'scale={W}:{H}:flags=lanczos,format=rgb24',
                            '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
    tmp_v = f'{carpeta}/_video_subs.mp4'
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', f'{num}/{den}', '-i', '-', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
                            '-pix_fmt', 'yuv420p', tmp_v], stdin=subprocess.PIPE)
    n = 0
    while True:
        raw = dec.stdout.read(W * H * 3)
        if len(raw) < W * H * 3:
            break
        t = n / fps
        frame = Image.frombuffer('RGB', (W, H), raw).convert('RGBA')
        if titulo is not None and t < tit['hasta']:
            frame.alpha_composite(titulo)
        else:
            for a, b, w, ac in tramos:
                if a <= t < b:
                    k = min(int((t - a) * fps), 2)          # «pop»: 3 fotogramas creciendo
                    clave = (w, ac, k)
                    if clave not in cache:
                        cache[clave] = capa_palabra(w, ac, (0.86, 0.94, 1.0)[k])
                    frame.alpha_composite(cache[clave])
                    break
        enc.stdin.write(frame.convert('RGB').tobytes())
        n += 1
    enc.stdin.close(); enc.wait(); dec.wait()

    # audio: voz original + efectos
    args = ['ffmpeg', '-v', 'error', '-y', '-i', src]
    fil = ['[0:a]aresample=44100,aformat=channel_layouts=stereo[v0]']
    for j, (f, at, vol) in enumerate(cfg.get('efectos', [])):
        args += ['-i', f'{SFX}/{f}']
        fil.append(f'[{j + 1}:a]aresample=44100,aformat=channel_layouts=stereo,volume={vol},adelay={int(at * 1000)}|{int(at * 1000)}[e{j}]')
    ne = len(cfg.get('efectos', []))
    fil.append('[v0]' + ''.join(f'[e{j}]' for j in range(ne)) + f'amix=inputs={ne + 1}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5[a]')
    out = f'{carpeta}/SUBTITULADO_movil.mp4'
    sh = args + ['-i', tmp_v, '-filter_complex', ';'.join(fil), '-map', f'{ne + 1}:v', '-map', '[a]', '-c:v', 'libx264',
                 '-profile:v', 'high', '-level', '4.1', '-crf', '21', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                 '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{dur:.3f}', out]
    subprocess.run(sh, check=True)
    os.remove(tmp_v)
    print('OK', out)


if __name__ == '__main__':
    main(sys.argv[1])
