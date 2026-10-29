# estilo.md · Guía de edición de PHARAON

Referencia: vídeo de Uri «Me llevó 5 años…» (TikTok @uri.cr_tattoo, 76,9 s, 576×1024 a 30 fps, descargado con marca de agua).
Análisis del 29/10/2026: fotogramas a 2 por segundo (154), detección de cambios de plano (umbral 0,22 → 48 detecciones) y audio a 16 kHz.
Todo se escala a nuestro formato: **1080×1920 a 30 fps** (factor 1,875 sobre la referencia).
Lo que no se puede medir con seguridad va marcado con **[SUPOSICIÓN]**.

---

## 1. Ritmo de cortes

| Dato | Valor medido |
|---|---|
| Planos distintos | 28 en 73,5 s de contenido (sin la cortinilla final de TikTok) |
| Duración media de plano | **2,6 s** |
| Bloque de «proceso» (20,4–34 s) | un corte cada **1,0–1,9 s** (media 1,3 s) |
| Bloques de «hablar a cámara» | planos de hasta 11,4 s, pero partidos con **jump cuts y punch-in cada 2–4 s** |
| Punch-in | se alterna plano normal ↔ **zoom 1,12–1,18×** sobre la cara, sin transición (corte seco) |
| Hook | primer plano a los **0,0 s**; el primer cambio, a los **1,87 s** |
| Silencios | no hay pausas audibles: los cortes eliminan los silencios [SUPOSICIÓN: umbral ≈ 0,2–0,3 s] |

Para nuestro vídeo: **ningún plano dura más de 3 s sin un corte o un punch-in**.

## 2. Subtítulos

| Dato | Valor |
|---|---|
| Palabras por bloque | **1** (una palabra cada vez, siempre) |
| Fuente | sans geométrica, negrita pesada, minúsculas → usamos **Inter ExtraBold (800)** [SUPOSICIÓN: el original parece Montserrat/TikTok Sans Bold] |
| Tamaño | palabra de 5 letras ≈ 21 % del ancho → **≈ 92 px** de cuerpo a 1080 de ancho |
| Color | **#FFFFFF** |
| Contorno y sombra | brillo exterior blanco (desenfoque ≈ 10 px, opacidad ≈ 45 %) + sombra oscura suave (desenfoque 6 px, 0/+4 px, negro al 60 %) |
| Posición | centrada en horizontal; **centro vertical al 58 % de la altura (y ≈ 1114 px)** (corrección del usuario, 29/10: «un pelín más abajo» que el 51 % de la referencia); varía ±6 % para no tapar la cara o las manos |
| Mayúsculas | todo en **minúsculas**, como se dice; sin puntuación |
| Animación | **ninguna**: entra y sale en seco con la palabra (medido fotograma a fotograma en 20,25–20,6 s) |
| Duración | desde que empieza la palabra hasta que empieza la siguiente; sin huecos en blanco si la pausa < 0,35 s |
| Palabra destacada | números y cifras clave: **cian #22E1EE**, **≈ 2,2×** el tamaño normal (≈ 200 px), con brillo cian; los da el contenido («3», «4», «4 PASOS») |

En los vídeos de PHARAON (corrección del usuario, 28/10): el color de acento es **naranja Halloween #FF8A1F** en lugar del cian **cuando el vídeo es de Halloween**, y solo en las palabras clave (marca, nombre del evento, cifras), no en palabras normales.

## 3. Textos en pantalla (aparte de los subtítulos)

| Tipo | Valores |
|---|---|
| Rótulo de entrada (0,1–1,8 s) | 2 líneas centradas al 45–55 % de altura: línea 1 en **serif cursiva cian** (≈ 150 px), escrita letra a letra (≈ 2 letras por fotograma, «máquina de escribir»); línea 2 en **condensada en mayúsculas blanca** (Anton, ≈ 190 px) |
| Rótulo de capítulo | «4 PASOS»: mayúsculas, cian con brillo, ≈ 120 px, 1,3 s |
| Números de lista | «2», «3», «4»: cian, ≈ 260 px, sustituyen al subtítulo durante ≈ 0,8 s |
| Texto meme | «aaah shit…», «here we go again.»: **amarillo #F5F000**, minúsculas, ≈ 60 px, sans regular-bold, centrado; solo en momentos de humor, ≈ 1,0–1,5 s |
| Gráficos | 1 vez: rótulo «FORMACIÓN» con iconos en blanco (≈ 57 s) y 1 vez un pantallazo de comentarios (≈ 63 s) |

## 4. B-roll

- Planos de detalle del proceso (manos, botellas, caps) intercalados con el plano a cámara: **≈ 40 % del tiempo**.
- Un plano de un tatuaje terminado en el minuto 1,87 s (brazo entero) como gancho visual.
- Planos generales del estudio (techo de hexágonos) para resetear.

## 5. Transiciones

| Tipo | Valores |
|---|---|
| Corte seco | la mayoría (≈ 75 %) |
| **Destello de luz (light leak)** | 7 veces: 4,8 / 8,5 / 13,9 / 35,15 / 51,33 / 57,7 / 64,7 s. Duración **5–6 fotogramas (0,17–0,2 s)**: naranja-rojo → blanco → naranja. Pico de blanco en el fotograma central |
| Desenfoque blanco de entrada | 0–0,23 s: arranca en negro, sube a blanco desenfocado y aparece el rótulo |
| Frecuencia | un destello cada **≈ 9 s** de media, siempre en un cambio de tema |

## 6. Zooms

- Punch-in seco 1,12–1,18× en los planos largos a cámara (ver Ritmo).
- No hay zoom continuo (Ken Burns) en los planos de vídeo [SUPOSICIÓN: no se aprecia en los fotogramas a 2 fps].

## 7. Color

| Tramo | Tratamiento |
|---|---|
| Base | color natural, ligeramente desaturado y frío (−15 % de saturación) [SUPOSICIÓN] |
| Bloque de proceso (20,4–34 s) y planos sueltos (1,87 s; 39,8 s) | **blanco y negro** con contraste alto |
| Tras cada destello | **tinte cálido naranja-rojo** sobre el plano (degradado #FF5A1F→#FFB347, opacidad 35–55 %) durante **2–5 s**, y luego vuelve al color base |

## 8. Sonido

| Dato | Valor medido |
|---|---|
| Voz | protagonista; mediana −40 dBFS en el archivo descargado (normalizado por TikTok) |
| Música | no se detecta música de fondo continua: en los silencios el nivel cae a −60 dBFS [SUPOSICIÓN: sin música o muy baja] |
| Efectos | **en cada destello hay un pico de +15 a +19 dB** sobre la voz → whoosh o impacto de transición |
| Meme de audio | [SUPOSICIÓN] en «here we go again.» suena el audio del meme (GTA San Andreas); no lo usamos (regla: nada de audio de terceros) |
| Mezcla final | voz a −14 LUFS integrados, picos −1,5 dBTP; efectos 6–10 dB por debajo de la voz salvo en los golpes |

---

## Reglas añadidas por el usuario (se van sumando)

- 28/10 · Subtítulos sincronizados de verdad: tiempos por palabra de un transcriptor (Whisper o ElevenLabs Scribe), nunca estimados.
- 28/10 · Naranja solo en las palabras clave (marca, evento, cifras).
- 29/10 · Subtítulos un poco más abajo: centro al **58 %** de la altura (antes 51 %).
- Reglas de PHARAON que siempre aplican: sin audio de terceros, sin cámara lenta, solo sale gente del equipo (clientes solo de fondo y sin cara).
