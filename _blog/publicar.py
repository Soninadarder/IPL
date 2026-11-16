#!/usr/bin/env python3
"""Genera el blog de IPL a partir de _blog/articulos/*.md.

Cada artículo: cabecera «clave: valor» (titulo, fecha AAAA-MM-DD, resumen, etiquetas),
una línea «---» y el texto en Markdown sencillo (## títulos, párrafos, listas -, **negrita**,
*cursiva*, [enlaces](url)).

Crea blog/index.html, blog/<slug>.html y actualiza en index.html la sección «Del blog»
(entre <!--BLOG:INICIO--> y <!--BLOG:FIN-->).
Uso: python3 _blog/publicar.py
"""
import html, re, pathlib, datetime

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "_blog" / "articulos"
OUT = RAIZ / "blog"
WEB = "https://soninadarder.github.io/IPL/"
MESES = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()


def fecha_larga(f):
    d = datetime.date.fromisoformat(f)
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*", r"<em>\1</em>", t)
    return t


def md(texto):
    out, lista = [], False
    for bloque in re.split(r"\n\s*\n", texto.strip()):
        lineas = bloque.strip().splitlines()
        if all(l.startswith("- ") for l in lineas):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lineas) + "</ul>")
        elif bloque.startswith("## "):
            out.append(f"<h2>{inline(bloque[3:].strip())}</h2>")
        elif bloque.startswith("### "):
            out.append(f"<h3>{inline(bloque[4:].strip())}</h3>")
        else:
            out.append(f"<p>{inline(' '.join(lineas))}</p>")
    return "\n".join(out)


def leer(p):
    cab, cuerpo = p.read_text(encoding="utf-8").split("\n---\n", 1)
    a = dict(l.split(":", 1) for l in cab.strip().splitlines())
    a = {k.strip(): v.strip() for k, v in a.items()}
    a["slug"] = p.stem
    a["etiquetas"] = [e.strip() for e in a.get("etiquetas", "").split(",") if e.strip()]
    a["html"] = md(cuerpo)
    palabras = len(re.findall(r"\w+", cuerpo))
    a["min"] = max(1, round(palabras / 200))
    return a


