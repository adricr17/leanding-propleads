// «PHARAON, EN 1 MINUTO» · 5 episodios (04/11/2026). Cada escena = una frase de la voz en off.
// Item: icono | tarjeta | numero | sello. x, y = centro en px (1080 de ancho; zona de contenido y 430-1330). t = momento de entrada (0-1 de la escena).
export type Item =
  | {k: 'icono'; i: string; x: number; y: number; s?: number; t?: number}
  | {k: 'tarjeta'; texto: string; sub?: string; x: number; y: number; w?: number; t?: number; color?: 'morado' | 'blanco' | 'negro'}
  | {k: 'numero'; n: string; sub: string; x: number; y: number; t?: number}
  | {k: 'sello'; texto: string; x: number; y: number; t?: number; color?: 'rojo' | 'verde' | 'morado'};
export type Escena = {titulo: string; voz: string; items: Item[]};
export type Episodio = {id: string; tema: string; escenas: Escena[]; fuentes: string[]};

const SIGUENOS: Escena = {titulo: '<a>Síguenos</a>', voz: 'Síguenos para entender los tatuajes en un minuto.', items: [{k: 'tarjeta', texto: '@pharaonstudio', sub: 'Tatuajes, en 1 minuto', x: 540, y: 800, w: 720, color: 'blanco'}, {k: 'sello', texto: 'SEGUIR ✓', x: 690, y: 980, t: 0.4, color: 'morado'}]};

