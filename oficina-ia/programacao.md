# Oficina de IA: Programação (versão inicial)

> Rascunho baseado em duas fontes: a conversa gravada sobre a premissa da oficina (2026-09-28) e o áudio do Daniel para a Eliane sobre oficina de agentes de IA (alfabetização, não construção).
> **Os tempos são estimativas**, porque a duração total ainda não foi definida. Somados, dão cerca de 3h25 com um intervalo.

## Para quem é

- **Pessoa-modelo:** alguém esperto e desenrolado, mas que usa o celular de forma limitada (WhatsApp, Instagram, joguinhos). Já ouviu falar de IA e provavelmente já usou o ChatGPT, mas não sabe como funciona.
- **Empreendedor:** tem ou quer ter um negócio próprio.
- **Só celular:** não tem computador. Todo exercício precisa rodar no telefone.
- **Tom:** lúdico e simples, sem matemática e com poucos termos técnicos. Crítico e honesto ("jogar a real") sobre limites, custos e promessas exageradas.
- **Premissa:** oficina de **alfabetização, não de construção**. A pessoa sai entendendo o que a IA faz, onde ela está madura e o que evitar, e não com um agente "pronto".

## Índice

| # | Bloco | Tempo estimado | Formato |
|---|-------|----------------|---------|
| 1 | Abertura e combinados | 10 min | Conversa |
| 2 | Como a IA funciona, sem matemática | 20 min | Explicação lúdica |
| 3 | O que é token e por que isso custa dinheiro | 10 min | Explicação + exemplo |
| 4 | Mapa das IAs: qual serve para quê | 15 min | Lista comentada |
| 5 | Prompt que funciona: projetos no Claude | 20 min | Demonstração + exercício no celular |
| 6 | Exercício 1: de PDF ou foto para planilha | 20 min | Demonstração junto com a turma |
| — | Intervalo | 15 min | |
| 7 | Exercício 2: um card de Instagram para o seu negócio | 30 min | Mão na massa, no celular de cada um |
| 8 | Papo reto sobre vídeo com IA | 15 min | Conversa franca |
| 9a | Agentes de IA: o que ninguém conta | 20 min | Conversa franca |
| 9b | Agentes e IA local na prática | 20 min | Demonstração crítica |
| 10 | Encerramento, dúvidas e próximos passos | 10 min | Conversa |

---

## 1. Abertura e combinados (10 min)
- Quem somos e o que a oficina vai (e não vai) entregar.
- **Alfabetização, não construção:** ninguém vai sair daqui com um agente pronto, e isso é de propósito. Uma oficina que "constrói um agente" em 4 horas só mostra um caso que funciona porque foi montado para funcionar; é fumaça. Quem sai achando que sabe fazer cai na mão de quem vende solução milagrosa pronta e infraestrutura cara.
- Pergunta rápida para a turma: quem já usou ChatGPT? Para quê?
- Pedir para todos deixarem o celular carregado e com internet, porque vamos usar.

## 2. Como a IA funciona, sem matemática (20 min)
- **Alerta de matemática pesada** (slide `alerta-perceptron`, com sirene): descontração antes da conta. O mesmo slide se repete no bloco 3, antes do embedding.
- **A matemática por trás** (slides `perceptron`, `sigmoide`, `backprop` e `dois-perceptrons`, logo depois da explicação lúdica): perceptron como soma ponderada + viés, sigmoide e regressão logística com perda logística, descida do gradiente e backpropagation, e uma rede com dois perceptrons escondidos fazendo ida e volta com números, tudo com o exemplo do bolo. Exceção pedida pelo Daniel à regra "sem matemática"; os tempos do bloco precisam ser revistos.
- A ideia de "árvore de decisão": a IA vai escolhendo caminhos, como um jogo de perguntas.
- Neurônios como **bolinhas com um número dentro** que passam informação adiante. Sem conta de perceptron, forward ou backpropagation.
- A matemática aparece só de passagem, no máximo uma imagem, e segue em frente.
- **Demonstração ao vivo** (slides `bolinhas-demo` e `mlp-demo`): primeiro uma versão de bolso sem contas (`programas/bolinhas.html`, "esse bolo vai vender bem?"), depois o simulador do Daniel (`programas/mlp_visualizer.html`). Mostrar que no começo a rede chuta e, com exemplos, acerta.
- **Questão de tamanho** (slide `parametros`, depois das demonstrações): tabela de parâmetros da rede do bolo com 4, 8 e 64 bolinhas no meio (21, 41 e 321), uma IA média de 27 bilhões e os modelos avançados na casa de 1 trilhão.
- **Vídeo da rede em 3D** (slide `rede-video`, logo depois): `exemplos/neuralnet.mp4` (2 min 45 s, do cybercontrols.org) mostra redes de verdade lendo números escritos à mão; cada ponto é uma bolinha e cada fio é um parâmetro. O recado é o tamanho: milhões de fios, e só 2% desenhados. Só no player local.
- Mensagem central: a IA prevê a próxima palavra com base em muitos exemplos. Não "pensa" como gente.

