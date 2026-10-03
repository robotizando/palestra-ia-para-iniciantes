// Player local dos slides da Oficina de IA.
// Lê ../deck.json e ../slides/<id>.html e mostra cada <section> numa tela de 1920×1080.
// Abra com ../apresentar.sh (o navegador não deixa ler arquivos locais por file://).
// Com "?notas" no endereço, vira a janela de notas do apresentador.

(function () {
  'use strict';

  const BASE = '../';
  const LARGURA = 1920;
  const ALTURA = 1080;
  const canal = 'BroadcastChannel' in window ? new BroadcastChannel('oficina-ia-slides') : null;
  const ehNotas = new URLSearchParams(location.search).has('notas');

  // ---------- Elementos do formato ----------

  customElements.define('x-icon', class extends HTMLElement {
    connectedCallback() {
      const nome = this.getAttribute('name');
      const desenho = window.ICONES && window.ICONES[nome];
      if (!desenho) console.warn('Ícone desconhecido:', nome);
      this.innerHTML = '<svg viewBox="0 0 256 256" aria-hidden="true">' + (desenho || '') + '</svg>';
    }
  });
  customElements.define('x-shape', class extends HTMLElement {});

  // ---------- Carregamento ----------

  async function buscar(caminho, comoJson) {
    const resp = await fetch(BASE + caminho, { cache: 'no-store' });
    if (!resp.ok) throw new Error(caminho + ': ' + resp.status);
    return comoJson ? resp.json() : resp.text();
  }

  async function carregarDeck() {
    const deck = await buscar('deck.json', true);
    const textos = await Promise.all(deck.order.map((id) => buscar('slides/' + id + '.html')));
    const slides = [];
    textos.forEach((html, i) => {
      const modelo = document.createElement('template');
      modelo.innerHTML = html;
      const secao = modelo.content.querySelector('section');
      if (!secao) return console.warn('Slide sem <section>:', deck.order[i]);
      if (!secao.id) secao.id = deck.order[i];
      if (secao.hasAttribute('hidden')) return; // slide escondido: não entra na apresentação
      // Imagens ficam ao lado do deck, não do player.
      secao.querySelectorAll('img[src]').forEach((img) => {
        const src = img.getAttribute('src');
        if (!/^(https?:|data:|\/)/.test(src)) img.setAttribute('src', BASE + src);
      });
      // Links (ex.: os programas de demonstração) também, e abrem em outra aba.
      secao.querySelectorAll('a[href]').forEach((a) => {
        const href = a.getAttribute('href');
        if (!/^(https?:|mailto:|#|\/)/.test(href)) a.setAttribute('href', BASE + href);
        a.setAttribute('target', '_blank');
        a.setAttribute('rel', 'noopener');
      });
      const aside = secao.querySelector('aside');
      slides.push({ id: secao.id, secao, notas: aside ? aside.innerHTML.trim() : '', som: secao.dataset.som || '' });
    });
    return { titulo: deck.title || 'Apresentação', slides };
  }

  // ---------- Som ----------

  // <section data-som="alerta"> toca uma sirene gerada aqui mesmo (sem arquivo, funciona sem internet).
  // Qualquer outro valor é tratado como arquivo de áudio ao lado do deck (ex.: data-som="sons/buzina.mp3").
  // O navegador só libera som depois de um clique ou tecla nesta janela; S liga/desliga.
  let audio = null;
  let somLigado = true;
  function contextoAudio() {
    const Ctx = window.AudioContext || window.webkitAudioContext;
    if (!audio && Ctx) audio = new Ctx();
    return audio;
  }
  function liberarAudio() {
    const ctx = contextoAudio();
    if (ctx && ctx.state === 'suspended') ctx.resume();
  }
  function sirene() {
    const ctx = contextoAudio();
    if (!ctx) return;
    if (ctx.state === 'suspended') ctx.resume();
    const t = ctx.currentTime + 0.02;
    const osc = ctx.createOscillator();
    const filtro = ctx.createBiquadFilter();
    const volume = ctx.createGain();
    osc.type = 'sawtooth';
    filtro.type = 'lowpass';
    filtro.frequency.value = 2200;
    // Alarme de dois tons: 6 bipes alternando agudo e grave, 1,5 s no total.
    for (let k = 0; k < 6; k++) osc.frequency.setValueAtTime(k % 2 ? 660 : 880, t + k * 0.25);
    volume.gain.setValueAtTime(0, t);
    volume.gain.linearRampToValueAtTime(0.18, t + 0.03);
    volume.gain.setValueAtTime(0.18, t + 1.4);
    volume.gain.linearRampToValueAtTime(0, t + 1.5);
    osc.connect(filtro).connect(volume).connect(ctx.destination);
    osc.start(t);
    osc.stop(t + 1.55);
  }
  function tocarSom(som) {
    if (!som || !somLigado) return;
    if (som === 'alerta') return sirene();
    const caminho = /^(https?:|\/)/.test(som) ? som : BASE + som;
    new Audio(caminho).play().catch(() => console.warn('Não consegui tocar', caminho));
  }

  // ---------- Palco ----------

  // Cria um palco com uma cópia de todas as seções; mostrar(i) troca o slide visível.
  function criarPalco(slides) {
    const palco = document.createElement('div');
    palco.className = 'palco';
    const tela = document.createElement('div');
    tela.className = 'tela sem-animacao';
    slides.forEach((s) => tela.appendChild(s.secao.cloneNode(true)));
    palco.appendChild(tela);

    let atual = -1;
    function ajustar() {
      const escala = Math.min(palco.clientWidth / LARGURA, palco.clientHeight / ALTURA) || 0;
      tela.style.transform = 'translate(-50%, -50%) scale(' + escala + ')';
    }
    new ResizeObserver(ajustar).observe(palco);

    return {
      elemento: palco,
      ajustar,
      mostrar(i, animar) {
        tela.classList.toggle('sem-animacao', !animar);
        if (atual >= 0 && tela.children[atual]) tela.children[atual].classList.remove('atual');
        atual = i;
        if (tela.children[i]) tela.children[i].classList.add('atual');
      },
    };
  }

  function indicePorHash(slides) {
    const id = decodeURIComponent(location.hash.slice(1));
    const i = slides.findIndex((s) => s.id === id);
    return i >= 0 ? i : 0;
  }

  // ---------- Janela principal ----------

  function iniciarApresentacao(deck) {
    const { slides } = deck;
    document.title = deck.titulo;
    document.body.className = 'modo-slides';
    const app = document.getElementById('app');
    app.innerHTML = '';

    const palco = criarPalco(slides);
    app.appendChild(palco.elemento);
    app.insertAdjacentHTML('beforeend',
      '<div class="cortina"></div>' +
      '<div class="salto"></div>' +
      '<div class="barra">' +
      '<button data-acao="anterior" title="Anterior (←)">◀</button>' +
      '<span class="contador"></span>' +
      '<button data-acao="proximo" title="Próximo (→)">▶</button>' +
      '<button data-acao="notas" title="Notas do apresentador (N)">Notas</button>' +
      '<button data-acao="tela-cheia" title="Tela cheia (F)">Tela cheia</button>' +
      '<button data-acao="ajuda" title="Atalhos (?)">?</button>' +
      '</div>');
    const contador = app.querySelector('.barra .contador');
    const salto = app.querySelector('.salto');

    let atual = -1;
    function ir(i, avisar = true, animar = true) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      if (i === atual) return;
      atual = i;
      palco.mostrar(i, animar);
      if (animar) tocarSom(slides[i].som);
      contador.textContent = (i + 1) + ' / ' + slides.length;
      history.replaceState(null, '', '#' + encodeURIComponent(slides[i].id));
      if (avisar && canal) canal.postMessage({ tipo: 'ir', id: slides[i].id });
    }

    const acoes = {
      anterior: () => ir(atual - 1),
      proximo: () => ir(atual + 1),
      notas: () => window.open(location.pathname + '?notas#' + slides[atual].id, 'oficina-ia-notas', 'width=1200,height=760'),
      som: () => {
        somLigado = !somLigado;
        salto.textContent = somLigado ? 'Som ligado' : 'Som desligado';
        salto.classList.add('ativo');
        setTimeout(() => salto.classList.remove('ativo'), 1200);
      },
      'tela-cheia': () => (document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen()),
      apagar: () => document.body.classList.toggle('apagado'),
      ajuda: () => alert(
        'Atalhos\n\n' +
        '→ ↓ Espaço PageDown: próximo slide\n' +
        '← ↑ PageUp: slide anterior\n' +
        'Home / End: primeiro / último\n' +
        'número + Enter: ir para o slide (ex.: 12 Enter)\n' +
        'F: tela cheia\n' +
        'N: abrir as notas do apresentador\n' +
        'S: liga/desliga o som dos slides de alerta\n' +
        'B ou .: tela preta\n' +
        'R: recarregar os slides (depois de editar)'),
    };

    app.querySelector('.barra').addEventListener('click', (e) => {
      const botao = e.target.closest('button');
      if (botao) acoes[botao.dataset.acao]();
      e.stopPropagation();
    });
    palco.elemento.addEventListener('click', (e) => {
      if (e.target.closest('a')) return;
      ir(atual + (e.clientX < window.innerWidth / 4 ? -1 : 1));
    });

    // O navegador só deixa tocar som depois de um gesto nesta janela.
    document.addEventListener('pointerdown', liberarAudio);
    document.addEventListener('keydown', liberarAudio);

    let digitado = '';
    document.addEventListener('keydown', (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      const k = e.key;
      if (/^[0-9]$/.test(k)) {
        digitado += k;
        salto.textContent = 'Ir para ' + digitado;
        salto.classList.add('ativo');
        return;
      }
      if (k === 'Enter' && digitado) {
        ir(parseInt(digitado, 10) - 1);
      } else if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(k)) {
        ir(atual + 1);
      } else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(k)) {
        ir(atual - 1);
      } else if (k === 'Home') {
        ir(0);
      } else if (k === 'End') {
        ir(slides.length - 1);
      } else if (k === 'f' || k === 'F') {
        acoes['tela-cheia']();
      } else if (k === 'n' || k === 'N') {
        acoes.notas();
      } else if (k === 'b' || k === 'B' || k === '.') {
        acoes.apagar();
      } else if (k === 's' || k === 'S') {
        e.preventDefault();
        digitado = '';
        acoes.som(); // mostra o aviso por conta própria
        return;
      } else if (k === 'r' || k === 'R') {
        location.reload();
      } else if (k === '?') {
        acoes.ajuda();
      } else if (k !== 'Escape') {
        return;
      }
      e.preventDefault();
      digitado = '';
      salto.classList.remove('ativo');
    });

    // Gesto de arrastar (tablet ou tela de toque).
    let toqueX = null;
    palco.elemento.addEventListener('touchstart', (e) => { toqueX = e.touches[0].clientX; }, { passive: true });
    palco.elemento.addEventListener('touchend', (e) => {
      if (toqueX === null) return;
      const dx = e.changedTouches[0].clientX - toqueX;
      if (Math.abs(dx) > 50) ir(atual + (dx < 0 ? 1 : -1));
      toqueX = null;
    });

    // A barra aparece quando o mouse mexe e some depois de 2,5 s.
    let timerMouse;
    document.addEventListener('mousemove', () => {
      document.body.classList.add('mouse');
      clearTimeout(timerMouse);
      timerMouse = setTimeout(() => document.body.classList.remove('mouse'), 2500);
    });

    if (canal) {
      canal.onmessage = (e) => {
        const m = e.data;
        if (m.tipo === 'ir') {
          const i = slides.findIndex((s) => s.id === m.id);
          if (i >= 0) ir(i, false);
        } else if (m.tipo === 'qual') {
          canal.postMessage({ tipo: 'ir', id: slides[atual].id });
        }
      };
    }
    window.addEventListener('hashchange', () => ir(indicePorHash(slides)));

    ir(indicePorHash(slides), true, false);
  }

  // ---------- Janela de notas ----------

  function iniciarNotas(deck) {
    const { slides } = deck;
    document.title = 'Notas: ' + deck.titulo;
    document.body.className = 'modo-notas';
    const app = document.getElementById('app');
    app.innerHTML =
      '<div class="notas">' +
      '<div class="atual-box"><span class="rotulo">Agora</span><div class="lugar-atual"></div>' +
      '<div class="relogios"><span class="cronometro">00:00</span><button class="zerar">Zerar</button>' +
      '<span class="contador"></span><span style="flex:1"></span><span class="hora"></span></div></div>' +
      '<div class="direita"><span class="rotulo">Próximo</span><div class="lugar-proximo"></div></div>' +
      '<div class="direita"><span class="rotulo">Notas</span><div class="texto"></div></div>' +
      '</div>';

    const palcoAtual = criarPalco(slides);
    const palcoProximo = criarPalco(slides);
    app.querySelector('.lugar-atual').replaceWith(palcoAtual.elemento);
    app.querySelector('.lugar-proximo').replaceWith(palcoProximo.elemento);
    const fim = document.createElement('div');
    fim.className = 'fim';
    fim.textContent = 'Fim da apresentação';
    palcoProximo.elemento.after(fim);
    const texto = app.querySelector('.texto');
    const contador = app.querySelector('.contador');

    let atual = -1;
    function ir(i, avisar = true) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      if (i === atual) return;
      atual = i;
      palcoAtual.mostrar(i, false);
      const temProximo = i + 1 < slides.length;
      palcoProximo.elemento.style.display = temProximo ? '' : 'none';
      fim.style.display = temProximo ? 'none' : '';
      if (temProximo) palcoProximo.mostrar(i + 1, false);
      texto.innerHTML = slides[i].notas || 'Sem notas neste slide.';
      texto.classList.toggle('vazio', !slides[i].notas);
      contador.textContent = 'Slide ' + (i + 1) + ' de ' + slides.length;
      history.replaceState(null, '', location.search + '#' + encodeURIComponent(slides[i].id));
      if (avisar && canal) canal.postMessage({ tipo: 'ir', id: slides[i].id });
    }

    document.addEventListener('keydown', (e) => {
      if (['ArrowRight', 'ArrowDown', 'PageDown', ' '].includes(e.key)) ir(atual + 1);
      else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) ir(atual - 1);
      else return;
      e.preventDefault();
    });

    let inicio = Date.now();
    app.querySelector('.zerar').onclick = () => { inicio = Date.now(); };
    const cronometro = app.querySelector('.cronometro');
    const hora = app.querySelector('.hora');
    const dois = (n) => String(n).padStart(2, '0');
    setInterval(() => {
      const s = Math.floor((Date.now() - inicio) / 1000);
      cronometro.textContent = (s >= 3600 ? Math.floor(s / 3600) + ':' : '') + dois(Math.floor(s / 60) % 60) + ':' + dois(s % 60);
      const agora = new Date();
      hora.textContent = dois(agora.getHours()) + ':' + dois(agora.getMinutes());
    }, 500);

    if (canal) {
      canal.onmessage = (e) => {
        if (e.data.tipo !== 'ir') return;
        const i = slides.findIndex((s) => s.id === e.data.id);
        if (i >= 0) ir(i, false);
      };
    }
    ir(indicePorHash(slides), false);
    if (canal) canal.postMessage({ tipo: 'qual' });
  }

  // ---------- Início ----------

  carregarDeck()
    .then((deck) => (ehNotas ? iniciarNotas : iniciarApresentacao)(deck))
    .catch((erro) => {
      console.error(erro);
      const local = location.protocol === 'file:';
      document.getElementById('app').innerHTML = '<p class="aviso"></p>';
      document.querySelector('.aviso').textContent = local
        ? 'O navegador não deixa abrir os slides direto do arquivo.\nRode o apresentar.sh (ou "python3 -m http.server" na pasta apresentacao) e abra o endereço que ele mostrar.'
        : 'Não consegui carregar os slides: ' + erro.message;
    });
})();
