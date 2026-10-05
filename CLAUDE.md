# CLAUDE.md — curso-codex-18

Curso "Codex: os 18 conceitos essenciais" no formato `formato-curso-v2` (4 trilhas: 4 + 3 + 6 + 5 módulos × 6 tópicos). courseId `cx18`.

- Regras, mapa congelado e fatos/comandos permitidos: `context/SPEC.md`. Conteúdo de cada conceito: `context/CONTEUDO.md`.
- **Sem citar fontes** (vídeo, canal, autor): o curso é autoral. O `lint.py` barra os termos mais óbvios.
- Toda seção de tópico tem ≥1 SVG inline (o lint confere). Imagem de abertura por módulo: `scripts/gerar-imagens.py` (inemaimg local, flux2-klein, sem texto na cena; conferir a imagem, o flux às vezes escreve letras).
- As páginas são **montadas**: edite `context/corpos/*.html`, rode `python3 scripts/montar.py` e `python3 scripts/lint.py` (precisa `LINT OK`). Não edite `curso/**/*.html` nem `index.html` à mão.
- Navegador: `node scripts/checar-navegador.cjs http://127.0.0.1:PORTA` com servidor local numa porta livre.
- Sem API externa sem autorização explícita.
- Conta git: `inematds <inematds@gmail.com>`. Publicar = push; GitHub Pages serve da raiz (main).

## Self-learning

When I correct you, or you catch yourself making a mistake: before continuing, add the lesson as a one-line rule under ## Lessons, so it never happens again.

## Lessons

- flux2-klein escreve letras embaralhadas quando a cena tem placa, pergaminho ou livro: pedir só pictogramas ("pure icons, no signs, no labels") e conferir a imagem antes de usar.
- `gh repo create --push` logo após `git init` empurra `master`: rodar `git branch -M main` antes do primeiro push (senão o Pages recusa).