## 3. O que é token e por que isso custa dinheiro (10 min)
- Token é o "pedacinho de texto" que a IA lê e escreve; toda conversa gasta tokens.
- A conta grátis tem limite; a conta paga e a API cobram por token.
- **Jogar a real:** o consumo de token não é transparente, e as empresas sempre empurram a versão mais nova, que gasta mais.
- **Por que pedacinhos?** (slide `token-porque`): a rede só faz conta com números, então o texto vira lista de números. Letra por letra deixa o texto enorme; palavra inteira exigiria um dicionário infinito; tokens são o meio-termo (uns 100 mil pedaços que formam qualquer palavra). Português costuma gastar mais tokens que inglês.
- **Opcional, para esticar** (slides `alerta-matematica` e `embedding`): um aviso de brincadeira antes da conta e, depois, o embedding. Cada token vira uma lista de números aprendida no treino, palavras parecidas ficam perto (cosseno) e rei − homem + mulher ≈ rainha.
- **Demonstração ao vivo** (slide `token-demo`): o programa do Daniel `programas/tokens_visualizer.html` mostra o texto sendo cortado em tokens. A divisão é simulada (parecida com a do GPT-4), não é a oficial.
- **Atenção** (slides `alerta-atencao`, com sirene, e depois `atencao-artigo`, `atencao-exemplo` e `atencao-conta`): o artigo "Attention Is All You Need" ("tudo que você precisa é atenção", Google, 2017), que criou o Transformer, o "T" do GPT. Exemplo "a torta não coube na caixa porque ela era grande/pequena": a atenção descobre quem é "ela". O terceiro slide traz a fórmula do artigo com números e é opcional.
- **Demonstração ao vivo** (slide `llm-demo`): o programa do Daniel `programas/llm_visualizer.html` gera texto token por token, mostra a atenção e as probabilidades da próxima palavra, com controle de temperatura.
- **A LLM de verdade** (slides `nuvem-fluxo`, `chatgpt-ao-vivo` e `nuvem-recursos`): o caminho da pergunta do celular até o datacenter e a volta token por token; ida ao navegador para usar o ChatGPT (pedir 3 nomes para uma loja de bolos, reparar nos pedacinhos, pedir de novo e ver a resposta mudar); e o que é preciso para rodar um ChatGPT (GPUs, servidores, energia, software), com o gancho do custo dos equipamentos e da energia: por isso a conta grátis tem limite.
- **E no meu negócio?** (slides `ideias`, `ideia-atendimento`, `ideia-divulgacao`, `ideia-contas` e `ideia-documentos`, logo depois do ChatGPT ao vivo): quatro ideias de uso do ChatGPT ou do Claude para negócio pequeno e vida pessoal, cada uma com um exemplo de pedido no celular, dicas de como pedir e um aviso "jogando a real": responder cliente (ler antes de mandar), ter ideia de post (reescrever do seu jeito), organizar contas e preço (conferir na calculadora) e entender papel difícil (não substitui contador nem advogado; cobrir dado sensível).

