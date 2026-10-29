"""Genera los carruseles de las series «LA HISTORIA DE…» y «TIPS DE…» a partir de un archivo de contenido.

Uso: python3 posts/_base/carrusel.py posts/<carpeta>/<nombre>.json
Escribe <nombre>.html al lado del .json y lo renderiza a <nombre>/01.png, 02.png… (1080x1350).

Contenido (JSON):
{
  "formato": "historia" | "tips",
  "etiqueta": "PHARAON · LA CATRINA",          texto pequeño arriba a la izquierda
  "fotos": "../../privado/catrina/",            carpeta de las fotos, relativa al .html
  "acento": "#9925AE",                          opcional (morado PHARAON; naranja #FF8A1F en Halloween)
  "diapositivas": [ {...}, ... ]
}
En los textos: <a>…</a> pinta en el color de acento y <b>…</b> en negrita.

Tipos de diapositiva:
  portada   foto, pos, lado ("izquierda"|"derecha"|"arriba"), antetitulo, titulo, texto [líneas], credito, oscuro (true = texto negro sobre fondo claro)
  capitulo  foto, pos, num, titulo, texto, arriba (true = texto arriba, para primeros planos)
  pregunta  foto, pos, titulo, texto                 (tips: pregunta para comentarios)
  paso      foto, pos, paso, cita, quien, marcas [[x, y, radio, "disc"?], ...]   (tips: explicación del artista)
  cierre    foto, pos, num, titulo, texto, handle (true = @PHARAONSTUDIO)
"""
import html, json, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

CSS = """
.bgfoto { position: absolute; inset: 0; background: center / cover no-repeat; z-index: 0; }
.velo { position: absolute; inset: 0; z-index: 0; }
.v-abajo { background: linear-gradient(rgba(10,10,10,.35) 0%, rgba(10,10,10,0) 18%, rgba(10,10,10,0) 42%, rgba(10,10,10,.82) 64%, rgba(10,10,10,.95) 100%); }
.v-arriba { background: linear-gradient(rgba(10,10,10,.95) 0%, rgba(10,10,10,.85) 24%, rgba(10,10,10,0) 36%); }
.v-izquierda { background: linear-gradient(90deg, rgba(10,10,10,.78) 0%, rgba(10,10,10,.45) 28%, rgba(10,10,10,0) 40%); }
.v-derecha { background: linear-gradient(270deg, rgba(10,10,10,.78) 0%, rgba(10,10,10,.45) 28%, rgba(10,10,10,0) 40%); }
.v-cierre { background: linear-gradient(rgba(10,10,10,.35) 0%, rgba(10,10,10,0) 14%, rgba(10,10,10,0) 80%, rgba(10,10,10,.9) 90%, rgba(10,10,10,.95) 100%); }
.slide > .etiqueta, .slide > .contador, .slide > .firma { z-index: 3; text-shadow: 0 2px 10px rgba(0,0,0,.8); }
.texto { position: absolute; left: 90px; right: 90px; bottom: 130px; z-index: 1; }
.texto.arriba { top: 140px; bottom: auto; }
.num { font-family: 'Space Mono'; font-weight: 700; color: var(--acento); font-size: 28px; letter-spacing: 3px; }
.texto .titular { font-size: 96px; margin-top: 16px; }
.texto.arriba .titular { font-size: 76px; margin-top: 10px; }
.texto p { font-size: 38px; line-height: 1.38; margin-top: 26px; }
.texto.arriba p { font-size: 32px; margin-top: 14px; }
.texto p b, .cita b { font-weight: 700; }
.ac { color: var(--acento); }
.col { position: absolute; top: 150px; width: 320px; z-index: 1; color: #fff; }
.col .ante { font-family: 'Space Mono'; font-weight: 700; font-size: 24px; letter-spacing: 4px; }
.col .t1 { font-family: 'Anton'; text-transform: uppercase; font-size: 66px; line-height: .9; margin-top: 12px; }
.col .t2 { font-family: 'Anton'; text-transform: uppercase; font-size: 98px; line-height: .9; color: var(--acento); }
.col .barra { width: 80px; height: 6px; background: var(--acento); margin: 32px 0 28px; }
.col p { font-size: 29px; line-height: 1.35; margin-top: 14px; font-weight: 500; }
.col p:first-of-type { font-size: 32px; font-weight: 700; }
.pie-portada { position: absolute; bottom: 60px; font-family: 'Space Mono'; font-size: 22px; color: #fff; opacity: .9; text-shadow: 0 1px 6px #000; z-index: 2; }
.banda { position: absolute; left: 0; right: 0; top: 0; padding: 150px 90px 120px; background: linear-gradient(rgba(17,17,17,.92) 60%, rgba(17,17,17,0)); z-index: 1; }
.pie { position: absolute; left: 0; right: 0; bottom: 0; padding: 120px 90px 120px; background: linear-gradient(rgba(17,17,17,0), rgba(17,17,17,.94) 35%); z-index: 1; }
.cita { font-size: 35px; line-height: 1.35; border-left: 6px solid var(--acento); padding-left: 26px; }
.cita b { color: var(--acento-claro); }
.quien { font-family: 'Space Mono'; font-size: 26px; color: var(--acento-claro); margin-top: 18px; padding-left: 32px; }
.paso { font-family: 'Space Mono'; font-weight: 700; font-size: 28px; color: var(--acento-claro); letter-spacing: 2px; }
svg.marca { position: absolute; inset: 0; width: 1080px; height: 1350px; z-index: 1; }
svg.marca circle { fill: none; stroke: var(--acento-claro); stroke-width: 7; filter: drop-shadow(0 0 6px rgba(0,0,0,.8)); }
svg.marca .disc { stroke-dasharray: 18 14; }
"""


