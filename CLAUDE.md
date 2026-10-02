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
- **Alfabetização, não construção:** ninguém sai com agente pronto. Sobre agentes, mostrar mais os problemas (processo, falhas, segurança, custo) do que as promessas.
- Mapa das IAs deve ser curto ("comece por estas"), para não deixar a pessoa perdida.

## Onde está cada coisa

| Caminho | O que é |
|---|---|
| `oficina-ia/programacao.md` | Programação em 10 blocos, com o 9 dividido em 9a e 9b (~3h25 com intervalo), com os pontos em aberto no fim. É a fonte de verdade do conteúdo. |
| `oficina-ia/apresentacao/deck.json` | Ordem dos 20 slides, seções e fontes. |
| `oficina-ia/apresentacao/slides/*.html` | Um fragmento HTML por slide (`<section>` com notas do apresentador em `<aside>`). |

**Versão viva da apresentação:** https://claude.ai/artifact/H3THoFiSSpR9ftCQrV9w39 (Artifact do tipo Slides no claude.ai; lá dá para apresentar, editar e exportar para PowerPoint ou PDF).

- Os HTML do repositório são a fonte desse Artifact, **não páginas independentes**: usam elementos do tipo Slides (`<x-icon>`, `<x-shape>`) e não abrem sozinhos no navegador.
- Edições feitas na página do Artifact não voltam sozinhas para o repositório, e edições aqui não publicam o Artifact. Em 2026-10-01 os arquivos do repositório estavam idênticos ao Artifact publicado antes da inclusão do áudio da Eliane; depois disso o repositório ficou à frente (slides `agente-processo` e `seguranca` novos e outros ajustados), até alguém republicar. Antes de mexer, confirme qual lado está mais novo.

## Ordem dos slides

capa, publico, roteiro, abertura, funciona, previsao, token, mapa, projetos, prompt, exercicio1, intervalo, exercicio2, video, agente, agente-processo, seguranca, agente-real, encerramento, pendencias.

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
- **Números do Gartner:** achar fonte e ano dos 17% de empresas implantando agentes e dos 80% de falha (slide `agente-processo`).
- **Vídeo com IA:** retestar as ferramentas com as dicas de prompt do Sérgio antes de fechar o bloco 8.

## Conteúdo sugerido pelo Claude (revisar)

- O exemplo de prompt seco × com contexto (loja de bolos caseiros) no slide `prompt`.
- As três frases do resumo no slide `encerramento`.
- A redação dos slides `agente-processo` e `seguranca` e do cartão "Quer mexer com agente?" no `encerramento`, resumidos a partir do áudio.
- Lacuna entre colchetes: ponto forte de Grok/Perplexity (slide `mapa`). As dicas de estudo do `encerramento` agora vêm do áudio.
