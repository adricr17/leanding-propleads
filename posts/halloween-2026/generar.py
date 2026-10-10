from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import sys
P='/tmp/claude-0/-home-user-leanding-propleads/872786be-9ea7-5130-ad53-28ad87a6c068/scratchpad/hw/poster_fecha.png'
F='/home/user/leanding-propleads/posts/_base/fuentes/'
OUT='/home/user/leanding-propleads/posts/halloween-2026/'
W,H=1080,1350
ROJO=(235,35,35); CREMA=(240,228,210); GRIS=(200,190,180)
poster=Image.open(P).convert('RGB')
def fondo(cy, zoom=1.6, bright=0.32):
    w=int(poster.width/zoom); h=int(w*H/W)
    y=int(poster.height*cy-h/2); y=max(0,min(poster.height-h,y)); x=(poster.width-w)//2
    bg=poster.crop((x,y,x+w,y+h)).resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(16))
    bg=ImageEnhance.Brightness(bg).enhance(bright)
    # viñeta
    v=Image.new('L',(W,H),0); d=ImageDraw.Draw(v)
    for i in range(40): d.rectangle([i*6,i*6,W-i*6,H-i*6],outline=int(255*(1-i/40)))
    v=v.filter(ImageFilter.GaussianBlur(60))
    bg.paste((0,0,0),(0,0),v.point(lambda p: int(p*0.8)))
    return bg
def font(n,s): return ImageFont.truetype(F+n,s)
def centro(d,y,txt,f,col,glow=False,img=None):
    w=d.textlength(txt,font=f); x=(W-w)/2
    if glow and img is not None:
        g=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(g)
        gd.text((x,y),txt,font=f,fill=ROJO+(255,)); g=g.filter(ImageFilter.GaussianBlur(14))
        img.paste(g,(0,0),g); d=ImageDraw.Draw(img)
    d.text((x,y),txt,font=f,fill=col)
    return d
def parrafo(d,y,txt,f,col,ancho=880,inter=1.35):
    pal=txt.split(); lin=[]; act=''
    for p in pal:
        t=(act+' '+p).strip()
        if d.textlength(t,font=f)>ancho and act: lin.append(act); act=p
        else: act=t
    lin.append(act)
    for l in lin:
        d.text(((W-d.textlength(l,font=f))/2,y),l,font=f,fill=col); y+=int(f.size*inter)
    return y
def firma(d,n):
    f=font('Anton-Regular.ttf',34); d.text((60,H-80),'PHARAON STUDIO',font=f,fill=ROJO)
    f2=font('DMSans-500.ttf',28); t=f'{n}/6'; d.text((W-60-d.textlength(t,font=f2),H-74),t,font=f2,fill=GRIS)
def titulo(img,y,lineas,size=128):
    d=ImageDraw.Draw(img); f=font('Anton-Regular.ttf',size)
    for l in lineas:
        d=centro(d,y,l,f,ROJO,glow=True,img=img); y+=int(size*1.08)
    return ImageDraw.Draw(img), y
def linea(d,y):
    d.rectangle([W/2-60,y,W/2+60,y+5],fill=ROJO)

# 2
img=fondo(0.3,1.8); d,y=titulo(img,250,['HALLOWEEN','COSTUME WEEK'],120)
y+=30; d=centro(d,y,'DEL 27 AL 31 DE OCTUBRE',font('Anton-Regular.ttf',58),CREMA); y+=110
linea(d,y); y+=60
y=parrafo(d,y,'Ven disfrazado de terror a tu cita en PHARAON y llévate premio seguro.',font('DMSans-700.ttf',48),CREMA)
y+=30; parrafo(d,y,'Y si tu disfraz es el mejor… hay premio gordo.',font('DMSans-500.ttf',42),GRIS)
firma(d,2); img.save(OUT+'02_costume_week.png')

