# Oficina de IA: memória do projeto

Este arquivo guarda o contexto do projeto para continuar o trabalho no Claude Code. Escreva e responda sempre em **português**.

## Objetivo

Preparar uma oficina (workshop) de IA para iniciantes, com uma apresentação em slides. O responsável é o Daniel (GitHub `robotizando`), que prepara a oficina em parceria com outra pessoa. A primeira versão da programação saiu de uma conversa gravada entre os dois sobre a premissa da oficina (2026-09-28). Em 2026-10-01 entrou uma segunda fonte: um áudio do Daniel para a Eliane defendendo que oficina de agentes de IA seja de **alfabetização, não de construção** (hype × maturidade, números do Gartner, processo antes de agente, falhas, segurança, custo de execução, caminho de estudo).

## Público e tom (decidido)

- **Pessoa-modelo:** esperta e desenrolada, mas usa o celular de forma limitada (WhatsApp, Instagram, joguinhos). Já ouviu falar de IA e provavelmente já usou o ChatGPT, mas não sabe como funciona.
- **Empreendedor:** tem ou quer ter um negócio próprio.
- **Só celular:** não tem computador. Todo exercício precisa rodar no telefone.
- **Tom:** lúdico e simples, **sem matemática** (nada de perceptron, forward, backpropagation, sigmoide). Neurônios viram "bolinhas com um número dentro". Crítico e honesto ("jogar a real") sobre limites, custos, tokens pouco transparentes e promessas exageradas (agentes, vídeo).
- Ferramentas: ChatGPT para o dia a dia e textos rápidos; Claude para o que é complexo e visual (Projetos, Claude Design). Economizar os tokens da conta grátis do Claude.
- **Exceção à regra da matemática (pedido do Daniel em 2026-10-02):** os slides `perceptron`, `sigmoide`, `backprop` e `dois-perceptrons`, logo depois do `funciona`, mostram a conta (soma ponderada, sigmoide, regressão logística, perda logística, descida do gradiente e backprop) com o exemplo do bolo. São para o Daniel explicar; o resto da oficina continua sem matemática.
- **Alfabetização, não construção:** ninguém sai com agente pronto. Sobre agentes, mostrar mais os problemas (processo, falhas, segurança, custo) do que as promessas.
- Mapa das IAs em três slides (decidido em 2026-10-02): porta de entrada curta ("comece por estas": ChatGPT, Claude, Gemini, Meta AI), mapa completo por categoria e semáforo de maturidade. A lista pode ser grande, desde que a porta de entrada venha antes.

## Onde está cada coisa

| Caminho | O que é |
|---|---|
| `oficina-ia/programacao.md` | Programação em 10 blocos, com o 9 dividido em 9a e 9b (~3h25 com intervalo), com os pontos em aberto no fim. É a fonte de verdade do conteúdo. |
| `oficina-ia/apresentacao/deck.json` | Ordem dos 72 slides, seções e fontes. |
| `oficina-ia/apresentacao/slides/*.html` | Um fragmento HTML por slide (`<section>` com notas do apresentador em `<aside>`). |
| `oficina-ia/apresentacao/player/` | Player local que mostra esses slides sem o claude.ai e sem internet (fontes e ícones guardados no repositório). |
| `oficina-ia/apresentacao/apresentar.sh` | Sobe um servidor local (servindo `oficina-ia/` inteira) e abre o player no navegador. |
| `oficina-ia/apresentacao/gerar-pdf.sh` | Gera `oficina-ia/apresentacao/pdf/oficina-ia.pdf`, um slide por página, a partir do player local (Chrome sem janela). |
| `oficina-ia/programas/` | Programas de demonstração: `mlp_visualizer.html`, `llm_visualizer.html` e `tokens_visualizer.html` (do Daniel) e `bolinhas.html` (versão sem matemática feita pelo Claude). `tela-cheia.html?p=<programa>.html` mostra um deles em tela cheia sem alterar o arquivo. |
| `oficina-ia/exemplos/` | Arquivos para os exercícios. `faturamento-laboratorio.pdf` é o PDF **fictício** do exercício 1 (laboratório inventado, 26 lançamentos de setembro/2026, entradas e saídas misturadas), gerado por `gerar_faturamento.py` (reportlab). Substitui o PDF real enquanto ele não chega. `faturas-clientes.pdf` é o segundo exemplo (slide `exercicio1-faturas`): 25 páginas, uma fatura de cliente fictício por página, laboratório veterinário, gerado por `gerar_faturas.py` com sorteio de semente fixa (25 faturas, 90 itens, soma R$ 29.978,00). Os prompts testados pelo Daniel ficam nas notas dos dois slides. |

