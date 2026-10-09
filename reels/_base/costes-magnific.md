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