def marcado(t):
    """Escapa el texto y deja pasar <a>…</a> (acento) y <b>…</b>."""
    t = html.escape(t or '', quote=False)
    t = re.sub(r'&lt;a&gt;(.*?)&lt;/a&gt;', r'<span class="ac">\1</span>', t)
    t = re.sub(r'&lt;b&gt;(.*?)&lt;/b&gt;', r'<b>\1</b>', t)
    return t.replace('\n', '<br>')


def claro(hexa):
    h = hexa.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return '#%02X%02X%02X' % tuple(int(c + (255 - c) * 0.35) for c in (r, g, b))


def fondo(c, d):
    return f'<div class="bgfoto" style="background-image:url({c["fotos"]}{d["foto"]}); background-position: {d.get("pos", "center")}"></div>'


def diapositiva(c, d, n, total):
    cab = f'<div class="etiqueta">{marcado(c["etiqueta"])}</div><div class="contador">{n}/{total}</div>'
    tipo = d['tipo']
    if tipo == 'portada':
        lado = d.get('lado', 'izquierda')
        pos_col = 'left:56px' if lado == 'izquierda' else 'right:56px'
        lineas = ''.join(f'<p>{marcado(x)}</p>' for x in d.get('texto', []))
        col = (f'<div class="col" style="{pos_col}{"; color:#111" if d.get("oscuro") else ""}">'
               f'<div class="ante">{marcado(d.get("antetitulo", ""))}</div>'
               f'<div class="t1">{marcado(d.get("titulo", ""))}</div><div class="t2">{marcado(d.get("titulo_acento", ""))}</div>'
               f'<div class="barra"></div>{lineas}</div>')
        velo = '' if d.get('oscuro') else f'<div class="velo v-{lado}"></div>'
        cred = f'<div class="pie-portada" style="right:60px">{marcado(d["credito"])}</div>' if d.get('credito') else ''
        return (f'<section class="slide">{fondo(c, d)}{velo}'
                f'<div class="contador" style="color:#fff; text-shadow:0 1px 6px #000">{n}/{total}</div>{col}'
                f'<div class="pie-portada" style="left:56px">Desliza →</div>{cred}</section>')
    if tipo == 'capitulo':
        arriba = d.get('arriba')
        return (f'<section class="slide">{fondo(c, d)}<div class="velo {"v-arriba" if arriba else "v-abajo"}"></div>{cab}'
                f'<div class="texto{" arriba" if arriba else ""}"><div class="num">{marcado(d.get("num", ""))}</div>'
                f'<h2 class="titular">{marcado(d["titulo"])}</h2><p>{marcado(d.get("texto", ""))}</p></div></section>')
    if tipo == 'pregunta':
        return (f'<section class="slide">{fondo(c, d)}{cab}<div class="banda"><h2 class="titular t-m">{marcado(d["titulo"])}</h2>'
                f'<p class="sub">{marcado(d.get("texto", ""))}</p></div><div class="firma">@pharaonstudio</div></section>')
    if tipo == 'paso':
        circulos = ''.join(f'<circle{" class=\"disc\"" if len(m) > 3 else ""} cx="{m[0]}" cy="{m[1]}" r="{m[2]}"/>' for m in d.get('marcas', []))
        svg = f'<svg class="marca">{circulos}</svg>' if circulos else ''
        return (f'<section class="slide">{fondo(c, d)}{svg}{cab}<div class="banda"><div class="paso">{marcado(d["paso"])}</div></div>'
                f'<div class="pie"><div class="cita">{marcado(d["cita"])}</div><div class="quien">— {marcado(d["quien"])}</div></div></section>')
    if tipo == 'cierre':
        handle = ('&nbsp;<span class="ac" style="font-family:Anton; font-size:40px; letter-spacing:1px">@PHARAONSTUDIO</span>'
                  if d.get('handle', True) else '')
        return (f'<section class="slide">{fondo(c, d)}<div class="velo v-cierre"></div>{cab}'
                f'<div class="texto" style="bottom:46px"><div class="num">{marcado(d.get("num", ""))}</div>'
                f'<h2 class="titular" style="font-size:62px; margin-top:6px">{marcado(d["titulo"])}</h2>'
                f'<p style="font-size:30px; margin-top:8px">{marcado(d.get("texto", ""))}{handle}</p></div></section>')
    raise ValueError(f'tipo de diapositiva desconocido: {tipo}')


def main(ruta):
    c = json.load(open(ruta))
    acento = c.get('acento', '#9925AE')
    total = len(c['diapositivas'])
    cuerpo = '\n'.join(diapositiva(c, d, i + 1, total) for i, d in enumerate(c['diapositivas']))
    base = os.path.relpath(f'{RAIZ}/posts/_base/base.css', os.path.dirname(os.path.abspath(ruta)))
    doc = (f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8">\n<link rel="stylesheet" href="{base}">\n'
           f'<!-- Generado con posts/_base/carrusel.py desde {os.path.basename(ruta)}: no editar a mano, editar el .json -->\n'
           f'<style>:root {{ --acento: {acento}; --acento-claro: {claro(acento)}; }}{CSS}</style></head><body>\n{cuerpo}\n</body></html>\n')
    salida = ruta[:-5] + '.html'
    open(salida, 'w').write(doc)
    subprocess.run(['node', f'{RAIZ}/posts/_base/render.js', salida], check=True)


if __name__ == '__main__':
    main(sys.argv[1])
