# NOVATO vs PRO · EP01 · «PEDIR CITA POR DM»

**Tarea:** pedir cita en un estudio de tatuajes por mensaje directo.
**Por qué esta:** la entiende cualquiera (todos hemos escrito «hola» y esperado), el PRO enseña algo real y útil para el estudio (qué poner en el DM para que os contesten rápido) y el loop sale solo.
**Herramienta:** Remotion (`remotion/src/novatopro/`). Personajes vectoriales propios: idénticos en cada toma, 0 créditos.
**Formato:** 1080×1920, 30 fps, 20 s. NOVATO arriba, PRO abajo, franja negra en medio. Paleta: hueso #EFEBE4 · negro #111 · morado PHARAON #9925AE · blanco.

## Personajes
- **NOVATO:** cabeza redonda blanca, contorno negro grueso, ojos enormes, camiseta negra. Se mueve rápido (balanceo de ±6 px), suda, tiembla, salta.
- **PRO:** el mismo muñeco con **gafas** y párpados a media asta; camiseta morada. Apenas se mueve (balanceo de ±3 px). Nunca cambia de cara: está aburrido de lo fácil que le sale.

## Guion por tomas

| Seg. | NOVATO hace | PRO hace | NOVATO dice | PRO dice | Texto en pantalla | Sonido |
|---|---|---|---|---|---|---|
| 0–1 | Mira el móvil, nervioso | Mira el móvil, tranquilo | — | — | **PEDIR CITA POR DM** (rótulo que rebota en la franja) | whoosh |
| 1–2,3 | Duda con el móvil | Empieza a escribir | «Vale… ¿qué le pongo?» | «Un mensaje. Ya está.» | — | — |
| 2,2–5 | Manda «hola», «holaaa», «¿buenas?». Aparece **Visto**. Le cae una gota de sudor | Un solo mensaje que se rellena línea a línea con ✔: idea · zona · tamaño · fechas | «¿Me han dejado en visto?» | «Idea, zona, tamaño y fechas.» | burbujas de chat | bip ×4 |
| 5–8 | Manda «¿precio?» y el estudio responde «¿De qué tatuaje? 😅». Mira a cámara | Adjunta una foto de referencia (rosa) | «…buena pregunta.» | «Y una referencia. Siempre.» | — | bip, golpe en la respuesta |
| 8–11 | Manda un audio de **3:47** que se alarga en pantalla | Estira el brazo y marca la zona con un rectángulo de puntos | «Mejor te lo explico por audio…» | «Aquí. Diez centímetros. Fin.» | — | bip + whoosh del audio |
| 11–14 | Tiembla y manda «??» y «???» | Deja el móvil y bebe café | «¿Les escribo también por WhatsApp?» | «Contestan en horario. Café.» | — | bip ×2 |
| 14–17,7 | **Le contestan** «¿Te va el jueves a las 11? 💜». Salta de alegría | Le llega **el mismo mensaje** | «¡¡ME HA CONTESTADO!!» | «A los dos. Lo leen todo.» | — | golpe |
| 17,9–19,5 | Vuelve a dudar con el móvil | — | «Vale… ¿y ahora qué le pongo?» | — | — | — |
| 19,5–20 | Los chats se vacían | Los chats se vacían | — | — | vuelve **PEDIR CITA POR DM** → **loop** con el segundo 0 | whoosh |

**Giro:** los dos acaban igual (el estudio lee todo y contesta a los dos), y el NOVATO vuelve a la casilla de salida: el último fotograma es el primero.
**Lo que enseña el PRO, sin sermón:** en un DM van idea, zona, tamaño, fechas y una foto de referencia; se contesta en horario.

## «Prompts» de animación (Remotion)
En lugar de prompts de IA, cada toma se define en `remotion/src/novatopro/guion.ts`: cara del muñeco (`nervioso`, `mira`, `feliz`, `aburrido`…), brazo (`movil`, `medir`, `cafe`), sudor, temblor y salto, burbujas del chat con su fotograma y las líneas de diálogo. Para hacer otro episodio basta con un `guion.ts` nuevo.
Si algún día se quiere en IA (Kling): *«Flat 2D vector cartoon, vertical 9:16 split screen. Top: a simple round-headed white character with huge eyes and black t-shirt, nervously typing on a phone. Bottom: the same character design with black glasses and a purple t-shirt, calm and bored. Solid colors, thick clean black outlines, plain beige background, palette beige #EFEBE4, black, purple #9925AE.»* (más caro y los personajes cambian de una toma a otra).

## Dirección de voz
- **NOVATO:** chico de 20–25 años, español de España. Rápido, agudo, frases que suben al final, con titubeos («vale…»). En «¡¡ME HA CONTESTADO!!» grita de alegría y se le quiebra la voz.
- **PRO:** chico de 28–32 años, español de España. Grave, lento y plano, con pausas. Suena a quien lo ha hecho mil veces. Nunca sube el tono, ni siquiera en «A los dos. Lo leen todo.».
- **Música:** base lo-fi muy suave por debajo (−20 dB de la voz) o nada. Los golpes van con los bips de mensaje enviado y con el golpe de la respuesta del estudio.

## Texto del post
**Caption:** ¿Eres NOVATO o PRO pidiendo cita? 📲 Spoiler: te contestamos igual, pero así vas más rápido 😉
**Hashtags:** #tatuajes #novatovspro #humor #santfeliudellobregat #pharaonstudio
**Comentario fijado:** ¿Qué hacemos en el próximo NOVATO vs PRO? 👇 Escribe la tarea y la animamos.
