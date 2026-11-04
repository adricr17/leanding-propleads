// NOVATO vs PRO · EP01 «PEDIR CITA POR DM». GENERADO por reels/NOVATO_VS_PRO/ep01_cita_dm/montar_tiempos.py: no editar a mano.
// 30 fps. Voces de ElevenLabs (Efrayn = NOVATO, Bruno = PRO) cortadas en frases y aceleradas x1.25. Nunca hablan los dos a la vez.
import {Cara} from './Muneco';
import {Burbuja} from './Chat';

export const FPS = 30;
export const DURACION = 743;
export const TAREA = 'PEDIR CITA POR DM';
export const CIERRE = 727;

type Linea = {desde: number; hasta: number; texto: string; audio: string};
type Estado = {desde: number; cara: Cara; brazo?: 'movil' | 'medir' | 'cafe' | 'abajo'; sudor?: boolean; temblor?: boolean; salto?: boolean};

export const NOVATO = {
  lineas: [
    {desde: 30, hasta: 90, texto: 'Vale… ¿qué le pongo?', audio: 'n1'},
    {desde: 135, hasta: 169, texto: '¿Me han dejado en visto?', audio: 'n2'},
    {desde: 314, hasta: 372, texto: 'Mejor te lo explico por audio…', audio: 'n4'},
    {desde: 453, hasta: 497, texto: '¿Les escribo también por WhatsApp?', audio: 'n5'},
    {desde: 570, hasta: 600, texto: '¡¡ME HA CONTESTADO!!', audio: 'n6'},
    {desde: 650, hasta: 715, texto: 'Vale… ¿y ahora qué le pongo?', audio: 'n7'},
  ] as Linea[],
  estados: [
    {desde: 0, cara: 'nervioso'},
    {desde: 117, cara: 'nervioso', sudor: true},
    {desde: 239, cara: 'mira'},
    {desde: 305, cara: 'normal'},
    {desde: 435, cara: 'nervioso', sudor: true, temblor: true},
    {desde: 561, cara: 'feliz', salto: true},
    {desde: 644, cara: 'nervioso'},
  ] as Estado[],
  chat: [
    {desde: 120, texto: 'hola', mia: true},
    {desde: 130, texto: 'holaaa', mia: true},
    {desde: 127, texto: '¿buenas?', mia: true},
    {desde: 213, texto: '¿precio?', mia: true},
    {desde: 242, texto: '¿De qué tatuaje? 😅'},
    {desde: 309, tipo: 'audio', mia: true},
    {desde: 438, texto: '??', mia: true},
    {desde: 447, texto: '???', mia: true},
    {desde: 561, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'},
  ] as Burbuja[],
  visto: 129,
};

export const PRO = {
  lineas: [
    {desde: 90, hasta: 135, texto: 'Un mensaje. Ya está.', audio: 'p1'},
    {desde: 168, hasta: 239, texto: 'Idea, zona, tamaño y fechas.', audio: 'p2'},
    {desde: 266, hasta: 314, texto: 'Y una referencia. Siempre.', audio: 'p3'},
    {desde: 371, hasta: 454, texto: 'Aquí. Diez centímetros. Fin.', audio: 'p4'},
    {desde: 497, hasta: 561, texto: 'Contestan en horario. Café.', audio: 'p5'},
    {desde: 599, hasta: 650, texto: 'A los dos. Lo leen todo.', audio: 'p6'},
  ] as Linea[],
  estados: [
    {desde: 0, cara: 'aburrido'},
    {desde: 359, cara: 'aburrido', brazo: 'medir'},
    {desde: 485, cara: 'aburrido', brazo: 'cafe'},
    {desde: 561, cara: 'aburrido', brazo: 'movil'},
  ] as Estado[],
  chat: [
    {desde: 165, mia: true, lineas: ['Idea: rosa fine line', 'Zona: antebrazo', 'Tamaño: 10 cm', 'Fechas: martes o jueves'], lineaCada: 12},
    {desde: 260, tipo: 'foto', mia: true},
    {desde: 561, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'},
  ] as Burbuja[],
};

// [archivo de public/sfx, fotograma, volumen]
export const EFECTOS: [string, number, number][] = [
  ['whoosh.mp3', 0, 0.5],
  ['bip.mp3', 120, 0.3], ['bip.mp3', 130, 0.3], ['bip.mp3', 127, 0.3],
  ['bip.mp3', 165, 0.3],
  ['bip.mp3', 213, 0.3], ['impacto.mp3', 242, 0.3], ['bip.mp3', 260, 0.3],
  ['bip.mp3', 309, 0.3],
  ['bip.mp3', 438, 0.3], ['bip.mp3', 447, 0.3],
  ['impacto.mp3', 561, 0.5],
  ['whoosh.mp3', 727, 0.45],
];