# 3
img=fondo(0.25,2.2); d,y=titulo(img,150,['TERROR BOX'],140)
d=centro(d,y+10,'METE LA MANO. SACA TU PREMIO.',font('Anton-Regular.ttf',50),CREMA); y+=110
y=parrafo(d,y,'Si vienes a tu cita disfrazado, sacas un premio al azar de nuestra caja del terror:',font('DMSans-500.ttf',36),GRIS,860)
y+=25
items=['Aftercare gratis','Descuento en piercing','2×1 en mini tattoos para tu próxima cita','10 % en tu próximo tatuaje','Camiseta PHARAON Clothing','Lámina de regalo']
f=font('DMSans-700.ttf',40)
for it in items:
    w=d.textlength(it,font=f); x=(W-w)/2
    d.ellipse([x-34,y+16,x-20,y+30],fill=ROJO); d.text((x,y),it,font=f,fill=CREMA); y+=62
y+=25
d.rounded_rectangle([110,y,W-110,y+150],radius=18,outline=ROJO,width=4,fill=(30,5,5))
d=centro(d,y+18,'PREMIOS ESPECIALES',font('Anton-Regular.ttf',44),ROJO)
parrafo(d,y+78,'Mini tattoo gratis · Bono para tu próximo tatuaje',font('DMSans-700.ttf',32),CREMA,860)
firma(d,3); img.save(OUT+'03_terror_box.png')

# 4
img=fondo(0.36,2.4); d,y=titulo(img,240,['BEST CLIENT','COSTUME'],130)
y+=20; d=centro(d,y,'EL MEJOR DISFRAZ LO ELEGÍS VOSOTROS',font('Anton-Regular.ttf',48),CREMA); y+=110
linea(d,y); y+=60
y=parrafo(d,y,'Subiremos los disfraces a nuestro Instagram y la comunidad votará al ganador.',font('DMSans-700.ttf',46),CREMA)
y+=40; d=centro(d,y,'PREMIO',font('Anton-Regular.ttf',52),ROJO); y+=80
y=parrafo(d,y,'Un descuentazo en tu próximo tatuaje grande en PHARAON.',font('DMSans-700.ttf',46),CREMA)
y+=20; parrafo(d,y,'Condiciones por DM.',font('DMSans-400.ttf',32),GRIS)
firma(d,4); img.save(OUT+'04_best_costume.png')

# 5
img=fondo(0.15,2.0); d,y=titulo(img,330,['¿NO VIENES','A TATUARTE?'],130)
y+=10; d,y=titulo(img,y,['VEN IGUAL.'],110)
y+=40; linea(d,y); y+=60
y=parrafo(d,y,'Pásate disfrazado por el estudio entre el 27 y el 31 de octubre y participa en el concurso al mejor disfraz.',font('DMSans-700.ttf',46),CREMA)
firma(d,5); img.save(OUT+'05_ven_igual.png')

# 6
img=fondo(0.42,2.6); d,y=titulo(img,170,['¿TE ATREVES?'],140)
y+=20; y=parrafo(d,y,'Reserva tu cita por DM',font('DMSans-700.ttf',52),CREMA)
d=centro(d,y+5,'@PHARAONSTUDIO',font('Anton-Regular.ttf',72),ROJO); y+=130
linea(d,y); y+=50
y=parrafo(d,y,'Carrer de Prolongació Falguera, 2',font('DMSans-500.ttf',38),CREMA)
y=parrafo(d,y,'Sant Feliu de Llobregat',font('DMSans-500.ttf',38),CREMA)
y+=15; y=parrafo(d,y,'Martes a sábado, de 9:00 a 19:00',font('DMSans-500.ttf',38),GRIS)
y+=55; d=centro(d,y,'NUESTROS ARTISTAS',font('Anton-Regular.ttf',44),ROJO); y+=75
for l in ['@uri.cr_tattoo   @avilastattoo   @siz0.tattoo','@delia.tattoo   @carlosmoreno.es   @meii.tattoo']:
    y=parrafo(d,y,l,font('DMSans-700.ttf',34),CREMA,1000)
firma(d,6); img.save(OUT+'06_reserva.png')
print('ok')
