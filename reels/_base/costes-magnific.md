# Costes de Magnific (plan Premium, 20.000 créditos/mes)

Precios exactos consultados con la herramienta de simulación de Magnific el 07/10/2026. Consultar no gasta créditos.

**Regla del usuario:** no gastar créditos sin su confirmación previa.

## Precio por pieza

| Pieza | Créditos |
|---|---|
| Imagen fotorrealista (modo auto; el precio puede variar) | ~100 |
| Voz en off de un reel (ElevenLabs v3, unos 470 caracteres) | 88 |
| Música de 30 s (Google Lyria 3) | 80 |
| Clip de vídeo de 5 s · Kling 2.5 a 720p | 140 |
| Clip de vídeo de 5 s · MiniMax H3 Max Turbo a 768p | 200 |
| Clip de vídeo de 5 s · Kling 2.5 a 1080p | 325 |
| Clip de vídeo de 5 s · Seedance 2.0 Fast a 720p | 1.175 |
| Clip de vídeo de 5 s · Seedance 2.5 a 720p | 2.200 |
| Clip de vídeo de 5 s · Seedance 2.5 a 1080p | 3.950 |

## Coste por reel (9 escenas)

Las tres opciones incluyen las 9 imágenes, la voz y la música, que suman unos 1.070 créditos.

| Formato | Créditos por reel | Reels al mes |
|---|---|---|
| A · Imágenes con movimiento de cámara | ~1.070 | ~18 |
| B · A + hook y final animados con Kling 2.5 1080p (2 clips) | ~1.720 | ~11 |
| B+ · A + 3 escenas animadas con Kling 2.5 1080p | ~2.050 | ~9 |
| C · Las 9 escenas animadas con Kling 2.5 1080p | ~4.000 | ~5 |
| C barato · Las 9 escenas animadas con Kling 2.5 720p | ~2.330 | ~8 |

Hay que dejar un margen de un 10-15 % para repetir imágenes o clips que salgan mal.

## Gasto real

- **07/10/2026:** 3 reels en formato B (2 clips de Kling 2.5 a 1080p por reel), con 18 imágenes, 3 voces y 3 músicas. Total: 3.826 créditos, unos 1.275 por reel. En la práctica las imágenes han costado 75 créditos cada una. Quedan 16.174.
- **07/10/2026, cambio de voz:**
  - Pruebas de voz: 7 pruebas cortas, unos 95 créditos.
  - Voces nuevas de Fernando Ruiz (ElevenLabs turbo v2.5, el motor B): 143 créditos.
  - Montaje: 0 créditos. Las pausas se recortan con `reels/_base/ajustar_voz.py`; la voz casi no se acelera (como mucho un 6 %).
  - Voz por defecto a partir de ahora: Fernando Ruiz, turbo v2.5, estabilidad 0,45, velocidad 1,1. Cuesta unos 48 créditos por reel.
- **07/10/2026, «La Catrina tenía otro nombre» y «5 errores de un diseño hecho con IA»:**
  - Sin clips de Kling. Las imágenes fijas se animan con zoom y recortes, y se usan fotos reales y la toma del logo.
  - Gasto: imágenes IA, 3 voces (una repetida para quitar "seis dedos") y 2 músicas.
  - Total: 917 créditos, unos 460 por reel. Quedan 15.019.
- **09/10/2026, montaje dinámico de los 3 primeros reels (opción B):**
  - 12 imágenes nuevas, 4 por reel, a 75 créditos cada una: 900 créditos.
  - Se quitan los subtítulos y ningún plano dura más de unos 2 s.
  - El troceado (`reels/_base/trocear.py`) no cuesta créditos.
  - Quedan unos 14.119 créditos.
- **09/10/2026, «Martes 13»:**
  - 8 imágenes (600), 1 clip de Kling 2.5 a 1080p (325), voz (41) y música (80): 1.046 créditos.
  - Dos intentos de imagen fallaron por un 403 del servidor. Parece que no se cobraron; comprobar en el saldo.
- **10/10/2026, transición «granada» (reel del primer año):**
  - 1 clip de Kling 2.5 a 1080p con fotograma inicial (local en obras) y final (local hoy): 325 créditos.
  - La foto en obras la hizo el usuario.
