# Editor de vídeo con Remotion (PHARAON)

- Proyecto vertical 1080x1920 a 30 fps. Composiciones en `src/Root.tsx`.
- Render: `cd remotion && npx remotion render <Composición> out/<archivo>.mp4`.
- Chrome no se puede descargar en este entorno: `remotion.config.ts` usa el headless_shell preinstalado (`/opt/pw-browsers/chromium_headless_shell-1194/...`).
- Skills oficiales instaladas con `npx skills add remotion-dev/skills` en `.claude/skills/remotion-*`.
- Whisper (faster-whisper) está instalado, pero los modelos se descargan de huggingface.co, que la red del entorno bloquea.
  Alternativa probada: ElevenLabs Scribe (tiempos por palabra; ~470 créditos de ElevenLabs por 35 s).
- Los vídeos de trabajo (`public/*.mov|mp4`) y los renders (`out/`) no se suben.
