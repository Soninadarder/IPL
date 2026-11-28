#!/usr/bin/env python3
"""Generador de carruseles y reels de @ipl.iaeducacion (versión 28-11-2026, estilo «hecho a mano»).

Uso desde otro script:
    from carrusel import render, pantalla, doodle
    render([html1, html2, ...], "salida/", ancho=1080, alto=1350)

Cada pantalla es HTML libre dentro de un lienzo con textura de papel. Helpers:
  doodle.sub(color)      subrayado irregular (SVG)      doodle.circ(color)  círculo a mano
  doodle.flecha(color)   flecha curva                    <span class="fosfo">  marcador fosforito
  <div class="posit">    pósit                           <div class="cinta">  cinta adhesiva
  <span class="mano">    letra manuscrita (Caveat)
Las fuentes van incrustadas en base64 (no dependen de file://).
"""
import base64, pathlib, sys
from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).resolve().parent
FUENTES = AQUI / "fonts"


def _b64(nombre):
    p = next(FUENTES.rglob(nombre))
    return base64.b64encode(p.read_bytes()).decode()


def _css_fuentes():
    out = []
    for peso in (400, 500, 700):
        out.append(f"@font-face{{font-family:'SG';font-weight:{peso};src:url(data:font/woff2;base64,{_b64(f'space-grotesk-latin-{peso}-normal.woff2')}) format('woff2')}}")
        out.append(f"@font-face{{font-family:'Caveat';font-weight:{peso};src:url(data:font/woff2;base64,{_b64(f'caveat-latin-{peso}-normal.woff2')}) format('woff2')}}")
    return "\n".join(out)


PAPEL = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
         "<rect width='400' height='400' filter='url(%23n)'/></svg>")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:W;height:H;overflow:hidden}
.lienzo{position:relative;width:W;height:H;overflow:hidden;font-family:'SG',sans-serif;color:#1D2B4F;background:var(--bg,#F6EFE3)}
.lienzo::after{content:'';position:absolute;inset:0;background:url("PAPEL");opacity:.16;mix-blend-mode:multiply;pointer-events:none}
.lienzo::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.35),transparent 60%),radial-gradient(ellipse at 80% 90%,rgba(0,0,0,.07),transparent 55%);pointer-events:none}
.mano{font-family:'Caveat',cursive;font-weight:700}
.fosfo{background:linear-gradient(100deg,transparent 2%,rgba(255,214,0,.75) 4%,rgba(255,224,60,.6) 92%,transparent 97%);padding:0 .12em;border-radius:.2em .5em .3em .6em}
.fosfo.rosa{background:linear-gradient(100deg,transparent 2%,rgba(255,140,170,.6) 4%,rgba(255,160,180,.5) 92%,transparent 97%)}
.posit{position:absolute;background:#FFE680;box-shadow:0 14px 26px rgba(0,0,0,.18),0 2px 4px rgba(0,0,0,.1);padding:46px 44px}
.cinta{position:absolute;width:190px;height:54px;background:rgba(255,250,230,.62);box-shadow:0 1px 3px rgba(0,0,0,.12);border-left:3px dashed rgba(0,0,0,.05);border-right:3px dashed rgba(0,0,0,.05)}
.abs{position:absolute}
.marca{position:absolute;font-weight:700;font-size:30px;letter-spacing:.02em;opacity:.85}
.num{font-weight:700;line-height:.8}
svg{overflow:visible}
"""


class doodle:
    @staticmethod
    def sub(color="#D9734E", ancho=520, grosor=12):
        return (f'<svg width="{ancho}" height="40" viewBox="0 0 500 40" preserveAspectRatio="none">'
                f'<path d="M6 24 C 90 10, 170 34, 260 18 S 420 30, 494 14" fill="none" stroke="{color}" '
                f'stroke-width="{grosor}" stroke-linecap="round"/>'
                f'<path d="M40 34 C 140 26, 260 36, 430 28" fill="none" stroke="{color}" stroke-width="{grosor*0.45}" stroke-linecap="round" opacity=".7"/></svg>')

    @staticmethod
    def circ(color="#D9734E", w=300, h=150, grosor=7):
        return (f'<svg width="{w}" height="{h}" viewBox="0 0 300 150" preserveAspectRatio="none">'
                f'<path d="M160 12 C 60 6, 8 40, 14 80 C 20 128, 120 146, 200 136 C 280 126, 300 80, 280 46 C 262 16, 200 4, 120 16" '
                f'fill="none" stroke="{color}" stroke-width="{grosor}" stroke-linecap="round"/></svg>')

    @staticmethod
    def flecha(color="#1D2B4F", w=180, rot=0, grosor=7):
        return (f'<svg width="{w}" height="{w*0.7:.0f}" viewBox="0 0 180 126" style="transform:rotate({rot}deg)">'
                f'<path d="M10 20 C 60 0, 130 20, 150 96" fill="none" stroke="{color}" stroke-width="{grosor}" stroke-linecap="round"/>'
                f'<path d="M122 80 L 152 104 L 168 70" fill="none" stroke="{color}" stroke-width="{grosor}" stroke-linecap="round" stroke-linejoin="round"/></svg>')

    @staticmethod
    def estrella(color="#E8B04B", s=90):
        return (f'<svg width="{s}" height="{s}" viewBox="0 0 100 100"><path d="M50 6 L58 40 L94 42 L64 60 L76 94 L50 72 L22 94 L34 60 L6 42 L42 38 Z" '
                f'fill="none" stroke="{color}" stroke-width="6" stroke-linejoin="round"/></svg>')

    @staticmethod
    def garabato(color="#1D2B4F", w=160):
        return (f'<svg width="{w}" height="{w*0.4:.0f}" viewBox="0 0 160 64"><path d="M6 40 C 20 6, 34 6, 36 34 C 38 60, 56 58, 60 30 C 64 4, 84 6, 86 34 C 88 60, 108 58, 112 30 C 116 6, 136 8, 154 30" '
                f'fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round"/></svg>')


def pagina(cuerpo, ancho, alto, bg="#F6EFE3"):
    css = CSS.replace("W", f"{ancho}px").replace("H", f"{alto}px").replace("PAPEL", PAPEL)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{_css_fuentes()}{css}</style></head>"
            f"<body><div class='lienzo' style='--bg:{bg}'>{cuerpo}</div></body></html>")


def render(pantallas, salida, ancho=1080, alto=1350, formato="jpg", nombres=None):
    """pantallas: lista de (html_cuerpo, color_fondo). Devuelve las rutas creadas."""
    salida = pathlib.Path(salida); salida.mkdir(parents=True, exist_ok=True)
    rutas = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": ancho, "height": alto})
        for i, (cuerpo, bg) in enumerate(pantallas, 1):
            pag.set_content(pagina(cuerpo, ancho, alto, bg))
            pag.evaluate("document.fonts.ready")
            pag.wait_for_timeout(150)
            nombre = (nombres[i-1] if nombres else f"{i:02d}") + "." + formato
            r = salida / nombre
            if formato == "jpg":
                pag.screenshot(path=str(r), type="jpeg", quality=90)
            else:
                pag.screenshot(path=str(r))
            rutas.append(r)
        nav.close()
    return rutas


if __name__ == "__main__":
    print(__doc__); sys.exit(0)
