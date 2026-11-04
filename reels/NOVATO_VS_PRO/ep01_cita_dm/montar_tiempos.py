"""EP01: corta las dos tomas de ElevenLabs en frases, las acelera un 20 % y genera remotion/src/novatopro/guion.ts
con la línea de tiempo secuencial (nunca hablan los dos a la vez). Uso: python3 reels/NOVATO_VS_PRO/ep01_cita_dm/montar_tiempos.py"""
import os, subprocess
R = '/home/user/leanding-propleads'
V = f'{R}/reels/NOVATO_VS_PRO/ep01_cita_dm/voces'
OUT = f'{R}/remotion/public/voces/np_ep01'
os.makedirs(OUT, exist_ok=True)
FPS, TEMPO, HUECO = 30, 1.25, 0.12

# tramos (s) de cada toma, sacados de los silencios (> 0,5 s)
NOV = [(0.0, 2.42), (3.48, 4.72), (5.59, 7.11), (7.88, 10.10), (10.91, 12.56), (13.26, 14.31), (14.91, 17.63)]
PRO = [(0.0, 1.72), (3.02, 5.79), (6.56, 8.42), (9.62, 12.88), (13.87, 16.38), (17.26, 19.41)]
TXT_N = ['Vale… ¿qué le pongo?', '¿Me han dejado en visto?', '…buena pregunta.', 'Mejor te lo explico por audio…',
         '¿Les escribo también por WhatsApp?', '¡¡ME HA CONTESTADO!!', 'Vale… ¿y ahora qué le pongo?']
TXT_P = ['Un mensaje. Ya está.', 'Idea, zona, tamaño y fechas.', 'Y una referencia. Siempre.', 'Aquí. Diez centímetros. Fin.',
         'Contestan en horario. Café.', 'A los dos. Lo leen todo.']

def corta(src, a, b, nombre):
    out = f'{OUT}/{nombre}.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-af',
                    f'atrim={a}:{b},asetpts=N/SR/TB,silenceremove=start_periods=1:start_threshold=-50dB,areverse,'
                    f'silenceremove=start_periods=1:start_threshold=-50dB,areverse,atempo={TEMPO}',
                    '-ar', '44100', out], check=True)
    d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout)
    return d

dN = [corta(f'{V}/novato_toma.mp3', a, b, f'n{i+1}') for i, (a, b) in enumerate(NOV)]
dP = [corta(f'{V}/pro_toma.mp3', a, b, f'p{i+1}') for i, (a, b) in enumerate(PRO)]

# orden de las frases (la n3 «…buena pregunta» se queda muda: gag visual)
orden = [('n', 0), ('p', 0), ('n', 1), ('p', 1), ('p', 2), ('n', 3), ('p', 3), ('n', 4), ('p', 4), ('n', 5), ('p', 5), ('n', 6)]
t = 1.0  # el rótulo ocupa el primer segundo
ini = {}
for quien, i in orden:
    d = (dN if quien == 'n' else dP)[i]
    if (quien, i) == ('p', 2): t += 0.9       # respiro: la respuesta «¿De qué tatuaje?» y la mirada a cámara, sin palabras
    if (quien, i) == ('n', 5): t += 0.3       # la respuesta del estudio entra antes del grito
    ini[(quien, i)] = (t, d)
    t += d + HUECO
