---
description: Ejecuta el flujo completo de PHARAON CONTENT STUDIO para preparar los vídeos de una semana.
argument-hint: [notas opcionales: artistas disponibles, fechas, eventos, restricciones]
---

Actúa como **Director Creativo** de PHARAON CONTENT STUDIO siguiendo `CLAUDE.md` y prepara el contenido de esta semana (~3 vídeos para Reels y TikTok).

Notas del usuario para esta semana: $ARGUMENTS

Pasos:

1. Lee `estudio/pharaon.md`, las fichas de `estudio/artistas/`, `formatos/series.md` y las 2-3 entregas más recientes de `entregas/` para no repetir ideas y dar continuidad a las series.
2. **INVESTIGAR** — lanza el agente `trend-hunter`, pasándole la fecha de hoy, las series activas y las notas del usuario.
3. **GENERAR** — lanza el agente `creative` con el informe completo del trend-hunter, las series activas, las ideas ya usadas y las notas del usuario. Mínimo 20 conceptos.
4. **FILTRAR** — lanza el agente `critic` con TODOS los conceptos, sin indicar preferencias.
5. **SELECCIONAR** — elige solo las ideas con verdadero potencial (normalmente 3; pueden ser menos si no hay nivel, y alguna de reserva si sobra calidad). Justifica cada elección y cualquier discrepancia con el critic. Aplica el FILTRO FINAL de `CLAUDE.md`.
6. **DESARROLLAR** — lanza el agente `script-writer` solo con los conceptos seleccionados (incluyendo las mejoras del critic que aceptes).
7. **ENTREGAR** — guarda la entrega completa en `entregas/AAAA-Www.md` (semana ISO) con: resumen ejecutivo, guiones, ideas de reserva, descartes destacados con motivo, y tendencias clave. Actualiza `formatos/series.md` si procede. Presenta al usuario un resumen breve y accionable.

Nunca rellenes para llegar a una cantidad.
