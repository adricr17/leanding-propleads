"""Crea las voces de IA del EP01 alineadas con la voz guía (mismos inicios y duraciones que los labios)."""
import subprocess, os
D = os.path.dirname(os.path.abspath(__file__)); RAW = f'{D}/raw'

def sh(*a): subprocess.run(a, check=True, capture_output=True)

def recorte(src, ss=None, to=None):
    """Devuelve un wav con la frase sin silencios de borde."""
    out = f'{RAW}/_seg_{os.path.basename(src)}_{ss}_{to}.wav'
    tr = f'atrim={ss}:{to},asetpts=N/SR/TB,' if ss is not None else ''
    sh('ffmpeg', '-y', '-i', src, '-af', tr + 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse', '-ac', '1', '-ar', '44100', out)
    return out

def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)

def atempo(r):
    f = []
    while r > 2.0: f.append('atempo=2.0'); r /= 2
    while r < 0.5: f.append('atempo=0.5'); r /= 0.5
    f.append(f'atempo={r:.4f}')
    return ','.join(f)

def montar(nombre, total, piezas):
    """piezas: (wav_frase, inicio, duración_objetivo)"""
    args = ['ffmpeg', '-y', '-f', 'lavfi', '-t', str(total), '-i', 'anullsrc=r=44100:cl=mono']
    fil = []
    for j, (src, at, target) in enumerate(piezas):
        args += ['-i', src]
        r = dur(src) / target
        fil.append(f'[{j + 1}]{atempo(r)},atrim=0:{target},adelay={int(at * 1000)}[p{j}]')
    fil.append('[0]' + ''.join(f'[p{j}]' for j in range(len(piezas))) + f'amix=inputs={len(piezas) + 1}:normalize=0,atrim=0:{total},loudnorm=I=-16:TP=-1.5[o]')
    sh(*args, '-filter_complex', ';'.join(fil), '-map', '[o]', '-ar', '44100', f'{D}/{nombre}')
    print(nombre, 'ok')

adri1 = recorte(f'{RAW}/adri.mp3', 0, 3.05); adri2 = recorte(f'{RAW}/adri.mp3', 3.6, 5.4)
uri_peq = recorte(f'{RAW}/uri.mp3', 0, 0.75); uri_no = recorte(f'{RAW}/uri.mp3', 1.4, 1.85); uri_per = recorte(f'{RAW}/uri.mp3', 2.3, 4.4)
and_hala = recorte(f'{RAW}/andrea.mp3', 0, 0.45); and_no = recorte(f'{RAW}/andrea_no.mp3'); and_pri = recorte(f'{RAW}/andrea_primero.mp3')
mei_madre = recorte(f'{RAW}/meii_madre.mp3'); mei_no = recorte(f'{RAW}/meii_no.mp3'); mei_es = recorte(f'{RAW}/meii_esmia.mp3')
kike_no = recorte(f'{RAW}/kike.mp3')

# Tiempos de la voz guía (ver EP01_algo_pequenito.md / transcripción del 18/10)
montar('voz_adri.wav', 5.13, [(adri1, 0.14, 2.72), (adri2, 3.64, 1.40)])
montar('uri_completo.wav', 7.1, [(uri_peq, 1.40, 0.72), (uri_no, 3.18, 0.30), (uri_per, 4.68, 1.36)])
montar('meii_completo.wav', 5.575, [(mei_madre, 1.30, 0.84), (mei_no, 3.14, 0.28), (mei_es, 4.30, 0.60)])
montar('andrea_completo.wav', 5.015, [(and_hala, 1.525, 0.34), (and_no, 2.285, 0.28), (and_pri, 3.225, 1.0)])
montar('kike_completo.wav', 2.77, [(kike_no, 1.35, 0.58)])
montar('C_meii_es_mia.wav', 1.5, [(mei_es, 0.40, 0.60)])
montar('D_andrea_yo_la_vi_primero.wav', 1.5, [(and_pri, 0.275, 1.0)])
montar('E_uri_el_estudio_es_mio.wav', 2.0, [(uri_per, 0.33, 1.36)])