**Versão viva da apresentação:** https://claude.ai/artifact/H3THoFiSSpR9ftCQrV9w39 (Artifact do tipo Slides no claude.ai; lá dá para apresentar, editar e exportar para PowerPoint ou PDF).

- Os HTML do repositório são a fonte desse Artifact, **não páginas independentes**: usam elementos do tipo Slides (`<x-icon>`, `<x-shape>`) e não abrem sozinhos no navegador.
- Edições feitas na página do Artifact não voltam sozinhas para o repositório, e edições aqui não publicam o Artifact. Em 2026-10-01 os arquivos do repositório estavam idênticos ao Artifact publicado antes da inclusão do áudio da Eliane; depois disso o repositório ficou à frente (slides `agente-processo` e `seguranca` novos e outros ajustados), até alguém republicar. Antes de mexer, confirme qual lado está mais novo.

## Apresentar localmente

- Rode `oficina-ia/apresentacao/apresentar.sh`: ele abre `http://127.0.0.1:8765/apresentacao/player/` (ou a próxima porta livre). Ctrl+C no terminal encerra. Sem o script: `python3 -m http.server` dentro de `oficina-ia/` e abrir `/apresentacao/player/`. Abrir o `index.html` direto do arquivo não funciona.
- Atalhos: → / ← (ou passador de slides), número + Enter para pular, F tela cheia, N notas do apresentador (segunda janela, com cronômetro e próximo slide), B tela preta, S liga/desliga o som, R recarrega depois de editar um slide.
- Som: `data-som="alerta"` na `<section>` toca uma sirene gerada pelo player (sem arquivo) ao chegar no slide; outro valor é tratado como arquivo de áudio relativo a `apresentacao/` (ex.: `data-som="sons/buzina.mp3"`). Usado em `alerta-perceptron`, `alerta-matematica` e `alerta-atencao`. O navegador só toca depois de um clique ou tecla na janela dos slides; o Artifact do claude.ai ignora o atributo.
- O player é nosso, não o motor do claude.ai: cobre o que os slides usam hoje (tela 1920×1080, estilos inline, `x-icon`, `x-shape`, transição fade, `<aside>`, `hidden`). Os ícones são do Phosphor (MIT), parecidos mas não idênticos aos do claude.ai. `x-connector`, `x-embed`, animações `data-build-*` e a transição `magic` não estão implementados. Se um slide novo usar um desses, conferir no player antes de apresentar.
- Links (`<a href>`) nos slides são relativos à pasta `apresentacao/` e abrem em outra aba. Os slides `bolinhas-demo`, `mlp-demo`, `token-demo` e `llm-demo` usam isso para abrir os programas de `programas/` via `tela-cheia.html` (o navegador exige um toque na aba nova para entrar em tela cheia; Ctrl+W volta aos slides). Esses links só funcionam no player local: os programas não estão publicados no Artifact do claude.ai.
- Vídeo: `<video src="../exemplos/arquivo.mp4" controls>` no slide (caminho relativo a `apresentacao/`, como os links). Clicar no vídeo toca e pausa sem trocar de slide, e ele para sozinho ao sair do slide. Usado em `video-exemplos`, com `exemplos/exemplo-video1.mp4` (10 s) e `exemplo-video2.mp4` (30 s), postos pelo Daniel. Só funciona no player local: os vídeos não estão publicados no Artifact.
- Para tirar um slide da apresentação (por exemplo `bolinhas-demo`), coloque `hidden` na `<section>`: o player pula.
- PDF: rode `oficina-ia/apresentacao/gerar-pdf.sh [arquivo-de-saida]` depois de editar os slides. Ele abre o player em modo `?imprimir` (todos os slides, um por página de 1920 × 1080) no Google Chrome ou Chromium sem janela. Slides com `hidden` ficam de fora, as notas do apresentador não entram e cada vídeo vira um quadro parado (o de 1 s, tirado com o ffmpeg; sem ffmpeg, um retângulo com um play). Links para os programas não funcionam no PDF. O PDF não se atualiza sozinho.

