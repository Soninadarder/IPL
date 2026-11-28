import sys; sys.path.insert(0, "/home/claude/insta")
from carrusel import render, doodle as d

N = "#1D2B4F"; T = "#D9734E"; M = "#E8B04B"; S = "#9DB59A"
MARCA = '<div class="marca" style="left:70px;bottom:56px">@ipl.iaeducacion</div>'

s = []
# 1 portada
s.append((f'''
<div class="abs mano" style="left:80px;top:90px;font-size:64px;color:{T};transform:rotate(-3deg)">antes de Navidad…</div>
<div class="abs" style="left:76px;top:200px;font-size:150px;font-weight:700;line-height:.92;letter-spacing:-.03em">La IA<br>llega<br>a casa</div>
<div class="abs" style="left:70px;top:690px">{d.sub(T, 560, 14)}</div>
<div class="abs" style="left:80px;top:770px;font-size:50px;font-weight:500;line-height:1.25;max-width:960px">5 consejos para padres<br><span class="fosfo">(y para profes que hablan con padres)</span></div>
<div class="posit" style="right:70px;bottom:150px;width:330px;transform:rotate(4deg)"><div class="cinta" style="top:-26px;left:70px;transform:rotate(-6deg)"></div><span class="mano" style="font-size:50px;line-height:1.05">desliza<br>y guárdalo 👉</span></div>
{MARCA}''', "#F6EFE3"))

# 2 clave 1
s.append((f'''
<div class="abs num" style="right:40px;top:30px;font-size:520px;color:{M};opacity:.9">1</div>
<div class="abs" style="left:80px;top:300px;font-size:104px;font-weight:700;line-height:1;max-width:700px;letter-spacing:-.02em">Pruébalo tú antes que ellos</div>
<div class="abs" style="left:84px;top:690px;font-size:46px;line-height:1.35;max-width:820px">Pregúntale como lo haría un niño de su edad. ¿Qué contesta? ¿Guarda lo que dice? ¿Pide fotos o la voz?</div>
<div class="abs mano" style="left:90px;top:1010px;font-size:60px;color:{T};transform:rotate(-2deg)">No acompañamos en lo que no conocemos.</div>
<div class="abs" style="left:110px;top:1080px">{d.sub(T, 620, 9)}</div>
{MARCA}''', "#F3E6D3"))

# 3 clave 2 (fondo oscuro)
s.append((f'''
<div class="abs" style="left:0;top:0;width:1080px;height:1350px;background:{N}"></div>
<div class="abs mano" style="left:80px;top:100px;font-size:70px;color:{M};transform:rotate(-2deg)">2 ·</div>
<div class="abs" style="left:80px;top:190px;font-size:92px;font-weight:700;line-height:1.02;color:#F6EFE3;max-width:900px">Lee la letra pequeña del juguete</div>
<div class="abs" style="left:84px;top:580px;font-size:44px;line-height:1.4;color:#F6EFE3;max-width:880px">Si «habla» con IA, tiene micrófono, internet y a veces cámara. ¿Funciona sin conexión? ¿Tiene control parental?</div>
<div class="posit" style="left:150px;top:920px;width:780px;background:#F2C4B8;transform:rotate(-2.5deg)"><div class="cinta" style="top:-24px;right:90px;transform:rotate(5deg)"></div><span style="font-size:46px;font-weight:700;line-height:1.2">¿Dudas? Mejor un juego de mesa compartido 🎲</span></div>
<div class="marca" style="left:70px;bottom:56px;color:#F6EFE3">@ipl.iaeducacion</div>''', N))

