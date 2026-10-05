#!/usr/bin/env python3
"""Gera a imagem de abertura de cada módulo (1536×640) no inemaimg local (flux2-klein).
Uso: python3 scripts/gerar-imagens.py [1-1 2-3 ...]   (sem argumento: todas que faltam)
Só fala com http://localhost:8000 (servidor local, sem API externa)."""
import base64, json, sys, urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTILO = ('flat vector editorial illustration, dark navy background, glowing {cor} and cyan neon accents, '
          'subtle futuristic grid, clean shapes, cinematic wide composition, no text, no letters, no words, no logos')
COR = {'1': 'emerald green', '2': 'electric blue', '3': 'violet purple', '4': 'warm amber'}
CENAS = {
    '1-1': 'a friendly woman in her forties at a desk with a laptop, a big glowing folder floating beside her filled with small documents, notes and photos, the folder emits a soft light connecting to the laptop',
    '1-2': 'a small friendly robot in a cozy home office arranging large glowing pictogram tiles on a wall board: a person silhouette tile, a gear tile, a shield tile, a map pin tile, tiles connected by glowing lines like a map, pure icons, no signs, no labels',
    '1-3': 'a circular loop of three glowing stations: a thinking brain, a toolbox with wrench and magnifier, and a speech bubble, a small robot running around the loop',
    '1-4': 'a small determined robot climbing stairs toward a glowing target flag at the top, obstacles on the way that it walks around, sense of persistence',
    '2-1': 'split scene: on the left a home computer with a house icon glow, on the right a cloud data center, in the middle a person on a walk holding a smartphone connected to both by light beams',
    '2-2': 'a glowing tree trunk splitting into two branches, on one branch a small workshop testing an experiment, the main trunk stays intact and calm, later the branches merge again',
    '2-3': 'an open drawer cabinet with labeled-free compartments, gears and toggle switches inside, one small drawer for a project and a bigger one for the user, tidy and organized',
    '3-1': 'three different engines side by side on pedestals: a huge powerful glowing engine, a medium reliable engine, a small fast light engine, with fuel gauges',
    '3-2': 'a mixing console with sliders going from low to ultra, a speedometer with a lightning bolt for fast mode, a battery gauge draining faster at high settings',
    '3-3': 'a traffic light with three states guarding a door, a small robot waiting politely for green, a padlock and a key nearby',
    '3-4': 'a recipe book open on a kitchen counter with pancakes on a plate, the recipe pages glow and a small robot chef follows the steps, notes being corrected on the page',
    '3-5': 'a travel suitcase opening to reveal neatly organized skill cards and folders, two different robot assistants sharing the same suitcase',
    '3-6': 'a central hub with many puzzle pieces plugging into it, each piece representing a different app like mail envelope, calendar, cloud drive, chat bubble, design palette',
    '4-1': 'a small robot sitting in front of a big browser window, clicking and typing on a website, eye icon showing it can see the screen, login key saved on a keychain',
    '4-2': 'a rocket launching from a small laptop screen into a globe with many people viewing a website, a padlock and an analytics chart floating nearby',
    '4-3': 'a queen bee robot at the center sending several small worker bee robots in different directions to gather information, each returning with a glowing note',
    '4-4': 'a large wall clock and calendar with a small robot working autonomously at night at a desk, moon outside the window, tasks being checked off',
    '4-5': 'a person speaking into a microphone with sound waves that turn into many glowing threads connecting to several screens where robots are working',
}


def gerar(mid):
    t = mid.split('-')[0]
    saida = RAIZ / 'curso' / f'trilha{t}' / 'assets' / 'img' / f'modulo-{mid}.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    corpo = {'model': 'flux2-klein', 'prompt': CENAS[mid] + ', ' + ESTILO.format(cor=COR[t]),
             'width': 1536, 'height': 640, 'steps': 4, 'guidance_scale': 1.0, 'seed': 1800 + int(mid.replace('-', ''))}
    req = urllib.request.Request('http://localhost:8000/generate', data=json.dumps(corpo).encode(),
                                 headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=600) as r:
        img = json.load(r)['image']
    saida.write_bytes(base64.b64decode(img.split(',')[-1]))
    print('ok', saida.relative_to(RAIZ))


if __name__ == '__main__':
    alvos = sys.argv[1:] or [m for m in CENAS if not (RAIZ / 'curso' / f'trilha{m[0]}' / 'assets' / 'img' / f'modulo-{m}.png').exists()]
    for m in alvos:
        gerar(m)