## Ordem dos slides

capa, publico, roteiro, abertura, funciona, alerta-perceptron, perceptron, sigmoide, backprop, dois-perceptrons, bolinhas-demo, mlp-demo, parametros, rede-video, previsao, token, token-porque, alerta-matematica, embedding, token-demo, alerta-atencao, atencao-artigo, atencao-exemplo, atencao-conta, llm-demo, nuvem-fluxo, chatgpt-ao-vivo, ideias, ideia-atendimento, ideia-divulgacao, ideia-contas, ideia-documentos, nuvem-recursos, ia-imagem, ia-transcricao, ia-locucao, ia-visao, mapa, mapa-lista, mapa-maturidade, projetos, prompt, harness-o-que-e, harness-ferramentas, harness-mcp, harness-oportunidade, harness-negocios, contexto-janela, contexto-limites, harness-skills, harness-resumo, exercicio1, exercicio1-faturas, intervalo, exercicio2, imagem-custo, video, video-desafio, video-prompt, video-exemplos, video-evolucao, video-evolucao-player, agente, agente-familias, agente-n8n, agente-openclaw, agente-processo, seguranca, agente-real, agente-stack, encerramento, obrigado.

O slide de bastidores (`pendencias`) foi removido em 2026-10-03; os pontos em aberto ficam só neste arquivo e na `programacao.md`.

## Visual (decidido)

- Fontes: **Fredoka** (títulos) + **Nunito Sans** (texto), via Google Fonts.
- Cores: creme `#FFF8EE` (fundo), azul-marinho `#1F2A44`, laranja `#F28C28`; laranja escuro `#9A4508` para rótulos e pendências; cards claros `#FFFDF9` com borda `#EFD9B8`.
- Pontos em aberto aparecem como pílulas tracejadas "Em aberto: ...".

## Pontos em aberto

- **Duração total e formato:** quantas horas, presencial, quantas pessoas, se tem Wi-Fi. Os tempos da programação são estimativas.
- **Exemplo do faturamento (exercício 1):** conseguir o PDF real de um laboratório e anonimizar os dados.
- **Link de afiliado do Claude (decidido em 2026-10-03):** não usar. O `encerramento` não tem link para assinar o Claude.
- **Preços e energia (slide `nuvem-recursos`):** conferir o preço das GPUs e servidores e os números de consumo perto da data.
- **Números do Gartner:** achar fonte e ano dos 17% de empresas implantando agentes e dos 80% de falha (slide `agente-processo`).
- **Vídeo com IA:** retestar as ferramentas com as dicas de prompt do Sérgio antes de fechar o bloco 8.

- **Exercício de prompt (decidido em 2026-10-03):** sem simulador próprio. No slide `prompt`, a turma manda o prompt seco e o com contexto no ChatGPT do próprio celular e compara.

## Conteúdo sugerido pelo Claude (revisar)

