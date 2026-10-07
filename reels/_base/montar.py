#!/usr/bin/env python3
"""Monta un reel 1080x1920 a partir de imágenes numeradas, voz en off y escenas.

Uso: python3 reels/_base/montar.py <carpeta_reel>
La carpeta necesita: imagenes/01.png..NN.png, voz.mp3 (opcional: musica.mp3) y escenas.json:
  [{"inicio": 0.0, "fin": 3.0, "texto": "TU CUERPO LLEVA AÑOS…", "clave": "ELIMINAR"}, ...]
Salida: <carpeta_reel>/<NOMBRE_CARPETA>.mp4
"""
import json, os, subprocess, sys

FUENTE = os.path.join(os.path.dirname(__file__), '..', '..', 'posts', '_base', 'fuentes', 'DMSans-700.ttf')
W, H, FPS = 1080, 1920, 30

def esc(t):
    return t.replace('\\', '\\\\').replace(':', '\\:').replace("'", "’").replace('%', '\\%')

def main(carpeta):
    escenas = json.load(open(os.path.join(carpeta, 'escenas.json')))
    voz = os.path.join(carpeta, 'voz.mp3')
    musica = os.path.join(carpeta, 'musica.mp3')
    clips = []
    for i, e in enumerate(escenas, 1):
        img = os.path.join(carpeta, 'imagenes', f'{i:02d}.png')
        dur = e['fin'] - e['inicio']
        frames = max(1, round(dur * FPS))
        out = os.path.join(carpeta, f'.clip{i:02d}.mp4')
        # Zoom lento 100 -> 108 % centrado; el texto va en el centro, a la altura de los ojos
        zoom = f"zoompan=z='1+0.08*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS}"
        texto = esc(e.get('texto', ''))
        sub = (f"drawtext=fontfile='{FUENTE}':text='{texto}':fontsize=64:fontcolor=white:"
               f"borderw=4:bordercolor=black@0.6:x=(w-text_w)/2:y=h*0.62") if texto else 'null'
        vf = f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},{zoom},{sub},format=yuv420p"
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', img, '-vf', vf,
                        '-frames:v', str(frames), '-r', str(FPS), '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', out], check=True)
        clips.append(out)
    lista = os.path.join(carpeta, '.clips.txt')
    open(lista, 'w').write(''.join(f"file '{os.path.abspath(c)}'\n" for c in clips))
    nombre = os.path.basename(os.path.normpath(carpeta))
    salida = os.path.join(carpeta, f'{nombre}.mp4')
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lista]
    if os.path.exists(voz):
        cmd += ['-i', voz]
        if os.path.exists(musica):
            cmd += ['-i', musica, '-filter_complex', '[1:a]volume=1.0[v];[2:a]volume=0.18[m];[v][m]amix=inputs=2:duration=first[a]', '-map', '0:v', '-map', '[a]']
        else:
            cmd += ['-map', '0:v', '-map', '1:a']
        cmd += ['-c:a', 'aac', '-b:a', '192k', '-shortest']
    cmd += ['-c:v', 'copy', '-movflags', '+faststart', salida]
    subprocess.run(cmd, check=True)
    for c in clips: os.remove(c)
    os.remove(lista)
    print(salida)

if __name__ == '__main__':
    main(sys.argv[1])
