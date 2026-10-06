#!/usr/bin/env bash
# Gera um PDF da apresentação, um slide por página, a partir do player local.
# Uso: ./gerar-pdf.sh [arquivo-de-saida]   (padrão: pdf/oficina-ia.pdf, nesta pasta)
# Precisa do Google Chrome ou do Chromium; para usar outro, CHROME=/caminho ./gerar-pdf.sh
# Slides com "hidden" ficam de fora, vídeo vira um quadro parado (precisa do ffmpeg; sem ele,
# fica um retângulo com um play) e as notas do apresentador não entram.
set -euo pipefail
aqui="$(cd "$(dirname "$0")" && pwd)"
saida="${1:-$aqui/pdf/oficina-ia.pdf}"
mkdir -p "$(dirname "$saida")"
saida="$(cd "$(dirname "$saida")" && pwd)/$(basename "$saida")"

chrome="${CHROME:-}"
for nome in google-chrome google-chrome-stable chromium chromium-browser; do
  [ -n "$chrome" ] && break
  chrome="$(command -v "$nome" || true)"
done
if [ -z "$chrome" ]; then
  echo "Não achei o Google Chrome nem o Chromium. Instale um deles ou rode: CHROME=/caminho/do/navegador $0" >&2
  exit 1
fi

# Um quadro parado de cada vídeo dos slides, para o player pôr no lugar dele (pasta apagada no fim).
quadros="$aqui/.quadros-pdf"
perfil="$(mktemp -d)"
servidor=""
trap '[ -n "$servidor" ] && kill $servidor 2>/dev/null; rm -rf "$perfil" "$aqui/.quadros-pdf"' EXIT INT TERM
if command -v ffmpeg >/dev/null; then
  mkdir -p "$quadros"
  grep -oh '<video[^>]*src="[^"]*"' "$aqui"/slides/*.html | sed 's/.*src="//; s/"$//' | sort -u | while read -r video; do
    nome="$(basename "${video%.*}")"
    ffmpeg -nostdin -loglevel error -y -ss 1 -i "$aqui/$video" -frames:v 1 -q:v 3 "$quadros/$nome.jpg" \
      || echo "Aviso: não consegui tirar um quadro de $video" >&2
  done
else
  echo "Aviso: sem o ffmpeg, os vídeos saem como um retângulo com um play." >&2
fi

cd "$aqui/.."  # serve oficina-ia/ inteira (slides e os quadros dos vídeos)

porta=8765
while python3 -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', $porta)) != 0)"; do
  porta=$((porta + 1))
done

python3 -m http.server "$porta" --bind 127.0.0.1 >/dev/null 2>&1 &
servidor=$!

for _ in $(seq 20); do
  python3 -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', $porta)))" && break
  sleep 0.2
done

echo "Gerando o PDF (leva alguns segundos)..."
rm -f "$saida"
"$chrome" --headless --disable-gpu --user-data-dir="$perfil" --no-pdf-header-footer \
  --autoplay-policy=no-user-gesture-required --virtual-time-budget=20000 \
  --print-to-pdf="$saida" "http://127.0.0.1:$porta/apresentacao/player/?imprimir" >/dev/null 2>&1 || true

if [ ! -s "$saida" ]; then
  echo "O navegador não gerou o PDF." >&2
  exit 1
fi
paginas=""
if command -v pdfinfo >/dev/null; then
  paginas=", $(pdfinfo "$saida" | awk '/^Pages:/ {print $2}') páginas"
fi
echo "PDF pronto: $saida ($(du -h "$saida" | cut -f1)$paginas)"