LOGO = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="tri" viewBox="0 0 120 120"><g transform="translate(60 59) scale(0.72) translate(-60 -64)" stroke-linecap="round">
<line x1="28" y1="88" x2="60" y2="28" stroke="currentColor" stroke-width="5"/><line x1="92" y1="88" x2="60" y2="28" stroke="currentColor" stroke-width="5"/>
<line x1="28" y1="88" x2="92" y2="88" stroke="currentColor" stroke-width="5"/><line x1="60" y1="28" x2="60" y2="66" style="stroke:var(--accent, #D4AF6A)" stroke-width="3.5"/>
<line x1="28" y1="88" x2="60" y2="66" style="stroke:var(--accent, #D4AF6A)" stroke-width="3.5"/><line x1="92" y1="88" x2="60" y2="66" style="stroke:var(--accent, #D4AF6A)" stroke-width="3.5"/>
<circle cx="60" cy="28" r="10" fill="currentColor"/><circle cx="28" cy="88" r="10" fill="currentColor"/><circle cx="92" cy="88" r="10" fill="currentColor"/>
<circle cx="60" cy="66" r="8" style="fill:var(--accent, #D4AF6A)"/></g></symbol>
<symbol id="rings" viewBox="0 0 120 120"><circle cx="60" cy="60" r="56" fill="none" style="stroke:var(--accent, #D4AF6A)" stroke-width="2.5"/>
<circle cx="60" cy="60" r="49" fill="none" style="stroke:var(--accent, #D4AF6A)" stroke-width="1"/></symbol></defs></svg>"""

CSS = """
:root{--navy:#1C2B4A;--navy-deep:#111C33;--gold-ink:#7A5A26;--gold-soft:#D4AF6A;--bg:#FFFFFF;--band:#F7F5F0;--line:#E4DFD4;--fg:#1C2B4A;--muted:#4E5A70;--card:#FFFFFF;
--font-display:"Space Grotesk","Inter",system-ui,sans-serif;--font-body:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif}
@media (prefers-color-scheme:dark){:root{--bg:#0E1628;--band:#141F36;--line:#2A3A5C;--fg:#EEF1F6;--muted:#B4BED0;--card:#18243E;--gold-ink:#D4AF6A;color-scheme:dark}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-body);font-size:17px;line-height:1.7;overflow-x:hidden}
a{color:inherit}h1,h2,h3{font-family:var(--font-display);line-height:1.15;text-wrap:balance;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.top{position:sticky;top:0;z-index:30;background:rgba(17,28,51,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);color:#fff;border-bottom:1px solid rgba(212,175,106,.25)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;min-width:0}.brand svg{flex:none}
.brand b{font-family:var(--font-display);font-size:26px;line-height:1;display:block}
.brand span{display:block;font-size:10px;letter-spacing:1.6px;text-transform:uppercase;color:#C9D0DC;line-height:1.35;margin-top:3px}
.menu{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:2px 18px;font-size:14.5px;font-weight:500}
.menu a{text-decoration:none;padding:10px 0;color:#E6EAF2}.menu a.on,.menu a:hover{color:var(--gold-soft)}
@media (max-width:760px){.menu{display:none}}
@media (max-width:520px){.brand span{font-size:8.5px;letter-spacing:1px}}
.hero{background:var(--navy);color:#fff;padding-block:clamp(48px,7vw,88px)}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:2.6px;text-transform:uppercase;color:var(--gold-soft)}
.hero h1{font-size:clamp(32px,5vw,54px);letter-spacing:-.8px;margin:12px 0 14px;max-width:900px}
.hero p{color:#C9D0DC;max-width:720px;margin:0;font-size:18px}
.meta{font-size:14px;color:#C9D0DC;margin-top:18px}
.lista{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;padding-block:56px 88px}
@media (max-width:960px){.lista{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:620px){.lista{grid-template-columns:1fr}}
.card{display:flex;flex-direction:column;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px;text-decoration:none;transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(17,28,51,.12)}
.card time{font-size:13px;color:var(--muted)}.card h2,.card h3{font-size:21px}.card p{margin:0;color:var(--muted);font-size:15.5px}
.card .mas{margin-top:auto;font-weight:700;color:var(--gold-ink);font-size:15px}
.tags{display:flex;flex-wrap:wrap;gap:6px}.tags span{font-size:12px;font-weight:600;border:1px solid var(--line);border-radius:999px;padding:2px 10px;color:var(--muted)}
article{max-width:740px;margin:0 auto;padding-block:48px 80px}
article h2{font-size:clamp(23px,3vw,28px);margin:38px 0 10px}article h3{font-size:20px;margin:28px 0 8px}
article p,article ul{margin:0 0 16px}article a{color:var(--gold-ink);font-weight:600}
.autora{display:flex;gap:14px;align-items:center;border-top:1px solid var(--line);margin-top:40px;padding-top:24px;font-size:15px;color:var(--muted)}
.autora b{color:var(--fg)}
.volver{display:inline-block;margin-top:28px;font-weight:700;text-decoration:none;color:var(--gold-ink)}
footer{background:var(--navy-deep);color:#C9D0DC;padding-block:36px;font-size:14px}
footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:14px 24px}footer a{text-decoration:none;color:#fff}
"""


def pagina(titulo, descripcion, cuerpo, url, raiz=".."):
    menu = "".join(f'<a href="{raiz}/#{a}">{t}</a>' for a, t in [
        ("ia", "Formación IA"), ("cursos", "Cursos"), ("servicios", "Servicios"),
        ("nosotros", "Sobre nosotros"), ("contacto", "Contacto")])
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(titulo)}</title>
<meta name="description" content="{html.escape(descripcion)}">
<meta property="og:title" content="{html.escape(titulo)}"><meta property="og:description" content="{html.escape(descripcion)}">
<meta property="og:url" content="{url}"><meta property="og:type" content="article">
<link rel="icon" href="{raiz}/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600;700&display=swap">
<style>{CSS}</style></head><body>
{LOGO}
<header class="top"><div class="wrap">
<a class="brand" href="{raiz}/" aria-label="IPL, ir al inicio"><svg width="46" height="46" viewBox="0 0 120 120" aria-hidden="true" style="color:#fff"><use href="#rings"/><use href="#tri"/></svg>
<div><b>IPL</b><span>International Projects for Learning<br>&amp; Educational Coaching</span></div></a>
<nav class="menu" aria-label="Secciones">{menu}<a class="on" href="{raiz}/blog/">Blog</a></nav>
</div></header>
<main>{cuerpo}</main>
<footer><div class="wrap"><span>© {datetime.date.today().year} International Projects for Learning &amp; Educational Coaching</span>
<a href="{raiz}/blog/">Blog</a><a href="{raiz}/">Volver a la web</a></div></footer>
</body></html>
"""


def tarjeta(a, enlace, h="h2"):
    tags = "".join(f"<span>{html.escape(e)}</span>" for e in a["etiquetas"])
    return (f'<a class="card" href="{enlace}"><time datetime="{a["fecha"]}">{fecha_larga(a["fecha"])} · {a["min"]} min de lectura</time>'
            f'<{h}>{html.escape(a["titulo"])}</{h}><p>{html.escape(a["resumen"])}</p>'
            f'<div class="tags">{tags}</div><span class="mas">Leer artículo →</span></a>')


def main():
    hoy = datetime.date.today().isoformat()
    arts = sorted((leer(p) for p in SRC.glob("*.md")), key=lambda a: a["fecha"], reverse=True)
    arts = [a for a in arts if a["fecha"] <= hoy]  # los programados con fecha futura esperan
    OUT.mkdir(exist_ok=True)
    for a in arts:
        cuerpo = (f'<section class="hero"><div class="wrap"><div class="eyebrow">Blog IPL · {" · ".join(map(html.escape, a["etiquetas"][:2]))}</div>'
                  f'<h1>{html.escape(a["titulo"])}</h1><p>{html.escape(a["resumen"])}</p>'
                  f'<div class="meta">{fecha_larga(a["fecha"])} · {a["min"]} min de lectura</div></div></section>'
                  f'<div class="wrap"><article>{a["html"]}'
                  f'<div class="autora"><div><b>Sonina Darder</b><br>CEO de IPL · Apple Distinguished Educator · formadora de docentes en IA</div></div>'
                  f'<a class="volver" href="./">← Todos los artículos</a></article></div>')
        (OUT / f'{a["slug"]}.html').write_text(pagina(f'{a["titulo"]} · Blog IPL', a["resumen"], cuerpo, f'{WEB}blog/{a["slug"]}.html'), encoding="utf-8")
    lista = "".join(tarjeta(a, f'{a["slug"]}.html') for a in arts) or "<p>Muy pronto, el primer artículo.</p>"
    cuerpo = ('<section class="hero"><div class="wrap"><div class="eyebrow">Blog IPL</div>'
              '<h1>Inteligencia artificial en el aula, contada desde el aula</h1>'
              '<p>Cada semana, ideas prácticas para docentes y equipos directivos: IA en educación, evaluación, tecnología y metodologías que funcionan.</p></div></section>'
              f'<div class="wrap lista">{lista}</div>')
    (OUT / "index.html").write_text(pagina("Blog · IPL & Educational Coaching", "Ideas prácticas sobre inteligencia artificial en educación para docentes y colegios.", cuerpo, f"{WEB}blog/"), encoding="utf-8")

    # Portada: sección «Del blog» con los 3 últimos
    idx = RAIZ / "index.html"
    t = idx.read_text(encoding="utf-8")
    seccion = ('<!--BLOG:INICIO--><section class="band" id="blog"><div class="wrap">'
               '<div class="eyebrow">Blog</div><h2 style="margin:10px 0 28px">Ideas para docentes, cada semana</h2>'
               '<div class="blog-grid">' + "".join(tarjeta(a, f'blog/{a["slug"]}.html', "h3") for a in arts[:3]) + '</div>'
               '<p style="margin-top:26px"><a class="btn navy" href="blog/">Ver todos los artículos</a></p></div></section><!--BLOG:FIN-->')
    if "<!--BLOG:INICIO-->" in t:
        t = re.sub(r"<!--BLOG:INICIO-->.*?<!--BLOG:FIN-->", lambda m: seccion, t, flags=re.S)
    else:
        t = t.replace('<section class="band dark" id="contacto">', seccion + '\n  <section class="band dark" id="contacto">', 1)
    if 'href="blog/">Blog</a>' not in t.split("</nav>")[0]:
        t = t.replace('<a href="#contacto">Contacto</a>\n    </nav>', '<a href="blog/">Blog</a>\n      <a href="#contacto">Contacto</a>\n    </nav>', 1)
    if ".blog-grid" not in t:
        t = t.replace("</style>", """.blog-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
@media (max-width:960px){.blog-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media (max-width:620px){.blog-grid{grid-template-columns:1fr}}
.blog-grid .card{display:flex;flex-direction:column;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px;text-decoration:none;transition:transform .2s,box-shadow .2s}
.blog-grid .card:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(17,28,51,.12)}
.blog-grid time{font-size:13px;color:var(--muted)}.blog-grid p{margin:0;color:var(--muted);font-size:15.5px}
.blog-grid .mas{margin-top:auto;font-weight:700;color:var(--gold-ink);font-size:15px}
.blog-grid .tags{display:flex;flex-wrap:wrap;gap:6px}.blog-grid .tags span{font-size:12px;font-weight:600;border:1px solid var(--line);border-radius:999px;padding:2px 10px;color:var(--muted)}
</style>""", 1)
    idx.write_text(t, encoding="utf-8")
    print(f"{len(arts)} artículo(s) publicados")


if __name__ == "__main__":
    main()
