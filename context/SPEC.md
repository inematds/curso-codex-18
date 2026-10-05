# SPEC — Codex: os 18 conceitos essenciais (formato-curso-v2)

Curso INEMA.CLUB (aberto e gratuito). Título exato: **Codex: os 18 conceitos essenciais**. courseId = `cx18`.
Skill de formato: `~/.claude/skills/formato-curso-v2/` (erros críticos #1–#31 valem).
Modelos congelados para copiar a estrutura: `~/projetos/curso-agent-runtime/context/corpos/modulo-1-1.html` (módulo) e `.../trilha1.html` (index de trilha). Copiar a ESTRUTURA e as classes, nunca o conteúdo.

## REGRA DURA — sem fontes

- **Não citar nenhuma fonte**: nenhum vídeo, canal, autor, criador, post, "segundo fulano", "num vídeo que circulou". Nenhum link para YouTube. O curso é autoral.
- Não citar nomes de projetos de terceiros (ex.: nada de "Herk", "Hyperframes", "trading challenge").
- Exemplos usam só as personagens abaixo.

## Público e tom

- Comunidade INEMA.CLUB, 30+, já usa ChatGPT/Claude no navegador, **nunca usou o Codex**, não é programador. Cada termo técnico é definido na 1ª vez (box "🆕 Novo aqui?").
- Tom: direto, frases curtas, parágrafos de 2–4 linhas, sem coachzinho, português correto com acentos. Imperativo nos títulos dos tópicos.
- Personagens fixos:
  - **Paula, 45, consultora de RH**, trabalha sozinha. O projeto dela no Codex é a pasta `paula-escritorio` (clientes, propostas, modelos de e-mail, posts do LinkedIn).
  - **Rui, 52, dono de uma loja de materiais de construção**. Projeto `loja-rui` (planilha de estoque em CSV, catálogo, promoções da semana, site simples da loja).

## Tese (atravessa o curso)

O Codex deixa de ser "um chat" quando você dá a ele **uma pasta (projeto), regras (AGENTS.md), receitas (skills) e conexões (plugins)**. A partir daí ele trabalha num **ciclo** (pensa → usa ferramenta → responde) e você escolhe **quanto ele pode fazer sozinho** (permissões) e **quanto gastar** (modelo + esforço). Os 18 conceitos são as peças desse sistema, em 4 partes.

## Vocabulário fixo (um nome por conceito)

- **projeto** = a pasta aberta no Codex · **AGENTS.md** = regras da casa · **ciclo do agente** = pensar → agir (ferramenta) → responder, repetindo
- **harness** = o programa que dá ferramentas e o ciclo ao modelo (o Codex é um harness)
- **objetivo** = o que se passa no `/goal` · **local** = só na sua máquina · **nuvem** = num computador da OpenAI
- **worktree** = cópia de trabalho paralela do projeto · **`.codex/`** = configurações (projeto ou usuário) · **`.agents/`** = skills (projeto ou usuário)
- **skill** = receita reutilizável (`SKILL.md`) · **plugin** = conexão pronta com um aplicativo · **subagente** = ajudante que o agente principal dispara
- **cota** = o limite semanal da assinatura (não é dólar) · **token** ≈ 4 caracteres ou ¾ de palavra

## FATOS VERIFICADOS (Codex CLI 0.159.2 nesta máquina, 2026-10-05) — só isto entra como comando

| Fato / comando (verbatim) | Uso no curso |
|---|---|
| `codex` (abre na pasta atual) · `codex "pedido"` | abrir um projeto |
| `codex exec "pedido"` | rodar sem tela (sem interação) |
| `codex -C <pasta>` | usar outra pasta como raiz |
| `codex --worktree` | abrir a sessão numa worktree nova gerenciada |
| `codex -m gpt-6-astra` · `codex -m gpt-6-luna` | escolher modelo ao abrir |
| `codex -c model_reasoning_effort="high"` | mudar o esforço por uma sessão |
| `codex -s read-only` · `-s workspace-write` · `-s danger-full-access` | sandbox: só ler · editar na pasta · acesso total |
| `codex -a on-request` · `-a never` | quando pedir aprovação |
| `codex --approve-for-me` | aprovações passam por revisão automática (com sandbox workspace-write) |
| `codex resume` · `codex resume --last` | retomar conversa |
| `codex mcp list` · `codex mcp add <nome> -- <comando>` | conexões MCP |
| `codex plugin list` · `codex plugin add <nome>` · `codex plugin remove <nome>` | plugins pelo terminal |
| `codex doctor` | diagnóstico da instalação |
| `codex login` | entrar com a conta ChatGPT (assinatura) |
| `~/.codex/config.toml` com `model = "gpt-6-astra"` e `model_reasoning_effort = "medium"` | config global |
| Modelos no catálogo: **GPT-6-Astra** (mais forte, mais cota), **GPT-6.1-Sol** (o "cavalo de trabalho" do dia a dia), **GPT-6-Luna** (rápido e barato, tarefas fáceis); geração anterior: GPT-5.6-Sol/Terra/Luna | módulo 3.1 |
| Esforço: `low`, `medium`, `high`, `xhigh`, `max`, `ultra` (ultra = raciocínio máximo com delegação automática de tarefas; Luna vai até `max`) | módulo 3.2 |
| Modo rápido ("Fast"): **2× mais velocidade, mais consumo de cota** | módulo 3.2 |
| Recursos estáveis: metas (`/goal`), modo rápido, uso de navegador | módulos 1.4, 3.2, 4.1 |
| App desktop: projetos na barra lateral, seletor de modelo/esforço/permissão embaixo da caixa de mensagem, Plugins, navegador embutido, Sites, Agendadas, modo de voz, acesso remoto pelo app do ChatGPT no celular | descrever sem prometer o nome exato do botão: "o nome do botão pode mudar entre versões" |
| Permissões no app: **Pedir aprovação** (pergunta antes de editar fora da pasta e de usar a internet) · **Aprovar por mim** (só pergunta quando a ação parece arriscada: apagar, chamadas externas) · **Acesso total** (não pergunta nada) | módulo 3.3 |

**Proibido:** inventar comando, flag, preço em dólar ou saída de terminal. Preço de API: só dizer que a API cobra por milhão de tokens, que tokens de saída custam mais que os de entrada, que o modelo mais forte custa mais, e que **assinatura sai muito mais barata que API para uso pessoal**. Prompt copiável é sempre um **pedido em português para colar no Codex** (isso não tem risco de ser inventado). Comando de terminal só da tabela acima.

## Ilustração (pedido do usuário)

- **Todo tópico tem ≥1 ilustração SVG inline** (6 tópicos = ≥6 SVGs por módulo), no estilo de `SVG-FUTURISTA.md`: cor da trilha + ciano `#38bdf8`, grid, glow, `role="img"` + `aria-label` que descreve, `class="w-full h-auto"`, seguido de `<p class="text-sm text-neutral-400 mb-6"><strong class="text-neutral-300">Como ler o desenho:</strong> …</p>`.
- IDs de `<pattern>/<filter>/<marker>` únicos na página: prefixo `m<T><M><letra>-` (ex.: `m31a-grid`, `m31b-glow`).
- Variar o tipo de desenho: ciclo, fluxo, comparação lado a lado, pasta/árvore de arquivos, mock de tela do app (janela com barra lateral e caixa de mensagem), escada, fan-out, linha do tempo, painel de controle (sliders), etc. Nada de desenho repetido.
- Além dos SVGs, cada módulo tem uma imagem de abertura em `curso/trilhaN/assets/img/modulo-N-M.png` (gerada à parte pelo orquestrador; o autor só coloca a tag, ver abaixo).

Tag da imagem de abertura (logo depois do `</header>`, antes do grid principal):
```html
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-10">
    <figure class="rounded-2xl overflow-hidden border border-<cor>-500/30">
      <img src="assets/img/modulo-N-M.png" alt="<descrição do que a cena mostra e o que ensina>" class="w-full h-auto" loading="lazy" width="1536" height="640">
    </figure>
  </div>
```

## Estrutura de cada módulo (copiar do modelo congelado)

`<!--TITLE: título -->` na 1ª linha · breadcrumb · header com `data-inema-module`/`-track`, 4 stats, meter · figura de abertura · `<main>` com 6 `<section id="topico-N" data-inema-topic="modulo-T-M#topico-N">` (h2 `text-2xl font-bold flex-1` com o título EXATO do mapa, botão dúvida, parágrafos com `data-inema-block="mT-M-tN-pK"`, ≥1 SVG, legenda, componentes variados, marcar-lido) · resumo · aside TOC · `<!--CHECKS-->` com `INEMA.registerCheck` do teste rápido.
Profundidade: 500–850 linhas por arquivo de corpo montado; ≥2 grids ✓/✗, ≥1 timeline (passos numerados), ≥2 tip boxes, ≥1 code box "copia e cola" com **Objetivo / bloco / Como verificar** (rótulo literal "Como verificar"), ≥1 "🆕 Novo aqui?", 1 teste rápido de 3 opções.
Último módulo de cada trilha: botão final aponta para a trilha seguinte (`../trilha<N+1>/index.html`); o 4.5 aponta para `../../index.html`.

## MAPA CONGELADO (títulos exatos dos h2)

### Trilha 1 — Fundamentos (emerald)
- **1.1 [Projetos: a pasta que lembra de você]** 🗂️
  1. Entenda o problema do chat que esquece
  2. Veja que um projeto é só uma pasta
  3. Abra sua primeira pasta no Codex
  4. Organize a pasta para o Codex achar tudo
  5. Peça um resumo do que vocês já fizeram
  6. Evite os erros comuns com projetos
- **1.2 [AGENTS.md: as regras da casa]** 📜
  1. Descubra o que é um arquivo .md
  2. Entenda quando o Codex lê o AGENTS.md
  3. Escreva quem você é e o que o agente faz
  4. Monte o mapa de rotas do projeto
  5. Use um AGENTS.md por projeto
  6. Revise e melhore suas regras
- **1.3 [O ciclo do agente]** 🔄
  1. Entenda o que é um harness
  2. Siga o ciclo pensar, agir, responder
  3. Abra o registro do que ele fez
  4. Aprenda olhando o agente trabalhar
  5. Diferencie regras de memórias
  6. Faça um pedido e acompanhe o ciclo
- **1.4 [/goal: um objetivo até o fim]** 🎯
  1. Entenda o que muda com um objetivo
  2. Escreva um objetivo verificável
  3. Use objetivos subjetivos com cuidado
  4. Rode seu primeiro /goal
  5. Saia do caminho sem perder o controle
  6. Saiba quando não usar /goal

### Trilha 2 — Ambientes (blue)
- **2.1 [Local, nuvem e celular]** ☁️
  1. Entenda o que é local
  2. Desvende o localhost
  3. Compare tarefa local e tarefa na nuvem
  4. Controle o Codex pelo celular
  5. Escolha onde rodar cada tarefa
  6. Evite o link que só abre na sua máquina
- **2.2 [Worktrees: cópias para testar sem medo]** 🌿
  1. Entenda o risco de mexer no original
  2. Veja o que é uma worktree
  3. Conheça branch e main sem medo
  4. Crie uma worktree no Codex
  5. Junte o resultado de volta
  6. Saiba quando você não precisa disso
- **2.3 [A pasta .codex: configurações]** ⚙️
  1. Encontre a pasta .codex
  2. Separe projeto de usuário
  3. Leia o config.toml sem medo
  4. Saiba o que fica na pasta global
  5. Peça ao Codex para ajustar a configuração
  6. Proteja o que não deve sair da máquina

### Trilha 3 — Controle e personalização (purple)
- **3.1 [Modelos: força e custo]** 🧠
  1. Entenda que cada modelo tem força e preço
  2. Conheça a família de modelos do Codex
  3. Entenda tokens de entrada e de saída
  4. Diferencie assinatura de API
  5. Troque de modelo no meio da conversa
  6. Escolha o modelo pela tarefa
- **3.2 [Esforço e modo rápido]** 🎚️
  1. Entenda o que é nível de esforço
  2. Conheça a escada de low a ultra
  3. Veja por que mais esforço gasta mais cota
  4. Use o modo rápido com consciência
  5. Combine modelo e esforço
  6. Monte sua tabela pessoal
- **3.3 [Permissões: quanto ele faz sozinho]** 🚦
  1. Entenda por que o agente pede licença
  2. Conheça os três modos de permissão
  3. Comece pedindo aprovação para tudo
  4. Passe para a aprovação automática
  5. Saiba quando usar acesso total
  6. Bloqueie ações específicas na configuração
- **3.4 [Skills: receitas reutilizáveis]** 🍳
  1. Entenda a skill como receita
  2. Abra um SKILL.md por dentro
  3. Crie sua primeira skill
  4. Chame a skill por texto ou por barra
  5. Melhore a skill com feedback
  6. Encadeie skills num fluxo maior
- **3.5 [A pasta .agents e a vinda do Claude Code]** 🧳
  1. Encontre a pasta .agents
  2. Separe skills do projeto e skills globais
  3. Faça a skill usar outros arquivos
  4. Traga seu projeto do Claude Code
  5. Mantenha um projeto que serve a qualquer agente
  6. Organize sua biblioteca de skills
- **3.6 [Plugins: conecte seus aplicativos]** 🧩
  1. Entenda o que é um plugin
  2. Conecte seu primeiro aplicativo
  3. Busque o plugin que você precisa
  4. Use o plugin numa conversa
  5. Saiba o que fazer quando não há plugin
  6. Cuide da segurança das conexões

### Trilha 4 — Ferramentas e escala (amber)
- **4.1 [Navegador: o Codex usa sites por você]** 🌐
  1. Conheça o navegador dentro do Codex
  2. Faça login uma vez e reutilize
  3. Peça uma tarefa num site sem integração
  4. Entenda como o agente enxerga a tela
  5. Escolha entre plugin, API e navegador
  6. Use o navegador com regras
- **4.2 [Sites: do localhost para o mundo]** 🚀
  1. Entenda o que é publicar um site
  2. Transforme um localhost em site
  3. Decida quem pode abrir
  4. Acompanhe as visitas
  5. Ligue um domínio e um banco de dados
  6. Publique com responsabilidade
- **4.3 [Subagentes: delegue em paralelo]** 🐝
  1. Entenda o que é delegar
  2. Veja o agente principal e os ajudantes
  3. Use um modelo mais barato nos ajudantes
  4. Acompanhe cada subagente
  5. Junte os resultados
  6. Saiba quando dividir e quando não
- **4.4 [Tarefas agendadas: o Codex no piloto]** ⏰
  1. Entenda o que é uma tarefa agendada
  2. Veja que a tarefa é um pedido com horário
  3. Crie sua primeira tarefa
  4. Escolha projeto, conversa e frequência
  5. Peça ao Codex para criar a tarefa
  6. Coloque limites no que roda sozinho
- **4.5 [Modo de voz: tudo junto]** 🎙️
  1. Entenda o modo de voz
  2. Comece uma conversa por voz
  3. Mande trabalho para outras conversas
  4. Use a voz no celular
  5. Veja os 18 conceitos num pedido só
  6. Monte sua rotina com o Codex
