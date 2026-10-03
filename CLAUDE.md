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
| `oficina-ia/apresentacao/deck.json` | Ordem dos 45 slides, seções e fontes. |
| `oficina-ia/apresentacao/slides/*.html` | Um fragmento HTML por slide (`<section>` com notas do apresentador em `<aside>`). |
| `oficina-ia/apresentacao/player/` | Player local que mostra esses slides sem o claude.ai e sem internet (fontes e ícones guardados no repositório). |
| `oficina-ia/apresentacao/apresentar.sh` | Sobe um servidor local (servindo `oficina-ia/` inteira) e abre o player no navegador. |
| `oficina-ia/programas/` | Programas de demonstração: `mlp_visualizer.html`, `llm_visualizer.html` e `tokens_visualizer.html` (do Daniel) e `bolinhas.html` (versão sem matemática feita pelo Claude). `tela-cheia.html?p=<programa>.html` mostra um deles em tela cheia sem alterar o arquivo. |

**Versão viva da apresentação:** https://claude.ai/artifact/H3THoFiSSpR9ftCQrV9w39 (Artifact do tipo Slides no claude.ai; lá dá para apresentar, editar e exportar para PowerPoint ou PDF).

- Os HTML do repositório são a fonte desse Artifact, **não páginas independentes**: usam elementos do tipo Slides (`<x-icon>`, `<x-shape>`) e não abrem sozinhos no navegador.
- Edições feitas na página do Artifact não voltam sozinhas para o repositório, e edições aqui não publicam o Artifact. Em 2026-10-01 os arquivos do repositório estavam idênticos ao Artifact publicado antes da inclusão do áudio da Eliane; depois disso o repositório ficou à frente (slides `agente-processo` e `seguranca` novos e outros ajustados), até alguém republicar. Antes de mexer, confirme qual lado está mais novo.

## Apresentar localmente

- Rode `oficina-ia/apresentacao/apresentar.sh`: ele abre `http://127.0.0.1:8765/apresentacao/player/` (ou a próxima porta livre). Ctrl+C no terminal encerra. Sem o script: `python3 -m http.server` dentro de `oficina-ia/` e abrir `/apresentacao/player/`. Abrir o `index.html` direto do arquivo não funciona.
- Atalhos: → / ← (ou passador de slides), número + Enter para pular, F tela cheia, N notas do apresentador (segunda janela, com cronômetro e próximo slide), B tela preta, S liga/desliga o som, R recarrega depois de editar um slide.
- Som: `data-som="alerta"` na `<section>` toca uma sirene gerada pelo player (sem arquivo) ao chegar no slide; outro valor é tratado como arquivo de áudio relativo a `apresentacao/` (ex.: `data-som="sons/buzina.mp3"`). Usado em `alerta-perceptron` e `alerta-matematica`. O navegador só toca depois de um clique ou tecla na janela dos slides; o Artifact do claude.ai ignora o atributo.
- O player é nosso, não o motor do claude.ai: cobre o que os slides usam hoje (tela 1920×1080, estilos inline, `x-icon`, `x-shape`, transição fade, `<aside>`, `hidden`). Os ícones são do Phosphor (MIT), parecidos mas não idênticos aos do claude.ai. `x-connector`, `x-embed`, animações `data-build-*` e a transição `magic` não estão implementados. Se um slide novo usar um desses, conferir no player antes de apresentar.
- Links (`<a href>`) nos slides são relativos à pasta `apresentacao/` e abrem em outra aba. Os slides `bolinhas-demo`, `mlp-demo`, `token-demo` e `llm-demo` usam isso para abrir os programas de `programas/` via `tela-cheia.html` (o navegador exige um toque na aba nova para entrar em tela cheia; Ctrl+W volta aos slides). Esses links só funcionam no player local: os programas não estão publicados no Artifact do claude.ai.
- Para tirar um slide da apresentação (por exemplo `pendencias`), coloque `hidden` na `<section>`: o player pula.

## Ordem dos slides

capa, publico, roteiro, abertura, funciona, alerta-perceptron, perceptron, sigmoide, backprop, dois-perceptrons, bolinhas-demo, mlp-demo, parametros, previsao, token, token-porque, alerta-matematica, embedding, token-demo, atencao-artigo, atencao-exemplo, atencao-conta, llm-demo, nuvem-fluxo, chatgpt-ao-vivo, nuvem-recursos, ia-imagem, ia-transcricao, ia-locucao, ia-visao, mapa, mapa-lista, mapa-maturidade, projetos, prompt, exercicio1, intervalo, exercicio2, video, agente, agente-processo, seguranca, agente-real, encerramento, pendencias.

O último slide ("Bastidores", `pendencias`) é só para a equipe: esconder ou apagar antes de apresentar à turma.

