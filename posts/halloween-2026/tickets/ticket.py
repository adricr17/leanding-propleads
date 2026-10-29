"""Ticket digital de premio de la Terror Box (Halloween Costume Week 2026).

Uso: python3 posts/halloween-2026/tickets/ticket.py "2x1 EN MINIS" [--nombre "Laura"] [--valido "31/12/2026"]
Genera tickets/<codigo>.html y tickets/<codigo>/01.png (1080x1350) y apunta el código en registro.csv.
"""
import argparse, csv, datetime, html, os, random, string, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))

a = argparse.ArgumentParser()
a.add_argument('premio'); a.add_argument('--nombre', default=''); a.add_argument('--valido', default='')
a.add_argument('--fecha', default=datetime.date.today().strftime('%d/%m/%Y'))
o = a.parse_args()

random.seed()
codigo = 'TB26-' + ''.join(random.choice('ACDEFGHJKLMNPQRTUVWXY3479') for _ in range(5))
e = lambda s: html.escape(s)
lineas = [('FECHA', o.fecha), ('CÓDIGO', codigo)]
if o.nombre: lineas.insert(0, ('A NOMBRE DE', o.nombre.upper()))
if o.valido: lineas.append(('VÁLIDO HASTA', o.valido))
filas = ''.join(f'<div class="l"><span>{e(k)}</span><span>{e(v)}</span></div>' for k, v in lineas)

doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../_base/base.css">
<style>
.slide {{ background: radial-gradient(circle at 50% 35%, #2a1206 0%, #111 70%); display: flex; justify-content: center; align-items: center; padding: 0; }}
.ticket {{ background: var(--hueso); color: var(--negro); font-family: 'Space Mono'; font-size: 27px; line-height: 1.5; padding: 54px 58px 70px; width: 800px; position: relative; transform: rotate(-2deg);
  box-shadow: 0 30px 80px rgba(255,138,31,.25);
  -webkit-mask: conic-gradient(from -45deg at bottom, #0000, #000 1deg 89deg, #0000 90deg) bottom/36px 100%; }}
.c {{ text-align: center; }}
hr {{ border: 0; border-top: 2px dashed rgba(17,17,17,.5); margin: 20px 0; }}
.l {{ display: flex; justify-content: space-between; white-space: nowrap; gap: 20px; }}
.l span:first-child {{ overflow: hidden; }}
.l span:first-child::after {{ content: ' ....................................'; opacity: .4; }}
.l span:last-child {{ font-weight: 700; }}
.premio {{ font-family: 'Anton'; font-size: 112px; line-height: .95; text-transform: uppercase; color: #E86A00; margin: 10px 0 6px; }}
.marca {{ font-family: 'Anton'; font-size: 64px; letter-spacing: 2px; line-height: 1; }}
.peq {{ font-size: 21px; opacity: .75; }}
.sello {{ position: absolute; right: 95px; top: 492px; transform: rotate(14deg); border: 5px solid #E86A00; color: #E86A00; border-radius: 12px;
  font-family: 'Anton'; font-size: 40px; padding: 4px 16px; letter-spacing: 2px; opacity: .85; }}
.calabaza {{ font-size: 64px; }}
</style></head><body>
<section class="slide"><div class="ticket">
  <div class="c"><div class="marca">PHARAON STUDIO</div>
  <div class="peq">C/ Prolongació Falguera, 2 · Sant Feliu de Llobregat</div></div>
  <hr>
  <div class="c"><b>TERROR BOX</b><br><span class="peq">HALLOWEEN COSTUME WEEK · 2026</span></div>
  <div class="sello">PREMIO</div>
  <hr>
  <div class="c peq">HAS GANADO</div>
  <div class="c premio">{e(o.premio)}</div>
  <div class="c calabaza">🎃</div>
  <hr>
  {filas}
  <hr>
  <div class="c peq">Enséñanos este ticket (vale una captura)<br>al reservar tu cita.</div>
  <div class="c" style="margin-top:14px"><b>@PHARAONSTUDIO</b></div>
</div></section>
</body></html>"""
ruta = f'{AQUI}/{codigo}.html'
open(ruta, 'w').write(doc)
subprocess.run(['node', f'{RAIZ}/posts/_base/render.js', ruta], check=True)
nuevo = not os.path.exists(f'{AQUI}/registro.csv')
with open(f'{AQUI}/registro.csv', 'a', newline='') as f:
    w = csv.writer(f)
    if nuevo: w.writerow(['codigo', 'premio', 'nombre', 'fecha', 'valido_hasta'])
    w.writerow([codigo, o.premio, o.nombre, o.fecha, o.valido])
print(codigo, f'{AQUI}/{codigo}/01.png')