- A redação e o exemplo numérico dos slides `perceptron`, `sigmoide` e `backprop` (pesos 2, 1, −3 e viés 0,5; um passo de gradiente leva a previsão de 0,38 para 0,61) e do `dois-perceptrons` (h₁ "gostoso?" e h₂ "pesa no bolso?"; um passo de backprop leva de 0,69 para 0,78). Contas conferidas em Python.
- O slide `token-porque` (letra × palavra × token com "empreendedora"; o número 4821 é ilustrativo).
- Os slides `alerta-perceptron`, `alerta-matematica` e `alerta-atencao` (mesmo slide de descontração antes da conta, com sirene) e `embedding` (mapa 2D, cosseno bolo × torta ≈ 0,99 e bolo × carro ≈ 0,12, rei − homem + mulher ≈ rainha; números conferidos em Python). Os dois são opcionais: dá para pular direto para o `token-demo`.
- Os slides de atenção: `atencao-artigo` ("Attention Is All You Need", Vaswani e outros, Google, NeurIPS 2017, arXiv 1706.03762; o título em português é tradução livre), `atencao-exemplo` ("a torta não coube na caixa porque ela era grande/pequena", porcentagens ilustrativas) e `atencao-conta` (fórmula do artigo com exemplo: pesos 57/20/14/10%, conferidos em Python; opcional).
- Os slides `nuvem-fluxo` (caminho celular → internet → datacenter → GPUs e volta token por token), `chatgpt-ao-vivo` (roteiro no ChatGPT de verdade com o pedido dos nomes da loja de bolos; precisa de internet) e `nuvem-recursos` (hardware e software para rodar um ChatGPT, com os números de preço e energia: US$ 25–40 mil por GPU, mais de US$ 300 mil por servidor de 8, 700 W por GPU, 0,34 Wh por pergunta segundo a OpenAI em 2025). Preços e números de energia: conferir perto da data.
- Os slides `ideias`, `ideia-atendimento`, `ideia-divulgacao`, `ideia-contas` e `ideia-documentos` (depois do `chatgpt-ao-vivo`, pedidos pelo Daniel em 2026-10-03): quatro ideias de uso do ChatGPT ou do Claude para negócio pequeno e vida pessoal (responder cliente, divulgar, contas e preço, entender papel difícil). A escolha das quatro ideias, as dicas "peça assim", os avisos "jogando a real" e as conversas de exemplo no celular desenhado (loja de bolos) são do Claude, todas inventadas; a conta do preço (18 + 3 + 20 = 41, mais 20% ≈ 49, cobrar 50) foi conferida. Os quatro slides de detalhe saíram do mesmo molde; para mudar, edite os HTML direto.
- Os slides `ia-imagem`, `ia-transcricao`, `ia-locucao` e `ia-visao` (outros tipos de IA: esteira de 5 etapas com desenhos ilustrativos do bolo + cartões "como aprendeu", "no seu negócio" e "jogando a real"). Foram gerados por script; para mudar, edite os HTML direto.
- A série do harness (`harness-o-que-e`, `harness-ferramentas`, `harness-mcp`, `contexto-janela`, `contexto-limites`, `harness-skills`, `harness-resumo`; a janela de contexto é "a mesa de trabalho", de 100 mil a 1 milhão de tokens nos modelos grandes, conferir perto da data): analogias do arreio, da tomada padrão, do caderno de receitas e da confeitaria; exemplo da previsão do tempo para a feira; nomes de skills no slide são exemplos. Datas: MCP criado pela Anthropic em 2024; skills lançadas no Claude em 2025.
- O slide `rede-video` (depois do `parametros`, pedido pelo Daniel em 2026-10-03): toca `exemplos/neuralnet.mp4` (2 min 45 s, 1280 × 720, com som), posto pelo Daniel; só no player local. O vídeo é de terceiros: a simulação 3D de redes neurais do cybercontrols.org (marca no canto), com perceptron, perceptron multicamadas, rede convolucional e rede de pulsos lendo dígitos do MNIST. Título, legenda e notas são do Claude, a partir de quadros do vídeo; falta conferir se pode ficar no repositório público.
- Os slides `harness-oportunidade` e `harness-negocios` (depois do `harness-mcp`, pedidos pelo Daniel em 2026-10-03): oportunidades de negócio com um bom harness. O primeiro mostra a conta "modelo (igual para todos) + o que só você sabe + ferramentas ligadas = um bom harness" e três exemplos inventados (confeitaria, salão, oficina); o segundo, quatro oportunidades (ligar a IA no que você já usa, empacotar o que você sabe, arrumar a IA dos outros, apostar no seu ofício) com o aviso de que não é dinheiro fácil. Ideias e redação do Claude; a afirmação de que conector costuma pedir plano pago precisa ser conferida perto da data. Os dois ficam fora da numeração "N de 7" da série do harness.
- O slide `parametros`: conta 5N + 1 da rede do bolo (4 → 21, 8 → 41, 64 → 321), a escala "1 segundo por parâmetro" e o "1 trilhão" dos modelos avançados, que é ordem de grandeza (as empresas não divulgam).
- Os slides `imagem-custo` (antes do `video`: por que gerar imagem gasta; 1024 × 1024 × 3 ≈ 3 milhões de números, 20 a 50 passadas de difusão, GPU ocupada; nas notas, o estudo "Power Hungry Processing", Luccioni e outros, 2023, com 2,9 Wh por imagem contra 0,047 Wh por texto, citado de memória: conferir a fonte) e `video-desafio` (depois do `video`: 24 quadros por segundo, 120 imagens em 5 s, 1.440 em 1 min; consistência entre quadros, regras do mundo, custo). Pedidos pelo Daniel em 2026-10-03; duração dos clipes e o que é grátis mudam rápido.
- O slide `video-prompt` (depois do `video-desafio`): "No vídeo, prompt e contexto são tudo". O prompt de exemplo (diretriz de consistência, cena, câmera, ator, movimentos segundo a segundo, texto falado) é do Daniel, copiado como ele mandou em 2026-10-03, inclusive a fala com palavrão; a frase de abertura do slide e as notas são do Claude.
- O slide `video-exemplos` (depois do `video-prompt`): os dois vídeos lado a lado, com título e pergunta para a turma escritos pelo Claude ("O resultado: dois vídeos feitos com IA"; confirmar que os dois são mesmo de IA).
- Os slides `video-evolucao` (o teste do Will Smith comendo macarrão: três cartões, 2023, 2024, 2025 em diante; datas de busca na web em 2026-10-03: ModelScope em 23/03/2023, Veo 3 em maio de 2025) e `video-evolucao-player` (logo depois, antes do `agente`: toca `exemplos/AIprogression.mp4`, 1 min 9 s, posto pelo Daniel; só no player local). Redação do Claude.
- Os slides `agente-familias`, `agente-n8n` e `agente-openclaw` (logo depois do `agente`, pedidos pelo Daniel em 2026-10-03): exemplos visuais de agentes famosos. As telas são **ilustrações desenhadas** em HTML/SVG, não capturas reais (decisão do Daniel), e o cenário da loja de bolos é inventado. Fatos de busca na web em 2026-10-03: n8n é da n8n GmbH, de Berlim, desde 2019, com nó "AI Agent" que recebe modelo, memória e ferramentas; OpenClaw é de código aberto, do fim de 2025, de Peter Steinberger (antes Clawdbot e Moltbot), roda na máquina do usuário e conversa por WhatsApp, Telegram e outros. A ferramenta de agente da gravação ("open call", "opencloud") é o OpenClaw. A lista da terceira família (ChatGPT, Claude, Manus) é escolha do Claude. Os três slides entram no bloco 9a sem mudar os 20 min: o `agente-familias` é para passar em 1 minuto.
- O slide `obrigado` (último, pedido pelo Daniel em 2026-10-03): agradecimento, contato daniel@iapuru.com.br e QR code do repositório (https://github.com/robotizando/palestra-ia-para-iniciantes) com o endereço escrito embaixo. O QR é um SVG embutido no slide, gerado com a biblioteca Python `qrcode`; se o endereço do repositório mudar, é preciso gerar de novo. A frase "Ficou com dúvida ou quer continuar a conversa?" é do Claude.
- O slide `agente-stack` (depois do `agente-real`, pedido pelo Daniel em 2026-10-03): a stack da demonstração do bloco 9b em camadas. A stack é do Daniel: notebook Core i7 de última geração, GPU RTX 4060, Bonsai 27B rodando local e OpenClaw usando esse Bonsai. Fatos de busca na web em 2026-10-03: o nome completo é Bonsai 2 27B, da PrismML, lançado em 17/09/2026, licença Apache 2.0, versão ternária do Qwen 3.8 27B com 5,95 GB, que cabe em GPU de 8 GB (contexto de uns 16 mil tokens; há relato de 64 mil com ajustes). Os cartões "tudo numa máquina só", "por que cabe" e "jogando a real" são do Claude. Falta testar o conjunto antes da oficina.
- O programa `programas/bolinhas.html` e o slide `bolinhas-demo` (exemplo do bolo; se não servir, pôr `hidden` no slide).
- O exemplo de prompt seco × com contexto (loja de bolos caseiros) no slide `prompt`.
- As três frases do resumo no slide `encerramento`.
- A redação dos slides `agente-processo` e `seguranca` e do cartão "Quer mexer com agente?" no `encerramento`, resumidos a partir do áudio.
- Os pontos fortes de cada ferramenta nos slides `mapa` e `mapa-lista` e a divisão do semáforo em `mapa-maturidade` (nomes, preços e planos grátis mudam rápido: conferir perto da data). As dicas de estudo do `encerramento` agora vêm do áudio.