export const EPISODIOS: Episodio[] = [
  {
    id: 'ep01_tintas', tema: 'Europa prohibió colores de tinta',
    fuentes: ['Reglamento (UE) 2020/2081 (REACH, anexo XVII): aplicación 4/1/2022; Pigment Blue 15:3 y Green 7 desde 4/1/2023 (BfR; ECHA, webinar 29/03/2022).'],
    escenas: [
      {titulo: '<a>Europa</a> prohibió colores de tinta', voz: 'En Europa hay colores de tinta que ya no se pueden usar. ¿Lo sabías?', items: [{k: 'icono', i: 'ue', x: 300, y: 760, s: 300}, {k: 'icono', i: 'azul', x: 640, y: 700, s: 200, t: 0.3}, {k: 'icono', i: 'verde', x: 850, y: 700, s: 200, t: 0.4}, {k: 'sello', texto: 'PROHIBIDOS', x: 740, y: 950, t: 0.6, color: 'rojo'}]},
      {titulo: '1 · La <a>norma</a>', voz: 'Se llama REACH, y desde enero de 2022 limita las sustancias peligrosas de las tintas.', items: [{k: 'icono', i: 'libro', x: 300, y: 760, s: 280}, {k: 'tarjeta', texto: 'REACH', sub: 'norma europea', x: 720, y: 640, w: 440, t: 0.2, color: 'morado'}, {k: 'tarjeta', texto: 'ENERO 2022', sub: 'en vigor', x: 720, y: 900, w: 440, t: 0.5}]},
      {titulo: '1 · La <a>norma</a>', voz: 'Desde entonces, cada tinta que se usa en Europa tiene que cumplir esos límites.', items: [{k: 'icono', i: 'botella', x: 360, y: 780, s: 300}, {k: 'icono', i: 'ok', x: 740, y: 760, s: 240, t: 0.5}]},
      {titulo: '2 · Los <a>colores</a>', voz: 'En enero de 2023 cayeron dos pigmentos muy usados: un azul y un verde.', items: [{k: 'tarjeta', texto: 'ENERO 2023', x: 540, y: 560, w: 520}, {k: 'icono', i: 'azul', x: 380, y: 860, s: 240, t: 0.4}, {k: 'icono', i: 'verde', x: 700, y: 860, s: 240, t: 0.5}, {k: 'sello', texto: 'PROHIBIDOS', x: 540, y: 1120, t: 0.7, color: 'rojo'}]},
      {titulo: '2 · Los <a>colores</a>', voz: 'Estaban en muchísimos tonos, así que los fabricantes tuvieron que cambiar sus fórmulas.', items: [{k: 'icono', i: 'botella', x: 260, y: 800, s: 220}, {k: 'icono', i: 'botella', x: 540, y: 800, s: 220, t: 0.15}, {k: 'icono', i: 'botella', x: 820, y: 800, s: 220, t: 0.3}, {k: 'sello', texto: 'NUEVA FÓRMULA', x: 540, y: 1060, t: 0.6, color: 'morado'}]},
      {titulo: '2 · Los <a>colores</a>', voz: '¿Por qué? Por dudas sobre su seguridad a largo plazo.', items: [{k: 'icono', i: 'lupa', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: '¿SEGURO?', x: 760, y: 760, w: 380, t: 0.4}]},
      {titulo: '3 · <a>Tú</a>', voz: '¿Te puedes seguir tatuando en color? Sí, con tintas que cumplen la norma.', items: [{k: 'icono', i: 'tatuaje', x: 380, y: 800, s: 320}, {k: 'icono', i: 'ok', x: 760, y: 780, s: 240, t: 0.5}]},
      {titulo: '3 · <a>Tú</a>', voz: 'Por eso, pregunta siempre qué tintas usa tu estudio.', items: [{k: 'icono', i: 'dm', x: 380, y: 780, s: 300}, {k: 'tarjeta', texto: '¿Qué tintas usáis?', x: 720, y: 760, w: 520, t: 0.3, color: 'morado'}]},
      {titulo: 'Los dos <a>lados</a>', voz: 'Unos dicen que protege tu salud. Muchos tatuadores, que se perdieron colores.', items: [{k: 'icono', i: 'balanza', x: 540, y: 640, s: 260}, {k: 'tarjeta', texto: 'Protege tu salud', x: 290, y: 1000, w: 440, t: 0.15}, {k: 'tarjeta', texto: 'Se pierden colores', x: 790, y: 1000, w: 440, t: 0.55}]},
      {titulo: 'En <a>1 minuto</a>:', voz: 'Tatuarse en color sigue siendo posible. Con tinta que cumple.', items: [{k: 'icono', i: 'tatuaje', x: 300, y: 800, s: 260}, {k: 'icono', i: 'botella', x: 560, y: 800, s: 240, t: 0.3}, {k: 'icono', i: 'ok', x: 820, y: 800, s: 220, t: 0.6}]},
      SIGUENOS,
    ],
  },
  {
    id: 'ep02_precio', tema: '¿Por qué un tatuaje cuesta lo que cuesta?', fuentes: ['Explicación general del oficio, sin cifras (regla del estudio).'],
    escenas: [
      {titulo: '¿Por qué un tatuaje <a>cuesta</a> lo que cuesta?', voz: '¿Por qué un tatuaje cuesta lo que cuesta? Te lo explico en un minuto.', items: [{k: 'icono', i: 'tatuaje', x: 380, y: 800, s: 320}, {k: 'sello', texto: '¿?', x: 760, y: 760, t: 0.4, color: 'morado'}]},
      {titulo: '1 · Las <a>horas</a>', voz: 'Primero, las horas. Y no solo las de la camilla.', items: [{k: 'icono', i: 'reloj', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: 'SESIÓN', x: 760, y: 780, w: 360, t: 0.4}]},
      {titulo: '1 · Las <a>horas</a>', voz: 'Antes, el artista dibuja tu diseño. Eso también es trabajo.', items: [{k: 'icono', i: 'lapiz', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: '+ DISEÑO', x: 760, y: 780, w: 380, t: 0.4, color: 'morado'}]},
      {titulo: '2 · El <a>material</a>', voz: 'Segundo, el material. Agujas, guantes, film y protecciones: todo de un solo uso.', items: [{k: 'icono', i: 'aguja', x: 300, y: 760, s: 260}, {k: 'icono', i: 'guantes', x: 620, y: 760, s: 260, t: 0.3}, {k: 'sello', texto: '1 SOLO USO', x: 540, y: 1070, t: 0.65, color: 'morado'}]},
      {titulo: '2 · El <a>material</a>', voz: 'Se abre nuevo para ti y se tira al acabar.', items: [{k: 'icono', i: 'guantes', x: 340, y: 800, s: 260}, {k: 'icono', i: 'basura', x: 740, y: 800, s: 260, t: 0.45}]},
      {titulo: '3 · La <a>experiencia</a>', voz: 'Tercero, la experiencia. Años de práctica para que salga bien a la primera.', items: [{k: 'icono', i: 'estrella', x: 380, y: 800, s: 300}, {k: 'numero', n: 'AÑOS', sub: 'de práctica', x: 760, y: 800, t: 0.45}]},
      {titulo: '3 · La <a>experiencia</a>', voz: 'Porque un tatuaje no tiene control Z.', items: [{k: 'icono', i: 'deshacer', x: 540, y: 800, s: 360}]},
      {titulo: '4 · Zona y <a>tamaño</a>', voz: 'Y cuarto: no cuesta lo mismo una muñeca que una espalda entera.', items: [{k: 'icono', i: 'regla', x: 540, y: 620, s: 300}, {k: 'tarjeta', texto: 'MUÑECA', x: 300, y: 980, w: 380, t: 0.3}, {k: 'tarjeta', texto: 'ESPALDA', x: 780, y: 980, w: 380, t: 0.6, color: 'morado'}]},
      {titulo: 'Los dos <a>lados</a>', voz: 'Lo barato puede salir bien. O salir caro después, tapando o borrando.', items: [{k: 'icono', i: 'balanza', x: 540, y: 640, s: 260}, {k: 'tarjeta', texto: 'Sale bien', x: 290, y: 1000, w: 420, t: 0.15}, {k: 'tarjeta', texto: 'Tapar o borrar', x: 790, y: 1000, w: 420, t: 0.5}]},
      {titulo: 'En <a>1 minuto</a>:', voz: 'El precio es tiempo, seguridad y oficio.', items: [{k: 'icono', i: 'reloj', x: 280, y: 800, s: 230}, {k: 'icono', i: 'guantes', x: 540, y: 800, s: 230, t: 0.3}, {k: 'icono', i: 'estrella', x: 800, y: 800, s: 230, t: 0.6}]},
      {titulo: 'Pide <a>presupuesto</a>', voz: 'Pídenos presupuesto por DM con tu idea, la zona y el tamaño.', items: [{k: 'icono', i: 'dm', x: 540, y: 700, s: 300}, {k: 'tarjeta', texto: 'Idea · Zona · Tamaño', x: 540, y: 1020, w: 720, t: 0.4, color: 'morado'}]},
      SIGUENOS,
    ],
  },
  {
    id: 'ep03_cuidados', tema: 'Las 4 primeras semanas de tu tatuaje', fuentes: ['Pautas generales de cicatrización; REVISAR con el equipo antes de publicar (cada estudio da sus indicaciones).'],
    escenas: [
      {titulo: 'Las 4 primeras <a>semanas</a>', voz: 'Te acabas de tatuar. Esto es lo que pasa en las próximas cuatro semanas.', items: [{k: 'icono', i: 'calendario', x: 380, y: 800, s: 300}, {k: 'icono', i: 'tatuaje', x: 740, y: 800, s: 280, t: 0.4}]},
      {titulo: '<a>Días</a> 1 a 3', voz: 'Del día uno al tres está rojo, hinchado y suelta algo de plasma. Es normal.', items: [{k: 'icono', i: 'piel', x: 360, y: 780, s: 300}, {k: 'icono', i: 'gota', x: 720, y: 720, s: 200, t: 0.4}, {k: 'sello', texto: 'NORMAL', x: 720, y: 980, t: 0.75, color: 'verde'}]},
      {titulo: '<a>Días</a> 1 a 3', voz: 'Lávalo con agua y jabón suave, y sécalo a toquecitos.', items: [{k: 'icono', i: 'jabon', x: 380, y: 800, s: 280}, {k: 'icono', i: 'gota', x: 740, y: 800, s: 240, t: 0.35}]},
      {titulo: '<a>Días</a> 4 a 7', voz: 'Del cuatro al siete empieza a pelarse. Y pica. Mucho.', items: [{k: 'icono', i: 'piel', x: 380, y: 800, s: 300}, {k: 'sello', texto: 'PICA', x: 760, y: 780, t: 0.55, color: 'rojo'}]},
      {titulo: '<a>Días</a> 4 a 7', voz: 'Regla de oro: no se rasca. Ni un poquito.', items: [{k: 'icono', i: 'rascar', x: 540, y: 800, s: 360}]},
      {titulo: 'Semana <a>2</a>', voz: 'La segunda semana se pela como una quemadura de sol.', items: [{k: 'icono', i: 'sol', x: 380, y: 800, s: 300}, {k: 'icono', i: 'piel', x: 760, y: 800, s: 260, t: 0.4}]},
      {titulo: 'Semana <a>2</a>', voz: 'Crema, pero una capa fina. Nada de embadurnarlo.', items: [{k: 'icono', i: 'crema', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: 'CAPA FINA', x: 760, y: 780, w: 380, t: 0.4, color: 'morado'}]},
      {titulo: 'Semanas <a>3 y 4</a>', voz: 'La tercera y la cuarta se ve apagado, como lechoso. Tranquilo, es piel nueva.', items: [{k: 'icono', i: 'piel', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: 'PIEL NUEVA', x: 760, y: 780, w: 400, t: 0.6}]},
      {titulo: 'Mientras <a>tanto</a>', voz: 'Todo el mes: nada de piscina, mar ni sol directo.', items: [{k: 'icono', i: 'olas', x: 320, y: 760, s: 260}, {k: 'icono', i: 'sol', x: 720, y: 760, s: 240, t: 0.3}, {k: 'sello', texto: 'NO', x: 540, y: 1060, t: 0.6, color: 'rojo'}]},
      {titulo: 'En <a>1 minuto</a>:', voz: 'En un mes parece curado, pero la piel de debajo sigue trabajando.', items: [{k: 'icono', i: 'calendario', x: 380, y: 800, s: 280}, {k: 'icono', i: 'piel', x: 740, y: 800, s: 280, t: 0.4}]},
      {titulo: '<a>Ojo</a>', voz: 'Cada piel es un mundo: sigue siempre lo que te diga tu tatuador.', items: [{k: 'icono', i: 'dm', x: 540, y: 700, s: 300}, {k: 'tarjeta', texto: 'Pregunta a tu tatuador', x: 540, y: 1020, w: 720, t: 0.4, color: 'morado'}]},
      SIGUENOS,
    ],
  },
  {
    id: 'ep04_menores', tema: '¿Tatuarse siendo menor en Cataluña?',
    fuentes: ['Decret 90/2008, de 22 d\'abril (Generalitat de Catalunya), art. 6.2: consentimiento informado por escrito del menor con madurez suficiente, acreditada por escrito del padre, la madre o el tutor/a (DOGC 5118).', 'Diputació de Barcelona, hoja para usuarios: menores de 16, autorización de progenitores/tutores y fotocopias de los DNI.'],
    escenas: [
      {titulo: '¿Tatuarse siendo <a>menor</a>?', voz: '¿Te puedes tatuar siendo menor en Cataluña? Te lo cuento en un minuto.', items: [{k: 'icono', i: 'dni', x: 380, y: 800, s: 300}, {k: 'sello', texto: '-18', x: 760, y: 780, t: 0.4, color: 'morado'}]},
      {titulo: '1 · La <a>norma</a>', voz: 'Lo regula un decreto de la Generalitat de 2008.', items: [{k: 'icono', i: 'libro', x: 360, y: 800, s: 300}, {k: 'tarjeta', texto: 'DECRETO 90/2008', sub: 'Generalitat de Catalunya', x: 740, y: 780, w: 500, t: 0.35, color: 'morado'}]},
      {titulo: '1 · La <a>norma</a>', voz: 'Dice que el menor con madurez suficiente da su consentimiento, en persona y por escrito.', items: [{k: 'icono', i: 'firma', x: 380, y: 800, s: 300}, {k: 'tarjeta', texto: 'POR ESCRITO', x: 760, y: 780, w: 420, t: 0.5}]},
      {titulo: '2 · Tus <a>padres</a>', voz: 'Y esa madurez la tiene que acreditar por escrito tu padre, tu madre o tu tutor.', items: [{k: 'icono', i: 'padres', x: 360, y: 800, s: 300}, {k: 'icono', i: 'firma', x: 740, y: 800, s: 260, t: 0.45}]},
      {titulo: '2 · <a>Menos de 16</a>', voz: 'Con menos de dieciséis, te pedirán además fotocopia de tu DNI y del de quien firma.', items: [{k: 'sello', texto: '-16', x: 300, y: 760, color: 'morado'}, {k: 'icono', i: 'dni', x: 620, y: 780, s: 260, t: 0.35}, {k: 'icono', i: 'dni', x: 850, y: 820, s: 200, t: 0.5}]},
      {titulo: '3 · El <a>estudio</a>', voz: 'Y aun cumpliendo todo, cada estudio puede decidir si tatúa a menores o no.', items: [{k: 'icono', i: 'balanza', x: 540, y: 780, s: 300}]},
      {titulo: 'Los dos <a>lados</a>', voz: 'Unos dicen que con dieciséis ya decides tú. Otros, que mejor esperar.', items: [{k: 'icono', i: 'balanza', x: 540, y: 640, s: 260}, {k: 'tarjeta', texto: 'Ya decides tú', x: 290, y: 1000, w: 420, t: 0.15}, {k: 'tarjeta', texto: 'Mejor esperar', x: 790, y: 1000, w: 420, t: 0.5}]},
      {titulo: 'En <a>1 minuto</a>:', voz: 'Siendo menor, sí: con consentimiento por escrito y la firma de tus padres.', items: [{k: 'icono', i: 'firma', x: 380, y: 800, s: 280}, {k: 'icono', i: 'padres', x: 740, y: 800, s: 280, t: 0.4}]},
      {titulo: '<a>Ojo</a>', voz: 'Esto es un resumen: antes de ir, pregunta al estudio qué te van a pedir.', items: [{k: 'icono', i: 'dm', x: 540, y: 780, s: 320}]},
      SIGUENOS,
    ],
  },
  {
    id: 'ep05_laser', tema: 'Lo que nadie te cuenta del láser',
    fuentes: ['AAD (aad.org): puede doler, se puede usar anestesia tópica; un solo láser no quita todos los colores.', 'Skinsight (cita a la AAD): negro, azul oscuro y verde oscuro, los más fáciles; amarillo, blanco, naranja y rojo, los más difíciles; dolor comparado con gomas elásticas.', 'Varias clínicas: 6-12 sesiones habituales, al menos 6 semanas entre sesiones (rango orientativo).'],
    escenas: [
      {titulo: 'Lo que nadie te cuenta del <a>láser</a>', voz: 'Lo que nadie te cuenta del láser para borrar tatuajes.', items: [{k: 'icono', i: 'laser', x: 380, y: 760, s: 300}, {k: 'icono', i: 'tatuaje', x: 740, y: 820, s: 280, t: 0.35}]},
      {titulo: '1 · Las <a>sesiones</a>', voz: 'No se borra en una sesión. Lo normal es entre seis y doce.', items: [{k: 'numero', n: '6-12', sub: 'sesiones', x: 540, y: 800}]},
      {titulo: '2 · La <a>paciencia</a>', voz: 'Entre una sesión y otra, mínimo seis semanas.', items: [{k: 'icono', i: 'calendario', x: 360, y: 800, s: 300}, {k: 'numero', n: '6+', sub: 'semanas', x: 760, y: 800, t: 0.35}]},
      {titulo: '2 · La <a>paciencia</a>', voz: 'El láser rompe la tinta en trocitos, y tu cuerpo se los va llevando poco a poco.', items: [{k: 'icono', i: 'laser', x: 360, y: 760, s: 280}, {k: 'icono', i: 'piel', x: 740, y: 820, s: 280, t: 0.4}]},
      {titulo: '3 · Los <a>colores</a>', voz: 'El negro y los tonos oscuros son los que mejor salen.', items: [{k: 'icono', i: 'negro', x: 380, y: 800, s: 260}, {k: 'icono', i: 'ok', x: 740, y: 800, s: 240, t: 0.45}]},
      {titulo: '3 · Los <a>colores</a>', voz: 'Los claros, como el amarillo o el rojo, cuestan bastante más.', items: [{k: 'icono', i: 'amarillo', x: 340, y: 780, s: 240}, {k: 'icono', i: 'rojo', x: 620, y: 780, s: 240, t: 0.25}, {k: 'sello', texto: 'DIFÍCIL', x: 540, y: 1060, t: 0.6, color: 'rojo'}]},
      {titulo: '4 · ¿<a>Duele</a>?', voz: '¿Duele? Mucha gente lo compara con gomazos de una goma elástica.', items: [{k: 'icono', i: 'goma', x: 380, y: 800, s: 300}, {k: 'icono', i: 'rayo', x: 760, y: 780, s: 260, t: 0.45}]},
      {titulo: 'Los dos <a>lados</a>', voz: 'Hay quien lo borra del todo, y quien solo lo aclara para taparlo con otro.', items: [{k: 'icono', i: 'balanza', x: 540, y: 640, s: 260}, {k: 'tarjeta', texto: 'Borrar del todo', x: 290, y: 1000, w: 420, t: 0.15}, {k: 'tarjeta', texto: 'Aclarar y tapar', x: 790, y: 1000, w: 420, t: 0.5}]},
      {titulo: 'En <a>1 minuto</a>:', voz: 'Láser es paciencia, varias sesiones y un profesional.', items: [{k: 'icono', i: 'calendario', x: 280, y: 800, s: 230}, {k: 'icono', i: 'laser', x: 540, y: 800, s: 230, t: 0.3}, {k: 'icono', i: 'estrella', x: 800, y: 800, s: 230, t: 0.6}]},
      {titulo: '<a>Pregúntanos</a>', voz: '¿Quieres saber cuántas sesiones necesitaría el tuyo? Escríbenos.', items: [{k: 'icono', i: 'dm', x: 540, y: 780, s: 320}]},
      SIGUENOS,
    ],
  },
];
