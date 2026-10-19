"""Monta PHARAON SITCOM EP03 (especial Halloween) «Todos disfrazados».

Salida: reels/PHARAON_SITCOM/ep03/EP03_halloween_movil.mp4 (voces de IA)
        reels/PHARAON_SITCOM/ep03/EP03_halloween_sin_voces_movil.mp4 (solo efectos)
Uso: python3 reels/PHARAON_SITCOM/ep03/montar_ep03.py
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

R = '/home/user/leanding-propleads'
EP = f'{R}/reels/PHARAON_SITCOM/ep03'
SFX = f'{R}/reels/_base/sfx'
FUENTES = f'{R}/posts/_base/fuentes/'
TMP = f'{EP}/tmp'
os.makedirs(TMP, exist_ok=True)
W, H, FPS = 1080, 1920, 30
NARANJA = (255, 140, 30)


def sh(*a):
    subprocess.run(a, check=True)


def font(n, s):
    return ImageFont.truetype(FUENTES + n, s)


def cartela(nombre, lineas, y, size=92):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = font('Anton-Regular.ttf', size)
    alto = int(size * 1.2)
    ancho = max(d.textlength(l, font=f) for l in lineas)
    d.rounded_rectangle([(W - ancho) / 2 - 40, y - 24, (W + ancho) / 2 + 40, y + alto * len(lineas) + 20],
                        radius=26, fill=(10, 10, 12, 215))
    for i, l in enumerate(lineas):
        d.text(((W - d.textlength(l, font=f)) / 2, y + i * alto), l, font=f, fill=(245, 238, 230))
    p = f'{TMP}/{nombre}.png'
    im.save(p)
    return p


def fija(nombre, img, dur, zoom=1.08):
    out = f'{TMP}/{nombre}.mp4'
    n = int(dur * FPS)
    sh('ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', img, '-vf',
       f'scale={W * 2}:{H * 2},zoompan=z=\'1+{zoom - 1}*on/{n}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={n}:s={W}x{H}:fps={FPS},setsar=1',
       '-t', str(dur), '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out)
    return out


def clip(nombre, src, ss, dur):
    out = f'{TMP}/{nombre}.mp4'
    sh('ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', src, '-t', str(dur), '-vf',
       f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}',
       '-an', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out)
    return out


def pantalla_dm():
    im = Image.new('RGB', (W, H), (14, 14, 16))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 230], fill=(22, 22, 26))
    d.text((70, 120), '‹', font=font('DMSans-500.ttf', 70), fill=(240, 240, 240), anchor='lm')
    d.ellipse([130, 80, 210, 160], fill=(80, 80, 90))
    d.text((235, 105), 'nuevo_cliente', font=font('DMSans-700.ttf', 40), fill=(240, 240, 240))
    d.text((235, 152), 'Mensaje nuevo', font=font('DMSans-400.ttf', 28), fill=(150, 150, 160))
    fo = font('DMSans-500.ttf', 50)
    lineas = ['¿Puedo ir disfrazado', 'aunque no me vaya', 'a tatuar?']
    y0 = 760
    bw = max(d.textlength(t, font=fo) for t in lineas) + 80
    d.rounded_rectangle([60, y0, 60 + bw, y0 + 70 * len(lineas) + 60], radius=46, fill=(45, 45, 52))
    for i, t in enumerate(lineas):
        d.text((100, y0 + 30 + i * 70), t, font=fo, fill=(245, 245, 245))
    p = f'{TMP}/dm.png'
    im.save(p)
    return p


def cierre():
    fondo = Image.open(f'{EP}/G_grupo_disfraces.png').convert('RGB').resize((W, H))
    fondo = ImageEnhance.Brightness(fondo.filter(ImageFilter.GaussianBlur(14))).enhance(0.35)
    d = ImageDraw.Draw(fondo)
    def centro(y, t, f, col):
        d.text(((W - d.textlength(t, font=f)) / 2, y), t, font=f, fill=col)
    centro(560, 'DEL 27 AL 31 DE OCTUBRE', font('Anton-Regular.ttf', 92), NARANJA)
    centro(720, 'Ven disfrazado', font('Anton-Regular.ttf', 120), (245, 238, 230))
    centro(860, 'aunque no te tatúes', font('Anton-Regular.ttf', 120), (245, 238, 230))
    centro(1060, 'El mejor disfraz se lleva premio', font('DMSans-700.ttf', 52), (245, 238, 230))
    centro(1220, '@pharaonstudio', font('Anton-Regular.ttf', 76), NARANJA)
    p = f'{TMP}/cierre.png'
    fondo.save(p)
    return p


P = [
    (fija('p1', pantalla_dm(), 1.7, zoom=1.06), 1.7),                     # DM en pantalla
    (clip('p2', f'{EP}/A_adri_lipsync.mp4', 0, 1.95), 1.95),              # Adri: «Claro… ¿y nosotros?»
    (clip('p3', f'{EP}/U_uri_lipsync.mp4', 0, 1.7), 1.7),                 # Uri: «¡TODOS DISFRAZADOS!»
    (clip('p4', f'{EP}/G_grupo_clip.mp4', 0.3, 2.2), 2.2),                # todos disfrazados a disgusto
    (clip('p5', f'{EP}/P_calabaza_clip.mp4', 0.2, 2.6), 2.6),             # Uri calabaza feliz
    (clip('p6', f'{EP}/C_carlos_clip.mp4', 0.0, 3.2), 3.2),               # Carlos va de Carlos
    (fija('p7', cierre(), 2.8, zoom=1.04), 2.8),                          # cierre con la fecha
]
with open(f'{TMP}/lista.txt', 'w') as fh:
    for p, _ in P:
        fh.write(f"file '{p}'\n")
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{TMP}/lista.txt', '-c', 'copy', f'{TMP}/video.mp4')

ini, t = [], 0.0
for _, d in P:
    ini.append(t)
    t += d
TOTAL = t

carlos = cartela('carlos', ['Carlos va de Carlos.'], 1380, 96)

voces = [
    (f'{EP}/voces/adri_claro.wav', 0, 1.95, ini[1], 1.0),
    (f'{EP}/voces/uri_todos.wav', 0, 1.7, ini[2], 1.0),
]
efectos = [
    (f'{SFX}/bip.mp3', 0, 0.6, ini[0] + 0.15, 0.7),
    (f'{SFX}/impacto.mp3', 0, 1.2, ini[2] + 0.15, 0.6),
    (f'{SFX}/trueno.mp3', 0, 2.0, ini[3] - 0.15, 0.9),
    (f'{SFX}/whoosh.mp3', 0, 0.7, ini[4] - 0.1, 0.6),
    (f'{SFX}/scratch1.mp3', 0, 0.8, ini[5] + 0.9, 0.5),                    # se corta la fiesta al ver a Carlos
    (f'{SFX}/impacto.mp3', 0, 1.4, ini[6], 0.5),
]


def mezcla(pistas, salida):
    args = ['ffmpeg', '-v', 'error', '-y']
    fil = []
    for j, (src, ss, dur, at, vol) in enumerate(pistas):
        args += ['-i', src]
        fil.append(f'[{j}]atrim={ss}:{ss + dur},asetpts=N/SR/TB,aformat=sample_rates=44100:channel_layouts=stereo,'
                   f'afade=t=out:st={max(dur - 0.05, 0)}:d=0.05,volume={vol},adelay={int(at * 1000)}|{int(at * 1000)}[a{j}]')
    n = len(pistas)
    fil.append(''.join(f'[a{j}]' for j in range(n)) + f'amix=inputs={n}:normalize=0,apad,atrim=0:{TOTAL},'
               'loudnorm=I=-14:TP=-1.5[out]')
    args += ['-filter_complex', ';'.join(fil), '-map', '[out]', '-ar', '44100', salida]
    sh(*args)


mezcla(voces + efectos, f'{TMP}/audio_voces.wav')
mezcla(efectos, f'{TMP}/audio_sfx.wav')

for audio, nombre in [(f'{TMP}/audio_voces.wav', 'EP03_halloween_movil.mp4'), (f'{TMP}/audio_sfx.wav', 'EP03_halloween_sin_voces_movil.mp4')]:
    sh('ffmpeg', '-v', 'error', '-y', '-i', f'{TMP}/video.mp4', '-i', carlos, '-i', audio,
       '-filter_complex', f"[0][1]overlay=enable='between(t,{ini[5] + 1.1},{ini[6]})'[v]",
       '-map', '[v]', '-map', '2:a', '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p',
       '-crf', '21', '-preset', 'slow', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(TOTAL),
       f'{EP}/{nombre}')

print(f'OK · {TOTAL:.2f} s')
