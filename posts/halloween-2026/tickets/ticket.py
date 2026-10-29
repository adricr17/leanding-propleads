"""Ticket digital de premio de la Terror Box (Halloween Costume Week 2026).

Uso:
  python3 posts/halloween-2026/tickets/ticket.py "2x1 en minis" --para "@usuario" --precio "2 minis por el precio de 1 · 70 €" \
      --condicion "Mini: 5×5 cm (palabra: hasta 7 cm)" --condicion "Sin sombra y sin relleno" [--codigo TB26-XXXXX] [--valido 31/12/2026]
Genera tickets/<codigo>.html y tickets/<codigo>/01.png (1080x1350). Un código nuevo se apunta en registro.csv.
Es un documento privado para el cliente: aquí sí pueden ir precios (la regla de no poner euros es para publicaciones).
"""
import argparse, csv, datetime, html, os, random, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))

a = argparse.ArgumentParser()
a.add_argument('premio')
a.add_argument('--para', default='')
a.add_argument('--precio', default='')
a.add_argument('--condicion', action='append', default=[])
a.add_argument('--valido', default='')
a.add_argument('--codigo', default='')
a.add_argument('--fecha', default=datetime.date.today().strftime('%d/%m/%Y'))
o = a.parse_args()

nuevo_codigo = not o.codigo
codigo = o.codigo or 'TB26-' + ''.join(random.choice('ACDEFGHJKLMNPQRTUVWXY3479') for _ in range(5))
e = lambda s: html.escape(s)
datos = [('FECHA', o.fecha)] + ([('VÁLIDO HASTA', o.valido)] if o.valido else [])
filas = ''.join(f'<div class="l"><span>{e(k)}</span><span>{e(v)}</span></div>' for k, v in datos)
conds = ''.join(f'<li>{e(c)}</li>' for c in o.condicion)

doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../_base/base.css">
<style>
:root {{ --naranja: #FF8A1F; }}
.slide {{ padding: 0; background: #0b0b0b; }}
.fondo {{ position: absolute; inset: 0; background: url(../edit/fondo.jpg) center / cover; filter: brightness(.55) saturate(1.15); }}
.brillo {{ position: absolute; inset: 0; background: radial-gradient(circle at 50% 45%, rgba(255,138,31,.18), rgba(0,0,0,0) 60%); }}
.ticket {{ position: absolute; left: 130px; right: 130px; top: 50%; display: flex; flex-direction: column;
  transform: translateY(-50%) rotate(-2deg); filter: drop-shadow(0 30px 60px rgba(0,0,0,.7)) drop-shadow(0 0 40px rgba(255,138,31,.25)); }}
.cuerpo, .talon {{ background: #141110; color: #F4EDE4; border: 3px solid var(--naranja); position: relative; }}
/* cuerpo */ .cuerpo {{ border-radius: 28px 28px 0 0; border-bottom: none; padding: 46px 50px 36px; text-align: center; background: rgba(20,17,16,.93); }}
.talon {{ border-radius: 0 0 28px 28px; border-top: 3px dashed rgba(255,138,31,.8); padding: 26px 56px 32px; font-family: 'Space Mono'; }}
/* muescas de troquel */
.talon::before, .talon::after {{ content: ''; position: absolute; top: -26px; width: 50px; height: 50px; border-radius: 50%; background: #0b0b0b; border: 3px solid var(--naranja); }}
.talon::before {{ left: -28px; clip-path: inset(0 0 0 50%); }}
.talon::after {{ right: -28px; clip-path: inset(0 50% 0 0); }}
.marca {{ font-family: 'Anton'; font-size: 60px; letter-spacing: 3px; line-height: 1; }}
.dir {{ font-family: 'Space Mono'; font-size: 20px; opacity: .65; margin-top: 8px; }}
.evento {{ font-family: 'Space Mono'; font-weight: 700; font-size: 24px; letter-spacing: 4px; color: var(--naranja); margin-top: 26px; }}
.para {{ font-family: 'Space Mono'; font-size: 26px; margin-top: 30px; opacity: .85; }}
.para b {{ color: var(--naranja); font-weight: 700; }}
.premio {{ font-family: 'Anton'; text-transform: uppercase; font-size: 128px; line-height: .92; color: var(--naranja); margin-top: 10px;
  text-shadow: 0 0 30px rgba(255,138,31,.45); }}
.precio {{ font-family: 'DM Sans'; font-weight: 700; font-size: 38px; margin-top: 14px; }}
ul {{ list-style: none; margin: 30px auto 0; padding: 0; display: inline-block; text-align: left; font-family: 'DM Sans'; font-size: 29px; line-height: 1.5; }}
li::before {{ content: '🎃  '; }}
.l {{ display: flex; justify-content: space-between; font-size: 24px; }}
.l span:last-child {{ font-weight: 700; }}
.codigo {{ text-align: center; font-family: 'Anton'; font-size: 66px; letter-spacing: 6px; color: var(--naranja); margin-top: 8px; line-height: 1.1; }}
.nota {{ text-align: center; font-size: 19px; opacity: .7; margin-top: 4px; }}
</style></head><body>
<section class="slide"><div class="fondo"></div><div class="brillo"></div>
 <div class="ticket">
  <div class="cuerpo">
   <div class="marca">PHARAON STUDIO</div>
   <div class="dir">C/ Prolongació Falguera, 2 · Sant Feliu de Llobregat</div>
   <div class="evento">TERROR BOX · HALLOWEEN 2026</div>
   {f'<div class="para">Premio para <b>{e(o.para)}</b></div>' if o.para else '<div class="para">HAS GANADO</div>'}
   <div class="premio">{e(o.premio)}</div>
   {f'<div class="precio">{e(o.precio)}</div>' if o.precio else ''}
   {f'<ul>{conds}</ul>' if conds else ''}
  </div>
  <div class="talon">
   {filas}
   <div class="codigo">{e(codigo)}</div>
   <div class="nota">Enséñanos este ticket (vale una captura) al reservar<br>@PHARAONSTUDIO</div>
  </div>
 </div>
</section>
</body></html>"""
ruta = f'{AQUI}/{codigo}.html'
open(ruta, 'w').write(doc)
subprocess.run(['node', f'{RAIZ}/posts/_base/render.js', ruta], check=True)
if nuevo_codigo:
    nuevo = not os.path.exists(f'{AQUI}/registro.csv')
    with open(f'{AQUI}/registro.csv', 'a', newline='') as f:
        w = csv.writer(f)
        if nuevo: w.writerow(['codigo', 'premio', 'para', 'fecha', 'valido_hasta'])
        w.writerow([codigo, o.premio, o.para, o.fecha, o.valido])
print(codigo, f'{AQUI}/{codigo}/01.png')
