# Plantillas de carrusel · «LA HISTORIA DE…» y «TIPS DE…»

Un carrusel = un archivo `.json` con el contenido. El diseño lo pone `posts/_base/carrusel.py`:

    python3 posts/_base/carrusel.py posts/<carpeta>/<nombre>.json

Copiar `historia.json` o `tips.json` a la carpeta del carrusel, rellenar y generar. Las fotos de clientes van siempre en `privado/<carpeta>/`
(no se suben) y la carpeta de renders se añade a `.gitignore`. Ejemplo completo: `posts/catrina/catrina.json`.

## Qué hace falta para cada uno

**LA HISTORIA DE… (mito, símbolo o historia detrás de un tatuaje)**
- 4–6 fotos de la pieza: una a sangre para la portada, primeros planos y, si hay, **una ya curada** para el cierre.
- Quién la hizo y **permiso del cliente** para publicarla.
- El tema (Ícaro, la catrina…). La historia la investigo yo con fuentes; **no se inventa el significado personal** que tenga para el cliente.

**TIPS DE [ARTISTA] (cómo se hizo una pieza, explicado por zonas)**
- 1 foto general + 1 foto por zona (3–5 zonas) y, si hay, una del proceso (stencil, freehand…).
- **Las explicaciones las da el artista** (audio, nota o respuestas a mis preguntas). No se escriben técnicas por él.
- Duración de la sesión y permiso del cliente.

## Reglas de la serie
- Nunca llamarlo «guía» ni «manual»: la familia se llama **TIPS**.
- Sin cifras en euros. Texto corto: titular + 2 frases por diapositiva como máximo.
- El texto no tapa la cara ni lo importante del tatuaje: abajo en tomas generales, arriba (`"arriba": true`) en primeros planos.
- Acento morado PHARAON por defecto; naranja `#FF8A1F` solo en campañas de Halloween.
