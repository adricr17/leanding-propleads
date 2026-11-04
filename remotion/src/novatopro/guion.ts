// NOVATO vs PRO · EP01 «PEDIR CITA POR DM» (04/11/2026). 30 fps, 20 s. Tiempos en fotogramas.
import {Cara} from './Muneco';
import {Burbuja} from './Chat';

export const FPS = 30;
export const DURACION = 600;
export const TAREA = 'PEDIR CITA POR DM';

type Linea = {desde: number; hasta: number; texto: string};
type Estado = {desde: number; cara: Cara; brazo?: 'movil' | 'medir' | 'cafe' | 'abajo'; sudor?: boolean; temblor?: boolean; salto?: boolean};

export const NOVATO = {
  lineas: [
    {desde: 30, hasta: 70, texto: 'Vale… ¿qué le pongo?'},
    {desde: 108, hasta: 150, texto: '¿Me han dejado en visto?'},
    {desde: 196, hasta: 240, texto: '…buena pregunta.'},
    {desde: 250, hasta: 330, texto: 'Mejor te lo explico por audio…'},
    {desde: 348, hasta: 420, texto: '¿Les escribo también por WhatsApp?'},
    {desde: 438, hasta: 490, texto: '¡¡ME HA CONTESTADO!!'},
    {desde: 536, hasta: 584, texto: 'Vale… ¿y ahora qué le pongo?'},
  ] as Linea[],
  estados: [
    {desde: 0, cara: 'nervioso'},
    {desde: 100, cara: 'nervioso', sudor: true},
    {desde: 190, cara: 'mira'},
    {desde: 246, cara: 'normal'},
    {desde: 336, cara: 'nervioso', sudor: true, temblor: true},
    {desde: 430, cara: 'feliz', salto: true},
    {desde: 536, cara: 'nervioso'},
  ] as Estado[],
  chat: [
    {desde: 66, texto: 'hola', mia: true},
    {desde: 84, texto: 'holaaa', mia: true},
    {desde: 100, texto: '¿buenas?', mia: true},
    {desde: 156, texto: '¿precio?', mia: true},
    {desde: 186, texto: '¿De qué tatuaje? 😅'},
    {desde: 246, tipo: 'audio', mia: true},
    {desde: 340, texto: '??', mia: true},
    {desde: 360, texto: '???', mia: true},
    {desde: 430, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'},
  ] as Burbuja[],
  visto: 112,
};

export const PRO = {
  lineas: [
    {desde: 36, hasta: 70, texto: 'Un mensaje. Ya está.'},
    {desde: 92, hasta: 150, texto: 'Idea, zona, tamaño y fechas.'},
    {desde: 172, hasta: 240, texto: 'Y una referencia. Siempre.'},
    {desde: 258, hasta: 330, texto: 'Aquí. Diez centímetros. Fin.'},
    {desde: 344, hasta: 420, texto: 'Contestan en horario. Café.'},
    {desde: 466, hasta: 532, texto: 'A los dos. Lo leen todo.'},
  ] as Linea[],
  estados: [
    {desde: 0, cara: 'aburrido'},
    {desde: 250, cara: 'aburrido', brazo: 'medir'},
    {desde: 336, cara: 'aburrido', brazo: 'cafe'},
    {desde: 430, cara: 'aburrido', brazo: 'movil'},
  ] as Estado[],
  chat: [
    {desde: 70, mia: true, lineas: ['Idea: rosa fine line', 'Zona: antebrazo', 'Tamaño: 10 cm', 'Fechas: martes o jueves'], lineaCada: 7},
    {desde: 162, tipo: 'foto', mia: true},
    {desde: 430, texto: '¡Hola! ¿Te va el jueves a las 11? 💜'},
  ] as Burbuja[],
};

// [archivo de public/sfx, fotograma, volumen]
export const EFECTOS: [string, number, number][] = [
  ['whoosh.mp3', 0, 0.5],
  ['bip.mp3', 66, 0.35], ['bip.mp3', 84, 0.35], ['bip.mp3', 100, 0.35],
  ['bip.mp3', 70, 0.35],
  ['bip.mp3', 156, 0.35], ['bip.mp3', 162, 0.35], ['impacto.mp3', 186, 0.35],
  ['bip.mp3', 246, 0.35], ['whoosh.mp3', 250, 0.4],
  ['bip.mp3', 340, 0.35], ['bip.mp3', 360, 0.35],
  ['impacto.mp3', 430, 0.55],
  ['whoosh.mp3', 585, 0.45],
];