FIN = t + 0.35
f = lambda s: int(round(s * FPS))
def L(q, i, txt): a, d = ini[(q, i)]; return f"    {{desde: {f(a)}, hasta: {f(a + d) + 4}, texto: '{txt}', audio: '{q}{i+1}'}},"
lineasN = '\n'.join(L('n', i, TXT_N[i]) for i in (0, 1, 3, 4, 5, 6))
lineasP = '\n'.join(L('p', i, TXT_P[i]) for i in range(6))
n = lambda q, i, off=0.0: f(ini[(q, i)][0] + off)
fin_n2 = f(ini[('n', 1)][0])
DUR = f(FIN) + 18
ts = f"""// NOVATO vs PRO · EP01 «PEDIR CITA POR DM». GENERADO por reels/NOVATO_VS_PRO/ep01_cita_dm/montar_tiempos.py: no editar a mano.
// 30 fps. Voces de ElevenLabs (Efrayn = NOVATO, Bruno = PRO) cortadas en frases y aceleradas x{TEMPO}. Nunca hablan los dos a la vez.
import {{Cara}} from './Muneco';
import {{Burbuja}} from './Chat';

export const FPS = 30;
export const DURACION = {DUR};
export const TAREA = 'PEDIR CITA POR DM';
export const CIERRE = {DUR - 16};

type Linea = {{desde: number; hasta: number; texto: string; audio: string}};
type Estado = {{desde: number; cara: Cara; brazo?: 'movil' | 'medir' | 'cafe' | 'abajo'; sudor?: boolean; temblor?: boolean; salto?: boolean}};

export const NOVATO = {{
  lineas: [
{lineasN}
  ] as Linea[],
  estados: [
    {{desde: 0, cara: 'nervioso'}},
    {{desde: {n('n',1,-0.6)}, cara: 'nervioso', sudor: true}},
    {{desde: {n('p',2,-0.9)}, cara: 'mira'}},
    {{desde: {n('n',3,-0.3)}, cara: 'normal'}},
    {{desde: {n('n',4,-0.6)}, cara: 'nervioso', sudor: true, temblor: true}},
    {{desde: {n('n',5,-0.3)}, cara: 'feliz', salto: true}},
    {{desde: {n('n',6,-0.2)}, cara: 'nervioso'}},
  ] as Estado[],
  chat: [
    {{desde: {n('p',0,1.0)}, texto: 'hola', mia: true}},
    {{desde: {n('p',0,1.35)}, texto: 'holaaa', mia: true}},
    {{desde: {n('n',1,-0.25)}, texto: '¿buenas?', mia: true}},
    {{desde: {n('p',1,1.5)}, texto: '¿precio?', mia: true}},
    {{desde: {n('p',2,-0.8)}, texto: '¿De qué tatuaje? 😅'}},
    {{desde: {n('n',3,-0.15)}, tipo: 'audio', mia: true}},
    {{desde: {n('n',4,-0.5)}, texto: '??', mia: true}},
    {{desde: {n('n',4,-0.2)}, texto: '???', mia: true}},
    {{desde: {n('n',5,-0.3)}, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'}},
  ] as Burbuja[],
  visto: {fin_n2 - 6},
}};

export const PRO = {{
  lineas: [
{lineasP}
  ] as Linea[],
  estados: [
    {{desde: 0, cara: 'aburrido'}},
    {{desde: {n('p',3,-0.4)}, cara: 'aburrido', brazo: 'medir'}},
    {{desde: {n('p',4,-0.4)}, cara: 'aburrido', brazo: 'cafe'}},
    {{desde: {n('n',5,-0.3)}, cara: 'aburrido', brazo: 'movil'}},
  ] as Estado[],
  chat: [
    {{desde: {n('p',1,-0.1)}, mia: true, lineas: ['Idea: rosa fine line', 'Zona: antebrazo', 'Tamaño: 10 cm', 'Fechas: martes o jueves'], lineaCada: 12}},
    {{desde: {n('p',2,-0.2)}, tipo: 'foto', mia: true}},
    {{desde: {n('n',5,-0.3)}, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'}},
  ] as Burbuja[],
}};

// [archivo de public/sfx, fotograma, volumen]
export const EFECTOS: [string, number, number][] = [
  ['whoosh.mp3', 0, 0.5],
  ['bip.mp3', {n('p',0,1.0)}, 0.3], ['bip.mp3', {n('p',0,1.35)}, 0.3], ['bip.mp3', {n('n',1,-0.25)}, 0.3],
  ['bip.mp3', {n('p',1,-0.1)}, 0.3],
  ['bip.mp3', {n('p',1,1.5)}, 0.3], ['impacto.mp3', {n('p',2,-0.8)}, 0.3], ['bip.mp3', {n('p',2,-0.2)}, 0.3],
  ['bip.mp3', {n('n',3,-0.15)}, 0.3],
  ['bip.mp3', {n('n',4,-0.5)}, 0.3], ['bip.mp3', {n('n',4,-0.2)}, 0.3],
  ['impacto.mp3', {n('n',5,-0.3)}, 0.5],
  ['whoosh.mp3', {DUR - 16}, 0.45],
];
"""
open(f'{R}/remotion/src/novatopro/guion.ts', 'w').write(ts)
print('duración', DUR / FPS, 's')
for k, (a, d) in sorted(ini.items(), key=lambda x: x[1][0]): print(k, round(a, 2), round(d, 2))
