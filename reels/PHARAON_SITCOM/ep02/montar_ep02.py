"""Monta PHARAON SITCOM EP02 «La guerra de la música».

Salidas (reels/PHARAON_SITCOM/ep02/):
  EP02_guia_movil.mp4      -> con las voces guía de IA (para copiar el ritmo al doblar)
  EP02_sin_voces_movil.mp4 -> solo efectos, para doblar encima en CapCut
Uso: python3 reels/PHARAON_SITCOM/ep02/montar_ep02.py
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

R = '/home/user/leanding-propleads'
EP = f'{R}/reels/PHARAON_SITCOM/ep02'
EP1 = f'{R}/reels/PHARAON_SITCOM/ep01'
V2 = os.environ.get('VOCES') == 'v2'  # voces definitivas del casting
VG = f'{EP}/voces_v2' if V2 else f'{EP}/voces_guia'
SFX = f'{R}/reels/_base/sfx'
FUENTES = f'{R}/posts/_base/fuentes/'
TMP = f'{EP}/tmp'
os.makedirs(TMP, exist_ok=True)
W, H, FPS = 1080, 1920, 30


def sh(*a):
    subprocess.run(a, check=True)


def font(n, s):
    return ImageFont.truetype(FUENTES + n, s)


def cartela(nombre, lineas, y, size=88):
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


def fija(nombre, img, dur, zoom=1.12):
    """Plano a partir de una imagen fija con un zoom suave (0 créditos)."""
    out = f'{TMP}/{nombre}.mp4'
    n = int(dur * FPS)
    sh('ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', img, '-vf',
       f'scale={W * 2}:{H * 2},zoompan=z=\'1+{zoom - 1}*on/{n}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={n}:s={W}x{H}:fps={FPS},setsar=1',
       '-t', str(dur), '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out)
    return out


# --- inserto del altavoz: recorte de N2 con el texto en la pantalla ---
BASE_ALT = Image.open(f'{EP}/N2_altavoz.png').convert('RGB').crop((300, 600, 860, 1596)).resize((W, H), Image.LANCZOS)
PANT = (270, 440, 680, 655)  # pantalla del altavoz en el recorte


def altavoz(nombre, texto, dur):
    im = BASE_ALT.copy()
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = PANT
    d.rectangle(PANT, fill=(205, 225, 235))
    lineas = texto.split('\n')
    f = font('SpaceMono-700.ttf', 62)
    alto = 72
    yy = (y0 + y1) / 2 - alto * len(lineas) / 2
    for i, l in enumerate(lineas):
        d.text(((x0 + x1) / 2 - d.textlength(l, font=f) / 2, yy + i * alto), l, font=f, fill=(20, 24, 30))
    p = f'{TMP}/{nombre}.png'
    im.save(p)
    return fija(nombre, p, dur, zoom=1.06)


def movil_cliente():
    im = Image.new('RGB', (W, H), (14, 14, 18))
    d = ImageDraw.Draw(im)
    d.text((80, 170), 'Lista del cliente', font=font('DMSans-700.ttf', 58), fill=(240, 240, 240))
    d.rounded_rectangle([80, 300, W - 80, 900], radius=40, fill=(30, 46, 70))
    d.text((W / 2, 600), '~ ~ ~', font=font('DMSans-700.ttf', 120), fill=(140, 190, 230), anchor='mm')
    d.text((80, 960), 'Meditación profunda', font=font('DMSans-700.ttf', 66), fill=(245, 245, 245))
    d.text((80, 1050), 'Sonidos de ballena', font=font('DMSans-500.ttf', 52), fill=(170, 175, 185))
    d.text((80, 1130), '3 h 47 min', font=font('DMSans-500.ttf', 52), fill=(170, 175, 185))
    d.rounded_rectangle([80, 1300, W - 80, 1312], radius=6, fill=(60, 60, 70))
    d.rounded_rectangle([80, 1300, 200, 1312], radius=6, fill=(140, 190, 230))
    d.ellipse([W / 2 - 70, 1420, W / 2 + 70, 1560], fill=(240, 240, 240))
    d.polygon([(W / 2 - 22, 1455), (W / 2 - 22, 1525), (W / 2 + 35, 1490)], fill=(14, 14, 18))
    p = f'{TMP}/movil.png'
    im.save(p)
    return p


def clip(nombre, src, ss, dur):
    out = f'{TMP}/{nombre}.mp4'
    sh('ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', src, '-t', str(dur), '-vf',
       f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}',
       '-an', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out)
    return out


# --- planos ---
P = []
P.append((fija('p01', f'{EP}/N1_meii_altavoz.png', 1.8), 1.8))                  # 1 Meii pone su música
P.append((altavoz('p02', 'Playlist\nde Meii', 0.8), 0.8))                       # 2
P.append((clip('p03', f'{EP}/D_andrea_lipsync.mp4', 0, 1.4), 1.4))               # 3 «¡Ni de broma!»
P.append((altavoz('p04', 'Playlist\nde Andrea', 0.8), 0.8))                     # 4
P.append((fija('p05', f'{EP1}/C_meii.png', 1.3, zoom=1.15), 1.3))               # 5 Meii contraataca
P.append((altavoz('p06', 'Playlist\nde Meii', 0.7), 0.7))                       # 6
P.append((clip('p07', f'{EP}/N3_duelo_clip.mp4', 0.3, 1.5), 1.5))                # 7 duelo
for i, t in enumerate(['Meii', 'Andrea', 'Meii', 'Andrea']):                     # 8 ráfaga
    P.append((altavoz(f'p08_{i}', f'Playlist\nde {t}', 0.25), 0.25))
P.append((clip('p09', f'{EP}/E_uri_lipsync.mp4', 0, 1.75), 1.75))                # 9 Uri
P.append((clip('p10', f'{EP}/N3_duelo_clip.mp4', 3.9, 1.1), 1.1))                # 10 se giran («Chicos…»)
P.append((clip('p11', f'{EP}/A_adri_lipsync.mp4', 0, 1.97), 1.97))               # 11 Adri
P.append((fija('p12', movil_cliente(), 1.5, zoom=1.08), 1.5))                   # 12 lista del cliente
P.append((clip('p13', f'{EP}/N4_sufrimiento_clip.mp4', 0.5, 1.9), 1.9))          # 13 sufrimiento
# 14 congelado oscurecido con la regla
sh('ffmpeg', '-v', 'error', '-y', '-sseof', '-0.1', '-i', f'{TMP}/p13.mp4', '-frames:v', '1', f'{TMP}/p13_last.png')
ImageEnhance.Brightness(Image.open(f'{TMP}/p13_last.png')).enhance(0.45).save(f'{TMP}/p14.png')
P.append((fija('p14', f'{TMP}/p14.png', 1.6, zoom=1.03), 1.6))
P.append((clip('p15', f'{EP}/N5_carlos_clip.mp4', 0.0, 4.2), 4.2))               # 15 Carlos

with open(f'{TMP}/lista.txt', 'w') as fh:
    for p, _ in P:
        fh.write(f"file '{p}'\n")
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{TMP}/lista.txt', '-c', 'copy', f'{TMP}/video.mp4')

ini, t = [], 0.0
for _, d in P:
    ini.append(t)
    t += d
TOTAL = t
# índices útiles
I_ANDREA, I_ALT2, I_ALT3, I_DUELO, I_RAF, I_URI, I_GIRO, I_ADRI, I_MOVIL, I_SUFRE, I_REGLA, I_CARLOS = 2, 3, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17

hook = cartela('hook', ['¿Quién pone la música', 'en un estudio de tatuajes?'], 200, 80)
regla = cartela('regla', ['REGLA DE LA CASA:', 'la música la pone', 'el cliente.'], 700, 96)
pregunta = cartela('pregunta', ['¿Qué canción pondrías', 'tú en la camilla?'], 1380, 80)

voces = [
    (f'{VG}/D_andrea_ni_de_broma.wav', 0, 1.4, ini[I_ANDREA], 1.0),
    (f'{VG}/E_uri_se_acabo.wav', 0, 1.75, ini[I_URI], 1.0),
    (f'{VG}/adri_chicos_off.wav', 0, 0.68, ini[I_GIRO] + 0.05, 0.9),
    (f'{VG}/A_adri_la_musica.wav', 0, 1.97, ini[I_ADRI], 1.0),
]
efectos = [
    (f'{SFX}/bip.mp3', 0, 0.6, ini[1], 0.7),
    (f'{SFX}/scratch1.mp3', 0, 0.9, ini[I_ALT2] - 0.05, 0.9),
    (f'{SFX}/scratch2.mp3', 0, 0.9, ini[I_ALT3] - 0.05, 0.9),
    (f'{SFX}/whoosh.mp3', 0, 0.6, ini[I_DUELO], 0.4),
]
for k in range(4):
    efectos.append((f'{SFX}/scratch{1 + k % 2}.mp3', 0, 0.3, ini[I_RAF + k], 0.85))
efectos += [
    (f'{SFX}/scratch1.mp3', 0, 0.8, ini[I_GIRO] - 0.05, 0.6),        # corte en seco al «Chicos…»
    (f'{SFX}/ballena.mp3', 0, 5.0, ini[I_MOVIL] + 0.2, 0.8),
    (f'{SFX}/impacto.mp3', 0, 1.4, ini[I_REGLA], 0.6),
    (f'{SFX}/ballena.mp3', 1.0, 0.5, ini[I_CARLOS], 0.6),             # la ballena sigue hasta el desenchufe
    (f'{SFX}/desenchufe.mp3', 0, 1.2, ini[I_CARLOS] + 0.45, 1.0),
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


mezcla(voces + efectos, f'{TMP}/audio_guia.wav')
mezcla(efectos, f'{TMP}/audio_sfx.wav')

c = ini[I_CARLOS]
salidas = [(f'{TMP}/audio_guia.wav', 'EP02_voces_v2_movil.mp4')] if V2 else [(f'{TMP}/audio_guia.wav', 'EP02_guia_movil.mp4'), (f'{TMP}/audio_sfx.wav', 'EP02_sin_voces_movil.mp4')]
for audio, nombre in salidas:
    sh('ffmpeg', '-v', 'error', '-y', '-i', f'{TMP}/video.mp4', '-i', hook, '-i', regla, '-i', pregunta, '-i', audio,
       '-filter_complex',
       f"[0][1]overlay=enable='between(t,0,{ini[2]})'[v1];"
       f"[v1][2]overlay=enable='between(t,{ini[I_REGLA] + 0.1},{ini[I_CARLOS]})'[v2];"
       f"[v2][3]overlay=enable='between(t,{c + 2.0},{TOTAL})'[v]",
       '-map', '[v]', '-map', '4:a', '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p',
       '-crf', '21', '-preset', 'slow', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(TOTAL),
       f'{EP}/{nombre}')

print(f'OK · {TOTAL:.2f} s')