- **10/10/2026, segundo clip de la granada** (la granada rueda y explota con fuego): 325 créditos. Quedan 12.423.
- **13/10/2026, transición «calabaza» (Halloween):** 1 clip de Kling 2.5 a 1080p desde la foto actual del estudio: 325 créditos. Quedan unos 12.098.
- **13/10/2026, calabaza v2:**
  - Clip de 10 s de Kling 2.5 a 1080p (la calabaza rueda, se para brillando y explota): 650 créditos.
  - El usuario autorizó gastar para que la espera fuera fluida.
  - Quedan unos 11.448.
- **13/10/2026, librería de efectos de sonido (`reels/_base/sfx/`):**
  - Efectos: impacto (3 s), gato, cristal, máquina de tatuar (2 s cada uno) y whoosh (1 s).
  - Coste: 50 créditos. Se reutilizan gratis en otros vídeos.
  - Primer uso: Martes 13.
- **16/10/2026, «Calabaza gigante»** (cebo «¿qué pasaría si…?» para anunciar la Halloween Costume Week):
  - Gasto: 6 imágenes (450), 3 clips de Kling 2.5 a 1080p (975), voz (47) y música (80). Total: 1.552 créditos.
  - Se reutilizan gratis los efectos de la librería, el clip de la calabaza en el estudio y la música de Martes 13.
- **16/10/2026, storyboard «Globo»** (cebo neutro para la Halloween Week): 4 imágenes, 300 créditos. A partir de aquí, nada se anima sin el OK del usuario.
| 2026-10-17 | Conejo · storyboard | images_generate x1 | 75 |
| 2026-10-18 | Sitcom EP01 · imagen A Adri recepción | images_generate x1 | 75 |
| 2026-10-18 | Sitcom EP01 · imagen A v2 (logo real, ideogram preciseEdit) | images_generate x1 | 80 |
| 2026-10-18 | Sitcom EP01 · lip-sync Adri (OmniHuman, 5 s) | video_speak | 900 |
| 2026-10-18 | Sitcom EP01 · imágenes B-F | images_generate x5 | 375 |
| 2026-10-18 | Sitcom EP01 · lip-sync Meii/Andrea/Uri | video_speak x3 | 1080 |
| 2026-10-18 | Sitcom EP01 · clips grupo + Kike (Kling 720p) | video_generate x2 | 280 |
| 2026-10-18 | Sitcom EP02 · voces guía TTS x3 | audio_tts | 9 |
| 2026-10-18 | Sitcom EP02 · imágenes N1-N5 | images_generate x5 | 375 |
| 2026-10-18 | SFX scratch x2, ballena, desenchufe, bip | audio_sfx_generate | 50 |
| 2026-10-18 | Sitcom EP02 · lip-sync Andrea (180) + Uri (360) + Adri (360) | video_speak x3 | 900 |
| 2026-10-18 | Sitcom EP02 · clips duelo, sufrimiento, Carlos (Kling 720p) | video_generate x3 | 420 |
| 2026-10-18 | Sitcom EP01 · voces IA (5 TTS) | audio_tts | 25 |
| 2026-10-18 | Sitcom EP01 · voces IA sueltas (5 TTS) | audio_tts | 6 |
| 2026-10-19 | Sitcom EP03 Halloween · voces TTS x2 | audio_tts | 5 |
| 2026-10-19 | Sitcom EP03 · imágenes x4 | images_generate | 300 |
| 2026-10-19 | Sitcom EP03 · cara de Uri en la calabaza (preciseEdit) | images_generate | 80 |
| 2026-10-19 | Sitcom EP03 · lip-sync Adri + Uri | video_speak x2 | 720 |
| 2026-10-19 | Sitcom EP03 · clips grupo, calabaza, Carlos (Kling 720p) | video_generate x3 | 420 |
| 2026-10-19 | SFX trueno | audio_sfx_generate | 10 |
| 2026-10-19 | Sitcom EP03 · quitar septum a Uri (preciseEdit) | images_generate | 80 |
| 2026-10-19 | Sitcom EP03 · clip calabaza rehecho sin septum | video_generate | 140 |
| 2026-10-20 | Casting de voces (15 TTS: eleven_v3 + Gemini) | audio_tts | 118 |
| 2026-10-20 | Voces v2 (todas las B): 12 OK + 2 combinadas (6 fallidas de Gemini) | audio_tts | ~112 |
| 2026-10-20 | Casting Adri (4 TTS) | audio_tts | 48 |
| 2026-10-21 | Post Halloween · fondo calabazas con flash de tatuaje x2 | images_generate | 120 |
| 2026-10-23 | Reel1 · clip de prueba imagen 07 (Kling 720p) | video_generate | 140 |