# 4 clave 3
s.append((f'''
<div class="abs" style="left:80px;top:110px;font-size:54px;font-weight:500;color:{T}">3 · normas de casa</div>
<div class="abs" style="left:80px;top:200px;font-size:96px;font-weight:700;line-height:1;max-width:900px;transform:rotate(-1.5deg)">Pocas, claras<br>y <span class="fosfo">para todos</span></div>
<div class="abs" style="left:100px;top:530px;font-size:48px;line-height:1.75">
✔︎ En zonas comunes, no en el cuarto<br>✔︎ Fuera de la mesa y de la cama<br>✔︎ Con un tiempo acordado</div>
<div class="abs" style="right:100px;top:880px">{d.garabato(T, 170)}</div>
<div class="abs mano" style="left:90px;top:1040px;font-size:64px;line-height:1;transform:rotate(-2deg)">…y los padres también las cumplimos 😉</div>
{MARCA}''', "#EAF0E4"))

# 5 clave 4
s.append((f'''
<div class="abs num" style="left:60px;top:60px;font-size:300px;color:{S}">4</div>
<div class="abs" style="left:300px;top:110px;font-size:80px;font-weight:700;line-height:1.02;max-width:700px">Deberes con IA</div>
<div class="abs" style="left:80px;top:400px;width:440px;height:420px;background:#fff;box-shadow:0 10px 24px rgba(0,0,0,.12);transform:rotate(-2deg);padding:40px">
<div style="font-size:70px;font-weight:700;color:{S}">Sí ✅</div><div style="font-size:42px;line-height:1.3;margin-top:16px">que te lo explique de otra manera</div></div>
<div class="abs" style="left:560px;top:430px;width:440px;height:420px;background:#fff;box-shadow:0 10px 24px rgba(0,0,0,.12);transform:rotate(2.5deg);padding:40px">
<div style="font-size:70px;font-weight:700;color:{T}">No ❌</div><div style="font-size:42px;line-height:1.3;margin-top:16px">que te lo haga</div></div>
<div class="abs mano" style="left:80px;top:950px;font-size:60px;line-height:1.1;max-width:920px">«Primero lo intentas tú. Si te atascas, pídele que te explique, no que te lo resuelva.»</div>
{MARCA}''', "#F6EFE3"))

# 6 clave 5
s.append((f'''
<div class="abs" style="left:80px;top:100px;font-size:50px;font-weight:500">5 · en la cena</div>
<div class="abs" style="left:80px;top:180px;font-size:100px;font-weight:700;line-height:1;max-width:900px">Habla de la IA con naturalidad</div>
<div class="posit" style="left:90px;top:520px;width:430px;transform:rotate(-3deg)"><span class="mano" style="font-size:52px;line-height:1.05">«¿Qué le has preguntado hoy?»</span></div>
<div class="posit" style="left:560px;top:600px;width:430px;background:#CFE3C6;transform:rotate(2.5deg)"><span class="mano" style="font-size:52px;line-height:1.05">«¿Te ha dicho algo que no fuera verdad?»</span></div>
<div class="abs" style="left:84px;top:1000px;font-size:44px;line-height:1.35;max-width:900px">Así aprenden que se equivoca y que <b>lo importante se cuenta en casa</b>.</div>
{MARCA}''', "#F8E3D6"))

# 7 final
s.append((f'''
<div class="abs" style="left:80px;top:130px;font-size:56px;font-weight:500;line-height:1.3;max-width:900px">La tecnología no educa sola.</div>
<div class="abs" style="left:80px;top:230px;font-size:130px;font-weight:700;line-height:.95;letter-spacing:-.02em">Educa quien está al lado.</div>
<div class="abs" style="left:330px;top:345px">{d.circ(T, 560, 170)}</div>
<div class="abs" style="left:80px;top:760px;font-size:44px;line-height:1.4;max-width:880px">📰 Y la noticia de la semana sobre juguetes con IA…</div>
<div class="abs mano" style="left:90px;top:900px;font-size:76px;line-height:1;color:{T};transform:rotate(-2deg)">Artículo completo en el blog<br>· enlace en la bio ·</div>
<div class="abs" style="right:80px;top:1120px">{d.estrella(M, 80)}</div>
{MARCA}''', "#F6EFE3"))

render(s, sys.argv[1])
