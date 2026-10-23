# PHARAON SITCOM (mini historias animadas con diálogo) · semilla 18/10/2026

Referencia de formato: mini sitcom animada con labios sincronizados (estilo @irrae.lucky). Solo como referencia de formato; no se reutiliza nada de ese vídeo.

## Reparto (dibujos hechos por el usuario, alfombra roja)

| Dibujo | Persona | Rol | Ficha |
|---|---|---|---|
| personajes/uri.png | Uri | Tatuador y dueño de PHARAON | estudio/artistas/uri-cr.md |
| personajes/meii.png | Meii | Tatuadora | estudio/artistas/meii.md |
| personajes/kike-siz0.png | Kike (Siz0) | Tatuador | estudio/artistas/siz0.md |
| personajes/andrea-avilas.png | Andrea (Avilas) | Tatuadora | estudio/artistas/avilas.md |
| personajes/adri.png | Adri | Manager y recepcionista | (sin ficha de artista) |
| personajes/carlos.png | Carlos Moreno | Tatuador | estudio/artistas/carlos-moreno.md |

Delia ya no forma parte del estudio (18/10/2026).

## Reglas
- Personalidades, manías y anécdotas: solo las que dé el usuario. Nada deducido de los dibujos.
- Voces: preferible la voz real de cada uno (audio del móvil) con sincronizado de labios; voz IA solo si lo pide el usuario.
- Todo en dibujos: sin planos reales de nadie del equipo (usuario, 18/10/2026).
- Proceso: guion (0 cr) → prueba de 1 escena con coste exacto → episodio completo. OK del usuario en cada paso.

## Estado
- PENDIENTE: situaciones reales del estudio para el episodio 1.

## Voces (usuario, 18/10/2026)
- Graban su voz: Uri, Meii, Kike, Andrea y Adri.
- Carlos: no graba (viene poco). Si sale, sin diálogo o con un papel mudo.

## Detalles físicos que hay que respetar en los prompts (usuario)
- Uri: dos aros en la nariz, uno en cada aleta. **No lleva septum** (19/10/2026).

## Voces definitivas (casting 20/10/2026, el usuario eligió todas las B)
- Adri: Puck (Google, gemini_v3_1_flash_tts, id 714) · opción C del casting de Adri (23/10). Antes: Emilio Salcedo (ElevenLabs, id 1280)
- Uri: Fenrir (Google, gemini_v3_1_flash_tts, id 706)
- Andrea: Leda (Google, id 711)
- Meii: Laomedeia (Google, id 710)
- Kike: Achird (Google, id 695)
Con Google, pedir siempre en `systemInstruction`: español de España, acento castellano peninsular, joven, natural, sin locutor. Las frases muy cortas a veces fallan («No audio content generated»): generarlas juntas en una toma y cortar.
Montaje con estas voces: `VOCES=v2 python3 reels/PHARAON_SITCOM/epXX/montar_epXX.py` (alineado en `voces_v2/alinear_v2.py`).
