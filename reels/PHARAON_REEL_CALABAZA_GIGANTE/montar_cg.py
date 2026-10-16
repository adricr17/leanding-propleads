import subprocess, os
W,H,FPS=1080,1920,30
CAL='../PHARAON_REEL_CALABAZA_HALLOWEEN/clips/calabaza_10s.mp4'
LOGO='../_base/tomas/logo-pared.mp4'
DARK='eq=brightness=-0.16:contrast=1.25:gamma=0.6:saturation=1.3,vignette=PI/3.5'
PUNCH='crop=iw*0.75:ih*0.75,scale=1080:1920'
# (tipo, fuente, desde, duración, extra)
S=[('img','imagenes/01_cielo.png',0,1.8,(0.5,0.5,1.12)),
   ('vid','clips/caida.mp4',0,1.8,''),
   ('vid','clips/caida.mp4',1.8,1.87,PUNCH),
   ('vid','clips/caida.mp4',3.0,2.06,''),
   ('img','imagenes/02_pueblo.png',0,1.3,(0.5,0.6,1.15)),
   ('vid','clips/impacto.mp4',1.6,2.42,'shake'),
   ('img','imagenes/04_meteorito.png',0,2.0,(0.5,0.5,1.1)),
   ('img','imagenes/04_meteorito.png',0,1.95,(0.62,0.22,1.35)),
   ('vid','clips/explosion.mp4',0,1.7,'shake'),
   ('vid','clips/explosion.mp4',1.7,1.8,''),
   ('img','imagenes/06_cohete.png',0,1.47,(0.55,0.2,1.15)),
   ('vid',CAL,2.2,2.02,''),
   ('vid',CAL,4.2,3.18,'shake'),
   ('img','imagenes/07_poster.png',0,1.8,(0.5,0.5,1.05)),
   ('img','imagenes/07_poster.png',0,1.8,(0.25,0.08,1.9)),
   ('img','imagenes/07_poster.png',0,1.8,(0.5,0.65,1.6)),
   ('img','imagenes/07_poster.png',0,1.81,(0.5,0.92,1.7)),
   ('vid',LOGO,0,3.4,DARK)]
outs=[]
for i,(t,src,ss,d,ex) in enumerate(S):
    o=f'cortes/s{i:02d}.mp4'; fr=round(d*FPS)
    if t=='img':
        cx,cy,z=ex
        vf=(f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='{z}+0.06*on/{fr}':x='max(0,min(iw-iw/zoom,iw*{cx}-iw/zoom/2))':y='max(0,min(ih-ih/zoom,ih*{cy}-ih/zoom/2))':d={fr}:s={W}x{H}:fps={FPS}")
        cmd=['ffmpeg','-loglevel','error','-y','-loop','1','-i',src,'-vf',vf+',setsar=1,format=yuv420p','-frames:v',str(fr)]
    else:
        base=f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
        if ex=='shake': base+=f",scale=1166:2074,crop={W}:{H}:x='43+36*sin(t*70)*exp(-t*4)':y='77+30*cos(t*83)*exp(-t*4)'"
        elif ex: base+=','+ex
        cmd=['ffmpeg','-loglevel','error','-y','-ss',str(ss),'-i',src,'-vf',base+',setsar=1,format=yuv420p','-frames:v',str(fr),'-an']
    subprocess.run(cmd+['-c:v','libx264','-crf','18','-preset','medium','-r',str(FPS),o],check=True); outs.append(o)
open('cortes/lista.txt','w').write(''.join(f"file '{os.path.basename(o)}'\n" for o in outs))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i','cortes/lista.txt','-c','copy','cortes/video.mp4'],check=True)
print(sum(s[3] for s in S))
