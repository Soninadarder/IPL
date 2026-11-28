import sys, subprocess, pathlib; sys.path.insert(0, "/home/claude/insta")
from carrusel import render, doodle as d

N = "#1D2B4F"; T = "#D9734E"; M = "#E8B04B"; S = "#7FA37A"
OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
MAR = '<div class="marca" style="left:80px;bottom:120px;font-size:36px">@ipl.iaeducacion</div>'

def idea(n, preg, resp, nota, fondo, color, rot):
    base = (f'<div class="abs num" style="right:50px;top:150px;font-size:560px;color:{color};opacity:.85">{n}</div>'
            f'<div class="abs" style="left:80px;top:620px;font-size:112px;font-weight:700;line-height:1;max-width:900px;transform:rotate({rot}deg)">{preg}</div>')
    full = base + (f'<div class="posit" style="left:110px;top:1080px;width:860px;transform:rotate({-rot*1.5}deg)"><div class="cinta" style="top:-24px;left:320px;transform:rotate(-3deg)"></div>'
                   f'<span style="font-size:58px;font-weight:700;line-height:1.15">{resp}</span></div>'
                   f'<div class="abs mano" style="left:110px;top:1460px;font-size:66px;color:{color};transform:rotate(-2deg)">{nota}</div>')
    return [(base + MAR, fondo), (full + MAR, fondo)]

# (pantalla, estado) -> segundos
pantallas = []
p1a = (f'<div class="abs" style="left:80px;top:420px;font-size:128px;font-weight:700;line-height:.95;letter-spacing:-.02em">¿Vas a regalar un juguete que <span class="fosfo">«habla»</span>?</div>{MAR}', "#F6EFE3")
p1b = (p1a[0].replace(MAR, '') + f'<div class="abs mano" style="left:90px;top:1050px;font-size:84px;color:{T};transform:rotate(-3deg)">Antes, hazte estas<br>3 preguntas 👇</div><div class="abs" style="left:620px;top:1240px">{d.flecha(N, 170, 30)}</div>{MAR}', "#F6EFE3")
pantallas.append([(p1a, 1.0), (p1b, 3.8)])
for n, preg, resp, nota, fondo, color, rot in [
    (1, "¿Funciona sin internet?", "Si no, lo que oye sale de casa.", "pregunta antes de comprar", "#F3E6D3", M, -1.5),
    (2, "¿Graba su voz o su cara?", "Mira qué guarda y dónde.", "la letra pequeña importa", "#EAF0E4", S, 1.2),
    (3, "¿Lo usaremos juntos?", "Ningún juguete sustituye un rato contigo.", "eso no lo hace ninguna IA ❤️", "#F8E3D6", T, -2),
]:
    a, b = idea(n, preg, resp, nota, fondo, color, rot)
    pantallas.append([(a, 1.2), (b, 5.8)])
f_a = (f'<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:{N}"></div>'
       f'<div class="abs" style="left:80px;top:520px;font-size:120px;font-weight:700;line-height:1;color:#F6EFE3">Ante la duda…</div>', N)
f_b = (f_a[0] + f'<div class="posit" style="left:120px;top:860px;width:840px;transform:rotate(-2.5deg)"><span style="font-size:80px;font-weight:700;line-height:1.1">un juego de mesa en familia 🎲</span></div>'
       f'<div class="abs mano" style="left:90px;top:1300px;font-size:64px;color:{M};transform:rotate(-2deg)">más ideas para familias cada semana</div>'
       f'<div class="marca" style="left:80px;bottom:120px;font-size:40px;color:#F6EFE3">@ipl.iaeducacion</div>', N)
pantallas.append([(f_a, 0.8), (f_b, 4.2)])

estados = [e for p in pantallas for e, _ in p]
nombres = [f"p{i}_{j}" for i, p in enumerate(pantallas) for j in range(len(p))]
render(estados, OUT, 1080, 1920, "png", nombres)
render([pantallas[0][1][0]], OUT, 1080, 1920, "jpg", ["portada"])

# un clip por pantalla con zoom lento (Ken Burns 4 %)
FPS = 30; TR = 0.5
clips, durs = [], []
for i, p in enumerate(pantallas):
    lista = OUT / f"l{i}.txt"
    lineas = []
    for j, (_, t) in enumerate(p):
        extra = TR if (i < len(pantallas) - 1 and j == len(p) - 1) else 0
        lineas += [f"file 'p{i}_{j}.png'", f"duration {t + extra:.2f}"]
    lineas.append(f"file 'p{i}_{len(p)-1}.png'")
    lista.write_text("\n".join(lineas))
    dur = sum(t for _, t in p) + (TR if i < len(pantallas) - 1 else 0)
    nfr = int(dur * FPS)
    zin = i % 2 == 0
    z = f"1+0.04*on/{nfr}" if zin else f"1.04-0.04*on/{nfr}"
    c = OUT / f"c{i}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista),
                    "-vf", f"fps={FPS},scale=2160:3840,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS},format=yuv420p",
                    "-frames:v", str(nfr), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(c)], check=True)
    clips.append(c); durs.append(dur)

trans = ["fade", "slideleft", "zoomin", "slideup"]
inputs = sum([["-i", str(c)] for c in clips], [])
fc, prev, off = [], "[0:v]", 0
for i in range(1, len(clips)):
    off += durs[i - 1] - TR
    lab = f"[v{i}]"
    fc.append(f"{prev}[{i}:v]xfade=transition={trans[(i-1)%len(trans)]}:duration={TR}:offset={off:.2f}{lab}")
    prev = lab
total = sum(durs) - TR * (len(clips) - 1)
musica = sys.argv[2]
inputs += ["-i", musica]
fc.append(f"[{len(clips)}:a]atrim=0:{total:.2f},asetpts=PTS-STARTPTS,volume={sys.argv[3]},afade=t=in:d=1.5,afade=t=out:st={total-2.5:.2f}:d=2.5[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", prev, "-map", "[a]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", "-t", f"{total:.2f}", str(OUT / "reel.mp4")], check=True)
print("duración", round(total, 2), [round(x, 2) for x in durs])