## 4. Mapa das IAs: qual serve para quê (15 min)
- **Antes do mapa, outros tipos de IA** (slides `ia-imagem`, `ia-transcricao`, `ia-locucao` e `ia-visao`), cada um com o caminho do que entra até o que sai, como aprendeu, uso no negócio e "jogando a real":
  - **Imagem a partir do prompt:** começa de um chuvisco e vai limpando em dezenas de passos, guiada pelo prompt (difusão). Erra mãos, letras e quantidades.
  - **Transcrição:** a voz vira números, depois uma "foto do som", e um Transformer prevê o texto. O WhatsApp já faz isso.
  - **Locução:** como a LLM, mas prevê o próximo pedacinho de som. Alerta do golpe da voz clonada: combinar palavra secreta com a família.
  - **Visão:** a foto é cortada em quadradinhos que viram "tokens" e entram na mesma LLM com a pergunta. Erra contagem e letra pequena.
Três slides: uma porta de entrada curta, o mapa completo e a leitura de maturidade. A lista é grande, mas a mensagem continua sendo "comece por estas", para a pessoa não sair perdida.
- **Comece por estas** (todas grátis e com app no celular):
  - **ChatGPT:** a mais conhecida. Tarefas do dia a dia, textos rápidos, ideias. Também tem API para colocar em programas e agentes.
  - **Claude:** tarefas mais complexas e visuais (projetos, documentos, cards). Usar com critério para não gastar os tokens da conta grátis.
  - **Gemini:** a do Google. Já vem em muito celular Android e é boa para criar imagem.
  - **Meta AI:** já está dentro do WhatsApp e do Instagram, sem instalar nada.
- **O mapa completo, por categoria** (só para saber que existe e onde procurar):
  - **Conversa:** as quatro acima; Grok (dentro do X, tom solto, assunto do momento); DeepSeek (chinesa e grátis, cuidado com dados); Copilot (Microsoft, junto do Windows e Office).
  - **Pesquisa:** Perplexity (responde com os links das fontes); ChatGPT e Gemini também buscam na internet. Sempre conferir a fonte.
  - **Imagem:** ChatGPT e Gemini (criar e editar foto); Canva com IA (artes e posts prontos); Ideogram (acerta texto escrito na imagem); Midjourney (visual artístico, só pago).
  - **Vídeo:** Sora, Veo, Kling (vídeo a partir de texto); CapCut (editar no celular, com IA). Detalhes no bloco 8.
  - **Voz e música:** ElevenLabs (narração com voz realista); Suno (música com letra a partir de um texto); criarmusicas.com.br (exemplo brasileiro para criar música).
  - **Programação:** Lovable (site ou app conversando); Claude Code e Cursor (para quem já programa).
- **O que já está maduro × o que é expectativa** (semáforo): verde, conversar com a IA e gerar imagem estão maduros; amarelo, vídeo avança rápido e programação está evoluindo bem; vermelho, o resto, principalmente agentes, ainda é mais expectativa do que realidade.

## 5. Prompt que funciona: projetos no Claude (20 min)
- Todo mundo já usou o ChatGPT; aqui apresentamos o Claude.
- Mostrar o recurso de **Projetos**: dar contexto, escrever instruções e só depois fazer o pedido. É mais completo do que o que a maioria faz.
- **Interação:** cada participante manda no próprio celular, no ChatGPT, primeiro o prompt "seco" e depois, numa conversa nova, o prompt com contexto, para comparar as respostas (decidido em 2026-10-03: sem simulador próprio).
- **Por dentro do app: o harness** (slides `harness-o-que-e`, `harness-ferramentas`, `harness-mcp`, `contexto-janela`, `contexto-limites`, `harness-skills` e `harness-resumo`), para leigos:
  - O modelo só recebe e devolve texto; o app (harness, "arreio") junta mensagem, conversa, instruções escondidas, arquivos, ferramentas e regras e manda tudo ao modelo.
  - Chamada de ferramenta: o modelo só escreve um pedido ("use a previsão do tempo para sábado"); quem executa, e decide se pode, é o app.
  - MCP: a tomada padrão para ligar serviços (agenda, planilha, sistema da loja) em qualquer IA. Cada conector é uma chave da sua casa.
  - Oportunidades de negócio (slides `harness-oportunidade` e `harness-negocios`, logo depois do MCP): o modelo é alugado e igual para todo mundo; o negócio está no arreio, que é o que só você sabe (preços, regras, jeito de atender) mais as ferramentas ligadas. Quatro oportunidades: ligar a IA no que você já usa, empacotar o que você sabe num Projeto, arrumar a IA dos negócios do bairro e apostar no seu ofício. Jogando a real: não é dinheiro fácil, conector costuma pedir plano pago e sem processo organizado não funciona.
  - Janela de contexto: a mesa de trabalho da IA. O modelo não tem memória; a cada mensagem o app reenvia tudo, e tem que caber (de 100 mil a 1 milhão de tokens nos modelos grandes). Limites: quando enche, esquece o começo; o meio de textos longos fica "borrado"; conversa longa é mais lenta e gasta o limite. Dicas: assunto novo, conversa nova; levar um resumo; mandar só o trecho que importa; instrução fixa no Projeto.
  - Skills: o caderno de receitas; o modelo vê só a capa e abre a receita quando o pedido combina.
  - Resumo da confeitaria (cérebro, confeitaria, forno, tomada, receitas) e gancho para os agentes: o app repetindo o ciclo sozinho.
  - Os tempos do bloco 5 precisam ser revistos com esses 7 slides.