## Visual (decidido)

- Fontes: **Fredoka** (títulos) + **Nunito Sans** (texto), via Google Fonts.
- Cores: creme `#FFF8EE` (fundo), azul-marinho `#1F2A44`, laranja `#F28C28`; laranja escuro `#9A4508` para rótulos e pendências; cards claros `#FFFDF9` com borda `#EFD9B8`.
- Pontos em aberto aparecem como pílulas tracejadas "Em aberto: ...".

## Pontos em aberto

- **Duração total e formato:** quantas horas, presencial, quantas pessoas, se tem Wi-Fi. Os tempos da programação são estimativas.
- **Simulador de prompt no celular:** ainda não existe. Definir o que compara (prompt "seco" × com contexto) e como a turma acessa (link ou QR code).
- **Exemplo do faturamento (exercício 1):** conseguir o PDF real de um laboratório e anonimizar os dados.
- **Link de afiliado do Claude:** decidir se usa no encerramento.
- **Ferramenta de agente:** confirmar se é OpenClaw (na gravação aparece como "open call" e "opencloud").
- **Preços e energia (slide `nuvem-recursos`):** conferir o preço das GPUs e servidores e os números de consumo perto da data.
- **Números do Gartner:** achar fonte e ano dos 17% de empresas implantando agentes e dos 80% de falha (slide `agente-processo`).
- **Vídeo com IA:** retestar as ferramentas com as dicas de prompt do Sérgio antes de fechar o bloco 8.

## Conteúdo sugerido pelo Claude (revisar)

- A redação e o exemplo numérico dos slides `perceptron`, `sigmoide` e `backprop` (pesos 2, 1, −3 e viés 0,5; um passo de gradiente leva a previsão de 0,38 para 0,61) e do `dois-perceptrons` (h₁ "gostoso?" e h₂ "pesa no bolso?"; um passo de backprop leva de 0,69 para 0,78). Contas conferidas em Python.
- O slide `token-porque` (letra × palavra × token com "empreendedora"; o número 4821 é ilustrativo).
- Os slides `alerta-perceptron` e `alerta-matematica` (mesmo slide de descontração antes da conta, com sirene) e `embedding` (mapa 2D, cosseno bolo × torta ≈ 0,99 e bolo × carro ≈ 0,12, rei − homem + mulher ≈ rainha; números conferidos em Python). Os dois são opcionais: dá para pular direto para o `token-demo`.
- Os slides de atenção: `atencao-artigo` ("Attention Is All You Need", Vaswani e outros, Google, NeurIPS 2017, arXiv 1706.03762; o título em português é tradução livre), `atencao-exemplo` ("a torta não coube na caixa porque ela era grande/pequena", porcentagens ilustrativas) e `atencao-conta` (fórmula do artigo com exemplo: pesos 57/20/14/10%, conferidos em Python; opcional).
- Os slides `nuvem-fluxo` (caminho celular → internet → datacenter → GPUs e volta token por token), `chatgpt-ao-vivo` (roteiro no ChatGPT de verdade com o pedido dos nomes da loja de bolos; precisa de internet) e `nuvem-recursos` (hardware e software para rodar um ChatGPT, com os números de preço e energia: US$ 25–40 mil por GPU, mais de US$ 300 mil por servidor de 8, 700 W por GPU, 0,34 Wh por pergunta segundo a OpenAI em 2025). Preços e números de energia: conferir perto da data.
- Os slides `ia-imagem`, `ia-transcricao`, `ia-locucao` e `ia-visao` (outros tipos de IA: esteira de 5 etapas com desenhos ilustrativos do bolo + cartões "como aprendeu", "no seu negócio" e "jogando a real"). Foram gerados por script; para mudar, edite os HTML direto.
- O slide `parametros`: conta 5N + 1 da rede do bolo (4 → 21, 8 → 41, 64 → 321), a escala "1 segundo por parâmetro" e o "1 trilhão" dos modelos avançados, que é ordem de grandeza (as empresas não divulgam).
- O programa `programas/bolinhas.html` e o slide `bolinhas-demo` (exemplo do bolo; se não servir, pôr `hidden` no slide).
- O exemplo de prompt seco × com contexto (loja de bolos caseiros) no slide `prompt`.
- As três frases do resumo no slide `encerramento`.
- A redação dos slides `agente-processo` e `seguranca` e do cartão "Quer mexer com agente?" no `encerramento`, resumidos a partir do áudio.
- Os pontos fortes de cada ferramenta nos slides `mapa` e `mapa-lista` e a divisão do semáforo em `mapa-maturidade` (nomes, preços e planos grátis mudam rápido: conferir perto da data). As dicas de estudo do `encerramento` agora vêm do áudio.
