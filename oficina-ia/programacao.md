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
| 5 | Prompt que funciona: projetos no Claude | 20 min | Demonstração + simulador no celular |
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
- A ideia de "árvore de decisão": a IA vai escolhendo caminhos, como um jogo de perguntas.
- Neurônios como **bolinhas com um número dentro** que passam informação adiante. Sem conta de perceptron, forward ou backpropagation.
- A matemática aparece só de passagem, no máximo uma imagem, e segue em frente.
- Mensagem central: a IA prevê a próxima palavra com base em muitos exemplos. Não "pensa" como gente.

## 3. O que é token e por que isso custa dinheiro (10 min)
- Token é o "pedacinho de texto" que a IA lê e escreve; toda conversa gasta tokens.
- A conta grátis tem limite; a conta paga e a API cobram por token.
- **Jogar a real:** o consumo de token não é transparente, e as empresas sempre empurram a versão mais nova, que gasta mais.

## 4. Mapa das IAs: qual serve para quê (15 min)
- Lista curta do que cada ferramenta resolve bem:
  - **ChatGPT:** tarefas do dia a dia, textos rápidos, ideias. Também tem API para colocar em programas e agentes.
  - **Claude:** tarefas mais complexas e visuais (projetos, documentos, cards). Usar com critério para não gastar os tokens da conta grátis.
  - **Grok, Perplexity e outras:** citar que existem e o ponto forte de cada uma.
  - **Imagem e vídeo:** citar as ferramentas, detalhes ficam para o bloco 8.
- **O que já está maduro × o que é expectativa:** conversar com a IA (ChatGPT, Grok) e gerar imagem estão maduros; vídeo avança rápido; programação está evoluindo bem. O resto, principalmente agentes, ainda é mais expectativa do que realidade.
- Cuidado para não virar uma lista gigante: muita referência deixa a pessoa perdida. Mostrar que existem e dizer "comece por estas".

## 5. Prompt que funciona: projetos no Claude (20 min)
- Todo mundo já usou o ChatGPT; aqui apresentamos o Claude.
- Mostrar o recurso de **Projetos**: dar contexto, escrever instruções e só depois fazer o pedido. É mais completo do que o que a maioria faz.
- **Interação:** simulador rodando no celular dos participantes, comparando um prompt "seco" com um prompt com contexto, para verem a diferença na resposta.

## 6. Exercício 1: de PDF ou foto para planilha (20 min)
- Exemplo real, com os dados anonimizados: faturamento de um laboratório em PDF ou imagem.
- Pedir ao Claude para transformar em planilha de controle de entrada e saída.
- Feito ao vivo, junto com a turma. É simples e tem a ver com negócio.

## 7. Exercício 2: um card de Instagram para o seu negócio (30 min)
- Todo mundo pega o celular e cria um card para postar sobre o próprio negócio (ou outro assunto que quiser).
- Divisão de ferramentas:
  - **Texto persuasivo:** se não souber o que escrever, pedir sugestão ao ChatGPT, para não gastar tokens do Claude com isso.
  - **Card em si:** fazer no Claude (Claude Design), que gera o visual e permite editar o texto.
- Fechamento: algumas pessoas mostram o card que fizeram.

## 8. Papo reto sobre vídeo com IA (15 min)
- **O que dá para fazer:** vídeo animado, com a voz gerada numa ferramenta e a animação em outra.
- **O que é difícil:** vídeo com pessoa real, avatar ou trocar o próprio rosto. Nesse nível, contrate um profissional ou estude a área a sério (indicar cursos e leituras).
- Vídeo ainda está em desenvolvimento para o grande público, é caro e consome muito token.
- Material de apoio: coletar as dicas de prompt de vídeo da conversa com o Sérgio e testar de novo antes da oficina, porque a tecnologia mudou.

## 9a. Agentes de IA: o que ninguém conta (20 min)
- O que é um agente: basicamente **um agendador turbinado**, que recebe uma tarefa e toma decisões sozinho.
- **Pico da expectativa, longe da maturidade.** Tem muita gente vendendo curso de agente e vendendo agente como solução final e oportunidade de ganhar dinheiro. Já vimos esse filme com blockchain e Bitcoin: toda tecnologia nova vira curso e artigo antes de passar no teste de mercado.
- **Números do Gartner** (conferir a fonte antes de usar): só 17% das empresas estão implantando agentes, e 80% das implantações falham, o dobro de quando não se usa agente.
- **Sem processo definido, o agente não serve para nada.** Ele amplifica processos e competências que já funcionam; não conserta processo bagunçado. E precisa de alguém (uma equipe) que traduza o processo para a ferramenta.
- **A parte difícil não são as caixinhas.** As ferramentas visuais de arrastar e ligar parecem simples, mas escondem complexidade. O difícil é decidir o que fazer quando algo dá errado. Como o agente age sozinho, os problemas aparecem uma semana depois, quando ninguém está olhando.
- **Segurança, o problema nº 1 (e quase ninguém fala):** dados pessoais, dados da empresa, senhas de banco e de ferramentas pagas estão indo parar na internet sem filtro, e tem gente usando os recursos dos outros com isso.
- **Custo de execução:** um aplicativo comum é feito uma vez e copiado quase de graça. O agente custa toda vez que roda (máquina forte, infraestrutura). Quem vende o pacote fechado não conta isso.
- No futuro a precisão vai melhorar, mas o papel do agente continua o mesmo: amplificar o que já funciona.

## 9b. Agentes e IA local na prática (20 min)
- **Demonstração de IA local:** a IA rodando na máquina, sem internet. Mostrar o que ela exige (placa de vídeo e memória específicas), por isso a maioria contrata serviço em nuvem.
- **Demonstração do agente** (OpenClaw, nome a confirmar): o conector liga em qualquer IA, até na local.
- Custos na prática:
  - A conta normal do Claude ou do ChatGPT não serve para agente; é preciso pagar a API e colocar créditos.
  - Se o agente não for bem configurado, ele sai gastando créditos à toa, por exemplo ficando vendo posts na internet.

## 10. Encerramento, dúvidas e próximos passos (10 min)
- Resumo em três frases: como a IA funciona, qual ferramenta usar para quê e o que é exagero.
- **Se quiser trabalhar com agentes, o caminho seguro:** estudar; definir (e escrever) os seus processos primeiro; observar as ferramentas antes de pagar por elas; analisar casos reais, onde o agente se aplica e onde não se aplica.
- Link para assinar o Claude (ver pontos em aberto).
- Perguntas.

---

## Pontos em aberto
- **Duração total e formato:** quantas horas, presencial, quantas pessoas e se tem Wi-Fi no local. No áudio para a Eliane, a referência foi uma oficina de 4 horas.
- **Números do Gartner (bloco 9a):** achar a fonte e o ano dos 17% de empresas implantando agentes e dos 80% de falha antes de colocar no slide.
- **Simulador de prompt no celular:** definir o que ele compara e como a turma acessa (link ou QR code).
- **Exemplo do faturamento:** conseguir o PDF real e anonimizar os dados.
- **Link de afiliado do Claude:** na conversa ficou a dúvida se vale usar; decidir.
- **Nome da ferramenta de agente:** confirmar se é OpenClaw (na gravação aparece como "open call" e "opencloud").
- **Vídeo com IA:** retestar as ferramentas com as dicas do Sérgio antes de fechar o bloco 8.