## 6. Exercício 1: de PDF ou foto para planilha (20 min)
- Exemplo real, com os dados anonimizados: faturamento de um laboratório em PDF ou imagem.
- Pedir ao Claude para transformar em planilha de controle de entrada e saída.
- Feito ao vivo, junto com a turma. É simples e tem a ver com negócio.
- Enquanto o PDF real não chega, usar o fictício `exemplos/faturamento-laboratorio.pdf`.
- **Segundo exemplo** (slide `exercicio1-faturas`): `exemplos/faturas-clientes.pdf`, 25 páginas, uma fatura de cliente fictício por página. Pedir uma planilha com os dados de todas as páginas em forma de lista. O tempo do bloco precisa ser revisto com os dois exemplos.

## 7. Exercício 2: um card de Instagram para o seu negócio (30 min)
- Todo mundo pega o celular e cria um card para postar sobre o próprio negócio (ou outro assunto que quiser).
- Divisão de ferramentas:
  - **Texto persuasivo:** se não souber o que escrever, pedir sugestão ao ChatGPT, para não gastar tokens do Claude com isso.
  - **Card em si:** fazer no Claude (Claude Design), que gera o visual e permite editar o texto.
- Fechamento: algumas pessoas mostram o card que fizeram.

## 8. Papo reto sobre vídeo com IA (15 min)
- **Antes, por que imagem gasta** (slide `imagem-custo`): uma imagem são uns 3 milhões de números, a IA repassa a imagem inteira de 20 a 50 vezes e a GPU fica ocupada só nisso. Por isso a conta grátis libera poucas imagens.
- **O que dá para fazer:** vídeo animado, com a voz gerada numa ferramenta e a animação em outra.
- **O que é difícil:** vídeo com pessoa real, avatar ou trocar o próprio rosto. Nesse nível, contrate um profissional ou estude a área a sério (indicar cursos e leituras).
- Vídeo ainda está em desenvolvimento para o grande público, é caro e consome muito token.
- **Por que vídeo é um desafio** (slide `video-desafio`, depois do `video`): são 24 imagens por segundo que precisam combinar entre si (rosto, roupa, cenário), a IA não conhece as regras do mundo e a conta multiplica; por isso os clipes são curtos e caros.
- **Prompt e contexto são tudo** (slide `video-prompt`): exemplo de prompt bom de vídeo, com diretriz de consistência do rosto, cena, câmera, ator, movimentos segundo a segundo e texto falado. O que não for dito, a IA inventa diferente a cada quadro.
- **Vendo na prática** (slide `video-exemplos`): tocar os dois vídeos de exemplo (`exemplos/exemplo-video1.mp4`, 10 s, e `exemplo-video2.mp4`, 30 s) e perguntar à turma o que ficou bom e o que entrega que é IA. Só no player local.
- **A evolução em 3 anos** (slides `video-evolucao` e `video-evolucao-player`): o teste do Will Smith comendo macarrão, de 2023 (rosto derretendo) até hoje (quase real, com som), e depois o vídeo `exemplos/AIprogression.mp4` (1 min 9 s, só no player local). Gancho: o que hoje é difícil pode não ser amanhã, e desconfiar de vídeo também é alfabetização.
- Material de apoio: coletar as dicas de prompt de vídeo da conversa com o Sérgio e testar de novo antes da oficina, porque a tecnologia mudou.

