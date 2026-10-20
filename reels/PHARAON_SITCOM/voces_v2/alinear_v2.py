"""Voces definitivas (casting 20/10/2026, todas las opciones B) alineadas con los labios de EP01-EP03.

Adri = Emilio Salcedo (ElevenLabs v3) · Uri = Fenrir · Andrea = Leda · Meii = Laomedeia · Kike = Achird (Google).
Genera ep01/voces_v2/, ep02/voces_v2/ y ep03/voces_v2/ con los mismos nombres de archivo que usan los montajes.
"""
import os, subprocess
B = os.path.dirname(os.path.abspath(__file__)); RAW = f'{B}/raw'; S = os.path.dirname(B)

def sh(*a): subprocess.run(a, check=True, capture_output=True)
def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)

def frase(nombre, src, tramos=None):
    """Recorta (y une con 0,12 s de pausa) los tramos de una toma y quita silencios de borde."""
    out = f'{RAW}/_{nombre}.wav'
    if tramos:
        args = ['ffmpeg', '-y']; fil = []
        for j, (a, b) in enumerate(tramos):
            args += ['-i', src]
            fil.append(f'[{j}]atrim={a}:{b},asetpts=N/SR/TB,aresample=44100,aformat=channel_layouts=mono[t{j}]')
        n = len(tramos)
        sil = f'anullsrc=r=44100:cl=mono,atrim=0:0.12[s]'
        if n > 1:
            fil.append(sil)
            seq = ''.join(f'[t{j}]' + ('[s]' if j < n - 1 else '') for j in range(n))
            # un solo anullsrc no se puede reutilizar: duplicarlo
            fil[-1] = f'anullsrc=r=44100:cl=mono,atrim=0:0.12,asplit={n - 1}' + ''.join(f'[s{k}]' for k in range(n - 1))
            seq = ''.join(f'[t{j}]' + (f'[s{j}]' if j < n - 1 else '') for j in range(n))
            fil.append(f'{seq}concat=n={2 * n - 1}:v=0:a=1[c]')
        else:
            fil.append('[t0]anull[c]')
        sh(*args, '-filter_complex', ';'.join(fil), '-map', '[c]', f'{RAW}/_tmp.wav')
        src = f'{RAW}/_tmp.wav'
    sh('ffmpeg', '-y', '-i', src, '-af', 'silenceremove=start_periods=1:start_threshold=-42dB,areverse,silenceremove=start_periods=1:start_threshold=-42dB,areverse',
       '-ac', '1', '-ar', '44100', out)
    return out

def atempo(r):
    r = max(0.85, min(r, 1.5)); return f'atempo={r:.4f}'

def montar(destino, total, piezas):
    """piezas: (frase, inicio, duración objetivo | None = natural)"""
    args = ['ffmpeg', '-y', '-f', 'lavfi', '-t', str(total), '-i', 'anullsrc=r=44100:cl=mono']; fil = []
    for j, (src, at, target) in enumerate(piezas):
        args += ['-i', src]
        d = dur(src)
        tempo = atempo(d / target) if target else 'anull'
        fil.append(f'[{j + 1}]{tempo},adelay={int(at * 1000)}[p{j}]')
    fil.append('[0]' + ''.join(f'[p{j}]' for j in range(len(piezas))) + f'amix=inputs={len(piezas) + 1}:normalize=0,atrim=0:{total},loudnorm=I=-16:TP=-1.5[o]')
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    sh(*args, '-filter_complex', ';'.join(fil), '-map', '[o]', '-ar', '44100', destino)
    print(os.path.relpath(destino, S), 'ok')

hola = frase('hola', f'{RAW}/adri_hola'); vale = frase('vale', f'{RAW}/adri_vale')
chicos = frase('chicos', f'{RAW}/adri_chicos'); musica = frase('musica', f'{RAW}/adri_musica'); claro = frase('claro', f'{RAW}/adri_claro')
u_peq = frase('u_peq', f'{RAW}/uri_peq_seacabo', [(0.25, 1.22)]); u_seacabo = frase('u_seacabo', f'{RAW}/uri_peq_seacabo', [(3.25, 4.22), (4.88, 5.32)])
u_no = frase('u_no', f'{RAW}/uri_no')
u_todos = frase('u_todos', f'{RAW}/uri_todos_perdona', [(0.5, 1.96)]); u_perdona = frase('u_perdona', f'{RAW}/uri_todos_perdona', [(3.58, 4.16), (5.02, 6.95)])
a_hala = frase('a_hala', f'{RAW}/andrea_hala2', [(0.22, 1.08)]); a_no = frase('a_no', f'{RAW}/andrea_no')
a_primero = frase('a_primero', f'{RAW}/andrea_nibroma_primero', [(1.68, 2.75)]); a_nibroma = frase('a_nibroma', f'{RAW}/andrea_nibroma')
m_madre = frase('m_madre', f'{RAW}/meii_madre'); m_no = frase('m_no', f'{RAW}/meii_no'); m_es = frase('m_es', f'{RAW}/meii_esmia')
k_no = frase('k_no', f'{RAW}/kike_no')

E1, E2, E3 = f'{S}/ep01/voces_v2', f'{S}/ep02/voces_v2', f'{S}/ep03/voces_v2'
# EP01 (tiempos de la voz guía del 18/10; frases con labios ajustadas, reacciones al ritmo natural)
montar(f'{E1}/voz_adri.wav', 5.13, [(hola, 0.14, 2.72), (vale, 3.64, 1.15)])
montar(f'{E1}/uri_completo.wav', 7.1, [(u_peq, 1.40, None), (u_no, 3.18, None), (u_perdona, 4.6, 1.72)])
montar(f'{E1}/meii_completo.wav', 5.575, [(m_madre, 1.30, None), (m_no, 3.14, None), (m_es, 4.30, 0.72)])
montar(f'{E1}/andrea_completo.wav', 5.015, [(a_hala, 1.525, None), (a_no, 2.285, None), (a_primero, 3.225, 1.0)])
montar(f'{E1}/kike_completo.wav', 2.77, [(k_no, 1.35, None)])
montar(f'{E1}/C_meii_es_mia.wav', 1.5, [(m_es, 0.38, 0.72)])
montar(f'{E1}/D_andrea_yo_la_vi_primero.wav', 1.5, [(a_primero, 0.275, 1.0)])
montar(f'{E1}/E_uri_el_estudio_es_mio.wav', 2.0, [(u_perdona, 0.2, 1.72)])
# EP02
montar(f'{E2}/D_andrea_ni_de_broma.wav', 1.4, [(a_nibroma, 0.22, 0.85)])
montar(f'{E2}/E_uri_se_acabo.wav', 1.75, [(u_seacabo, 0.12, 1.55)])
montar(f'{E2}/adri_chicos_off.wav', 0.9, [(chicos, 0.0, None)])
montar(f'{E2}/A_adri_la_musica.wav', 2.0, [(musica, 0.08, 1.65)])
# EP03
montar(f'{E3}/adri_claro.wav', 1.95, [(claro, 0.10, 1.45)])
montar(f'{E3}/uri_todos.wav', 1.7, [(u_todos, 0.10, 1.35)])
