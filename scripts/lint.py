#!/usr/bin/env python3
"""Lint do curso v2 (PT): manifesto idêntico, tópicos = manifesto, títulos h2 = SPEC, linhas, SVG,
ids de SVG únicos, Mapa da trilha, Ver Completo, links relativos, comandos fora da lista.
Uso: python3 scripts/lint.py [arquivo ...]   (sem argumento: todas as páginas PT)"""
import re, sys, json, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from montar import TRILHAS
NMODS = {n: len(m) for n, _, _, m in TRILHAS}

RAIZ = Path(__file__).resolve().parent.parent
spec = (RAIZ / 'context' / 'SPEC.md').read_text(encoding='utf-8')

# títulos dos tópicos por módulo, lidos do mapa congelado da SPEC
TOPICOS = {}
atual = None
for linha in spec.split('\n'):
    m = re.match(r'- \*\*(\d)\.(\d) \[', linha)
    if m:
        atual = f'{m.group(1)}-{m.group(2)}'; TOPICOS[atual] = []; continue
    m = re.match(r'\s+\d\. (.+)$', linha)
    if m and atual and len(TOPICOS[atual]) < 6:
        TOPICOS[atual].append(m.group(1).strip())

falhas = []
FONTES = re.compile(r'youtube|youtu\.be|num vídeo|nesse vídeo|neste vídeo|segundo o autor|canal de|criador de conteúdo|vídeos que circularam', re.I)
def falha(f, msg): falhas.append(f'{f}: {msg}')

paginas = [Path(a).resolve() for a in sys.argv[1:]] or ([RAIZ / 'index.html'] + sorted((RAIZ / 'curso').glob('trilha*/*.html')))
ref_manifest = None
for p in paginas:
    txt = p.read_text(encoding='utf-8')
    rel = p.relative_to(RAIZ)
    m = re.search(r'data-inema-manifest[^>]*>\s*(.*?)\s*</script>', txt, re.S)
    if not m: falha(rel, 'sem manifesto'); continue
    ref_manifest = ref_manifest or m.group(1)
    if m.group(1) != ref_manifest: falha(rel, 'manifesto difere')
    if 'https://inema.pro' not in txt: falha(rel, 'sem PRO')
    if not re.search(r'<a [^>]*text-sky-400[^>]*>INEMA.CLUB</a>', txt): falha(rel, 'sem INEMA.CLUB')
    if txt.find('ANTI-FOUC') > txt.find('cdn.tailwindcss.com'): falha(rel, 'anti-FOUC fora de ordem')
    if re.search(r'justify-center space-x', txt): falha(rel, 'justify-center em botões')
    ids = re.findall(r'<(?:pattern|filter|marker|linearGradient|radialGradient)[^>]*\sid="([^"]+)"', txt)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: falha(rel, f'ids de SVG repetidos: {sorted(dup)[:5]}')
    # links relativos
    for h in set(re.findall(r'(?:href|src)="([^"#:?]+\.(?:html|css|js|png))', txt)):
        if not os.environ.get('LINT_SEM_LINKS') and not (p.parent / h).resolve().exists(): falha(rel, f'link quebrado -> {h}')
    mod = re.match(r'modulo-(\d-\d)\.html', p.name)
    if mod:
        mid = mod.group(1)
        n = len(re.findall(rf'data-inema-topic="modulo-{mid}#topico-\d"', txt))
        linhas = txt.count('\n')
        svg = len(re.findall(r'<svg[^>]*role="img"', txt))
        h2 = re.findall(r'<h2 class="text-2xl font-bold flex-1">(.*?)</h2>', txt)
        esperado = TOPICOS.get(mid, [])
        print(f'{str(rel):34} linhas={linhas:<4} topicos={n} svg={svg} copyrun={txt.count("Como verificar")} check={txt.count("registerCheck(")}')
        if n != 6: falha(rel, f'{n} tópicos (precisa 6)')
        if not 500 <= linhas <= 850: falha(rel, f'{linhas} linhas fora de 500-850')
        secs = re.split(r'<section id="topico-\d"', txt)[1:]
        sem = [i + 1 for i, sec in enumerate(secs) if not re.search(r'<svg[^>]*role="img"', sec.split('</section>')[0])]
        if sem: falha(rel, f'tópicos sem SVG: {sem}')
        if FONTES.search(txt): falha(rel, f'cita fonte: {FONTES.search(txt).group(0)}')
        if '$' in re.sub(r'<script.*?</script>', '', txt, flags=re.S).replace('$PWD', ''): falha(rel, 'valor em dólar?')
        if [re.sub('<[^>]+>', '', x) for x in h2] != esperado: falha(rel, f'h2 ≠ SPEC: {h2}')
        if 'registerCheck(' not in txt: falha(rel, 'sem checagem')
        if 'data-inema-toc' not in txt: falha(rel, 'sem TOC')
    elif p.name == 'index.html' and 'trilha' in str(p.parent):
        tn = p.parent.name[-1]
        mods = len([d for d in re.findall(r'<div [^>]*data-inema-module="\d-\d"[^>]*>', txt) if 'id="modulo-' in d])
        vc = txt.count('>Ver Completo<'); tp = txt.count('class="topic-item"')
        print(f'{str(rel):34} modulos={mods} ver_completo={vc} topicos={tp} svg={txt.count(chr(114)+"ole=\"img\"")}')
        if '>Mapa da trilha<' not in txt: falha(rel, 'sem Mapa da trilha')
        k = NMODS[tn]
        if mods != k or vc != k or tp != 6 * k: falha(rel, f'precisa {k} módulos, {k} Ver Completo, {6*k} tópicos')
        for mid, tits in TOPICOS.items():
            if mid.startswith(tn):
                for t in tits:
                    if f'<span class="font-medium">{t}</span>' not in txt: falha(rel, f'tópico ausente/diferente: {mid} "{t}"')

for f in falhas: print('FALHA', f)
print('LINT OK' if not falhas else f'LINT FALHOU ({len(falhas)})')
sys.exit(1 if falhas else 0)