## 9a. Agentes de IA: o que ninguém conta (20 min)
- O que é um agente: basicamente **um agendador turbinado**, que recebe uma tarefa e toma decisões sozinho.
- **Como é um agente por fora** (três slides com telas desenhadas, logo depois da definição): as três caras do agente (caixinhas ligadas: n8n, Make, Zapier; assistente por mensagem: OpenClaw; agente dentro do chat: ChatGPT, Claude, Manus), o **n8n** de perto (fluxo da loja de bolos: mensagem no WhatsApp → agente de IA → responde o cliente e anota na planilha, com modelo, memória e ferramentas pendurados) e o **OpenClaw** de perto (você pede pelo celular, ele age no computador de casa e consulta uma LLM). Por baixo é sempre LLM + ferramentas + repetição.
- **Pico da expectativa, longe da maturidade.** Tem muita gente vendendo curso de agente e vendendo agente como solução final e oportunidade de ganhar dinheiro. Já vimos esse filme com blockchain e Bitcoin: toda tecnologia nova vira curso e artigo antes de passar no teste de mercado.
- **Números do Gartner** (conferir a fonte antes de usar): só 17% das empresas estão implantando agentes, e 80% das implantações falham, o dobro de quando não se usa agente.
- **Sem processo definido, o agente não serve para nada.** Ele amplifica processos e competências que já funcionam; não conserta processo bagunçado. E precisa de alguém (uma equipe) que traduza o processo para a ferramenta.
- **A parte difícil não são as caixinhas.** As ferramentas visuais de arrastar e ligar parecem simples, mas escondem complexidade. O difícil é decidir o que fazer quando algo dá errado. Como o agente age sozinho, os problemas aparecem uma semana depois, quando ninguém está olhando.
- **Segurança, o problema nº 1 (e quase ninguém fala):** dados pessoais, dados da empresa, senhas de banco e de ferramentas pagas estão indo parar na internet sem filtro, e tem gente usando os recursos dos outros com isso.
- **Custo de execução:** um aplicativo comum é feito uma vez e copiado quase de graça. O agente custa toda vez que roda (máquina forte, infraestrutura). Quem vende o pacote fechado não conta isso.
- No futuro a precisão vai melhorar, mas o papel do agente continua o mesmo: amplificar o que já funciona.

## 9b. Agentes e IA local na prática (20 min)
- **Demonstração de IA local:** a IA rodando na máquina, sem internet. Mostrar o que ela exige (placa de vídeo e memória específicas), por isso a maioria contrata serviço em nuvem.
- **Demonstração do agente** (OpenClaw): o conector liga em qualquer IA, até na local.
- **A stack da demonstração** (slide `agente-stack`): notebook Core i7 de última geração, GPU RTX 4060 (8 GB), modelo Bonsai 27B rodando local e OpenClaw usando esse Bonsai. Tudo numa máquina só, sem internet e sem crédito de API; em troca, é mais lento, tem janela de contexto menor e o notebook custa caro.
- Custos na prática:
  - A conta normal do Claude ou do ChatGPT não serve para agente; é preciso pagar a API e colocar créditos.
  - Se o agente não for bem configurado, ele sai gastando créditos à toa, por exemplo ficando vendo posts na internet.

## 10. Encerramento, dúvidas e próximos passos (10 min)
- Resumo em três frases: como a IA funciona, qual ferramenta usar para quê e o que é exagero.
- **Se quiser trabalhar com agentes, o caminho seguro:** estudar; definir (e escrever) os seus processos primeiro; observar as ferramentas antes de pagar por elas; analisar casos reais, onde o agente se aplica e onde não se aplica.
- Perguntas.
- Slide final de agradecimento: contato do Daniel (daniel@iapuru.com.br) e QR code do repositório no GitHub com todo o material.

---

## Pontos em aberto
- **Duração total e formato:** quantas horas, presencial, quantas pessoas e se tem Wi-Fi no local. No áudio para a Eliane, a referência foi uma oficina de 4 horas.
- **Números do Gartner (bloco 9a):** achar a fonte e o ano dos 17% de empresas implantando agentes e dos 80% de falha antes de colocar no slide.
- **Exemplo do faturamento:** conseguir o PDF real e anonimizar os dados.
- **Vídeo com IA:** retestar as ferramentas com as dicas do Sérgio antes de fechar o bloco 8.
