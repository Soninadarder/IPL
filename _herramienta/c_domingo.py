import sys; sys.path.insert(0, "/home/claude/insta")
from carrusel import render, doodle as d

N = "#1D2B4F"; T = "#D9734E"; M = "#E8B04B"; S = "#7FA37A"
MARCA = '<div class="marca" style="left:70px;bottom:56px">@ipl.iaeducacion</div>'
CAJA = '<span style="display:inline-block;width:44px;height:44px;border:5px solid #1D2B4F;border-radius:6px 10px 5px 9px;margin-right:22px;vertical-align:-6px;transform:rotate(-4deg)"></span>'

def hoja(titulo, filas, rot, color, fondo, nota=''):
    lis = "".join(f'<div style="margin:30px 0;font-size:50px;line-height:1.2">{CAJA}{f}</div>' for f in filas)
    return (f'''
<div class="abs" style="left:90px;top:230px;width:900px;min-height:600px;background:#FFFDF7;box-shadow:0 16px 34px rgba(0,0,0,.15);transform:rotate({rot}deg);padding:70px 66px;
background-image:repeating-linear-gradient(transparent 0 78px,rgba(80,120,200,.18) 78px 80px)">
<div class="cinta" style="top:-26px;left:350px;transform:rotate(-4deg)"></div>
<div style="font-size:66px;font-weight:700;color:{color};margin-bottom:20px">{titulo}</div>{lis}</div>
<div class="abs mano" style="left:110px;top:960px;font-size:62px;line-height:1.05;max-width:860px;color:{color};transform:rotate(-2deg)">{nota}</div>
{MARCA}''', fondo)

s = []
s.append((f'''
<div class="abs mano" style="left:84px;top:110px;font-size:70px;color:{T};transform:rotate(-3deg)">un regalo para el domingo 🎁</div>
<div class="abs" style="left:76px;top:240px;font-size:128px;font-weight:700;line-height:.95;letter-spacing:-.03em">El pacto<br>familiar<br>de la <span class="fosfo">IA</span></div>
<div class="abs" style="left:80px;top:690px;font-size:52px;font-weight:500;line-height:1.25;max-width:640px">Una plantilla para leer juntos, firmar y pegar en la nevera</div>
<div class="posit" style="right:80px;top:820px;width:330px;height:330px;transform:rotate(5deg)"><div class="cinta" style="top:-24px;left:70px;transform:rotate(3deg)"></div><span class="mano" style="font-size:58px;line-height:1">guárdalo<br>e imprímelo 📌</span></div>
{MARCA}''', "#F6EFE3"))

s.append((f'''
<div class="abs" style="left:80px;top:120px;font-size:58px;font-weight:500;color:{T}">Cómo se usa</div>
<div class="abs" style="left:80px;top:220px;font-size:84px;font-weight:700;line-height:1.05;max-width:900px">Sin sermones: en una comida tranquila</div>
<div class="abs" style="left:96px;top:540px;font-size:48px;line-height:1.5;max-width:880px">
<b>1.</b> Lo leéis juntos.<br><b>2.</b> Cada uno propone algo.<br><b>3.</b> Rellenáis los huecos.<br><b>4.</b> Firmáis <span class="fosfo">todos</span>.</div>
<div class="abs mano" style="left:520px;top:1010px;font-size:64px;line-height:1;transform:rotate(-4deg);color:{N}">sí, papá y mamá<br>también 😉</div>
<div class="abs" style="left:380px;top:960px">{d.flecha(T, 130, 100)}</div>
{MARCA}''', "#F3E6D3"))

s.append(hoja("En casa, la IA…", ["se usa en el salón o la cocina", "no viene a la mesa ni a la cama", "máximo ____ minutos al día"], -2, T, "#EAF0E4", "los minutos los decidís juntos ✍️"))
s.append(hoja("Para los deberes…", ["primero lo intento yo", "le pido que me explique, no que me lo haga", "si la he usado, lo digo"], 1.8, S, "#F8E3D6", "el esfuerzo también se educa 💪"))

s.append((f'''
<div class="abs" style="left:0;top:0;width:1080px;height:1350px;background:{N}"></div>
<div class="abs" style="left:80px;top:130px;font-size:96px;font-weight:700;line-height:1;color:#F6EFE3;max-width:900px">A la IA nunca le contamos…</div>
<div class="abs" style="left:100px;top:420px;font-size:56px;line-height:1.7;color:#F6EFE3">✗ dónde vivimos<br>✗ fotos nuestras<br>✗ contraseñas</div>
<div class="posit" style="left:170px;top:880px;width:760px;transform:rotate(-2deg)"><div class="cinta" style="top:-24px;left:280px;transform:rotate(4deg)"></div><span class="mano" style="font-size:60px;line-height:1.05">Lo que nos preocupa se habla en casa ❤️</span></div>
<div class="marca" style="left:70px;bottom:56px;color:#F6EFE3">@ipl.iaeducacion</div>''', N))

s.append((f'''
<div class="abs" style="left:80px;top:110px;font-size:84px;font-weight:700;line-height:1;max-width:900px">Y al final… <span class="mano" style="font-size:110px;color:{T}">¡a firmar!</span></div>
<div class="abs" style="left:90px;top:330px;width:900px;background:#FFFDF7;box-shadow:0 14px 30px rgba(0,0,0,.14);transform:rotate(-1.2deg);padding:60px 64px">
<div style="font-size:46px;font-weight:500">Firmamos:</div>
<div style="display:flex;gap:40px;margin:70px 0 20px">{"".join('<div style="flex:1;border-bottom:4px solid #1D2B4F"></div>' for _ in range(3))}</div>
<div style="font-size:46px;font-weight:500;margin-top:60px">Lo revisamos el día: ______</div></div>
<div class="abs" style="left:80px;top:870px;font-size:46px;line-height:1.35;max-width:900px">Un pacto que se cumple en familia vale más que cualquier control parental.</div>
<div class="abs mano" style="left:90px;top:1070px;font-size:64px;color:{T};transform:rotate(-2deg)">📌 Guárdalo y compártelo</div>
<div class="abs" style="right:90px;top:1060px">{d.estrella(M, 80)}</div>
{MARCA}''', "#F6EFE3"))

render(s, sys.argv[1])
