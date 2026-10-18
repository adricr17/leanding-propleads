"""Monta PHARAON SITCOM EP01 «Algo pequeñito».

Genera dos versiones en privado/sitcom-ep01/ (llevan la foto de la manga del cliente):
  EP01_guia_movil.mp4    -> con las voces guía (para revisar ritmo y labios)
  EP01_sin_voces_movil.mp4 -> solo efectos, para doblar encima en CapCut
Uso: python3 reels/PHARAON_SITCOM/ep01/montar_ep01.py
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

R = '/home/user/leanding-propleads'
EP = f'{R}/reels/PHARAON_SITCOM/ep01'
VG = f'{EP}/voces_guia'
PRIV = f'{R}/privado/sitcom-ep01'
SFX = f'{R}/reels/_base/sfx'
FUENTES = f'{R}/posts/_base/fuentes/'
TMP = f'{PRIV}/tmp'
os.makedirs(TMP, exist_ok=True)
W, H, FPS = 1080, 1920, 30

def sh(*a):
    subprocess.run(a, check=True)

def cartela(nombre, texto, y):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FUENTES + 'Anton-Regular.ttf', 92)
    w = d.textlength(texto, font=f)
    x = (W - w) / 2
    d.rounded_rectangle([x - 40, y - 24, x + w + 40, y + 130], radius=26, fill=(10, 10, 12, 215))
    d.text((x, y), texto, font=f, fill=(245, 238, 230))
    p = f'{TMP}/{nombre}.png'
    im.save(p)
    return p

# (archivo, inicio, duración, filtro extra de encuadre)
PLANOS = [
    (f'{EP}/A_adri_lipsync.mp4', 0.0, 3.05, ''),                 # 1 Adri lee el DM
    (f'{PRIV}/insert_movil.mp4', 0.0, 1.6, ''),                  # 2 la manga
    (f'{EP}/B_grupo_clip.mp4', 0.0, 1.5, ''),                    # 3 reacción
    (f'{EP}/A_adri_lipsync.mp4', 3.4, 1.73, ''),                 # 4 «Vale, le digo que no»
    (f'{EP}/B_grupo_clip.mp4', 1.9, 1.5, ''),                    # 5 «¡NO!»
    (f'{EP}/C_meii_lipsync.mp4', 0.0, 1.48, ''),                 # 6 Meii
    (f'{EP}/D_andrea_lipsync.mp4', 0.0, 1.48, ''),               # 7 Andrea
    (f'{EP}/E_uri_lipsync.mp4', 0.0, 1.97, ''),                  # 8 Uri
    (f'{EP}/F_kike_clip.mp4', 0.0, 4.6, 'scale=iw*1.35:-1,crop=iw/1.35:ih/1.35:(iw-iw/1.35)*0.75:ih-ih/1.35,'),  # 9 Kike (recorte para quitar el fondo)
]

# 1) normalizar cada plano a 1080x1920/30fps sin audio
segs = []
for i, (src, ss, dur, extra) in enumerate(PLANOS):
    out = f'{TMP}/p{i}.mp4'
    vf = f'{extra}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}'
    sh('ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', src, '-t', str(dur), '-vf', vf,
       '-an', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', out)
    segs.append((out, dur))

with open(f'{TMP}/lista.txt', 'w') as fh:
    for p, _ in segs:
        fh.write(f"file '{p}'\n")
sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{TMP}/lista.txt', '-c', 'copy', f'{TMP}/video.mp4')

ini = []
t = 0.0
for _, d in segs:
    ini.append(t)
    t += d
TOTAL = t

# 2) cartelas del final (plano de Kike)
c1 = cartela('c1', 'Mientras tanto, Kike:', 230)
c2 = cartela('c2', '¿Quién se la queda?', 230)
k = ini[8]

# 3) pistas de audio: (archivo, inicio_en_archivo, duración, momento_en_vídeo, volumen)
voces = [
    (f'{EP}/voz_adri.wav', 0.0, 3.05, ini[0], 1.0),
    (f'{VG}/uri_completo.wav', 1.35, 0.85, ini[2] + 0.15, 0.8),     # ¿Pequeñito?
    (f'{VG}/meii_completo.wav', 1.25, 0.95, ini[2] + 0.45, 0.7),    # Madre mía
    (f'{VG}/andrea_completo.wav', 1.48, 0.45, ini[2] + 0.95, 0.7),  # Hala
    (f'{EP}/voz_adri.wav', 3.4, 1.73, ini[3], 1.0),
    (f'{VG}/uri_completo.wav', 3.12, 0.4, ini[4] + 0.35, 0.9),      # ¡NO! x4
    (f'{VG}/meii_completo.wav', 3.08, 0.38, ini[4] + 0.37, 0.9),
    (f'{VG}/andrea_completo.wav', 2.24, 0.36, ini[4] + 0.36, 0.9),
    (f'{VG}/kike_completo.wav', 1.32, 0.65, ini[4] + 0.33, 0.9),
    (f'{VG}/C_meii_es_mia.wav', 0.0, 1.48, ini[5], 1.0),
    (f'{VG}/D_andrea_yo_la_vi_primero.wav', 0.0, 1.48, ini[6], 1.0),
    (f'{VG}/E_uri_el_estudio_es_mio.wav', 0.0, 1.97, ini[7], 1.0),
    (f'{VG}/C_meii_es_mia.wav', 0.3, 0.9, k + 0.6, 0.18),           # la pelea sigue de fondo
    (f'{VG}/D_andrea_yo_la_vi_primero.wav', 0.2, 1.1, k + 1.5, 0.18),
    (f'{VG}/E_uri_el_estudio_es_mio.wav', 0.25, 1.5, k + 2.7, 0.15),
]
efectos = [
    (f'{SFX}/whoosh.mp3', 0.0, 0.8, ini[1] - 0.1, 0.5),
    (f'{SFX}/impacto.mp3', 0.0, 1.6, ini[1] + 0.55, 0.9),          # revelación de la manga
    (f'{SFX}/whoosh.mp3', 0.0, 0.8, ini[4] + 0.2, 0.6),
    (f'{SFX}/whoosh.mp3', 0.0, 0.8, ini[5] - 0.1, 0.35),
    (f'{SFX}/whoosh.mp3', 0.0, 0.8, ini[6] - 0.1, 0.35),
    (f'{SFX}/whoosh.mp3', 0.0, 0.8, ini[7] - 0.1, 0.35),
]

def mezcla(pistas, salida):
    args = ['ffmpeg', '-v', 'error', '-y']
    fil = []
    for j, (src, ss, dur, at, vol) in enumerate(pistas):
        args += ['-i', src]
        fil.append(f'[{j}]atrim={ss}:{ss + dur},asetpts=N/SR/TB,aformat=sample_rates=44100:channel_layouts=stereo,'
                   f'volume={vol},adelay={int(at * 1000)}|{int(at * 1000)}[a{j}]')
    n = len(pistas)
    fil.append(''.join(f'[a{j}]' for j in range(n)) + f'amix=inputs={n}:normalize=0,apad,atrim=0:{TOTAL},'
               'loudnorm=I=-14:TP=-1.5[out]')
    args += ['-filter_complex', ';'.join(fil), '-map', '[out]', '-ar', '44100', salida]
    sh(*args)

mezcla(voces + efectos, f'{TMP}/audio_guia.wav')
mezcla(efectos, f'{TMP}/audio_sfx.wav')

for audio, nombre in [(f'{TMP}/audio_guia.wav', 'EP01_guia_movil.mp4'), (f'{TMP}/audio_sfx.wav', 'EP01_sin_voces_movil.mp4')]:
    sh('ffmpeg', '-v', 'error', '-y', '-i', f'{TMP}/video.mp4', '-i', c1, '-i', c2, '-i', audio,
       '-filter_complex',
       f"[0][1]overlay=enable='between(t,{k},{k + 1.9})'[v1];[v1][2]overlay=enable='between(t,{k + 2.4},{TOTAL})'[v]",
       '-map', '[v]', '-map', '3:a', '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p',
       '-crf', '21', '-preset', 'slow', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(TOTAL),
       f'{PRIV}/{nombre}')

print(f'OK · {TOTAL:.2f} s')
