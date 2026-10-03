#!/usr/bin/env bash
# Abre a apresentação no navegador, sem precisar do claude.ai nem de internet.
# Uso: ./apresentar.sh [porta]
# Sobe um servidor local só nesta máquina (o navegador não lê os slides por file://).
# Para encerrar, aperte Ctrl+C neste terminal.
set -euo pipefail
cd "$(dirname "$0")/.."  # serve oficina-ia/ inteira: slides e programas/

porta="${1:-8765}"
while python3 -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', $porta)) != 0)"; do
  porta=$((porta + 1))
done

python3 -m http.server "$porta" --bind 127.0.0.1 >/dev/null 2>&1 &
servidor=$!
trap 'kill $servidor 2>/dev/null' EXIT INT TERM

endereco="http://127.0.0.1:$porta/apresentacao/player/"
for _ in $(seq 20); do
  python3 -c "import socket,sys; s=socket.socket(); sys.exit(s.connect_ex(('127.0.0.1', $porta)))" && break
  sleep 0.2
done

echo "Apresentação em: $endereco"
echo "Atalhos: → próximo, ← anterior, F tela cheia, N notas, ? ajuda. Ctrl+C aqui para encerrar."
if command -v xdg-open >/dev/null; then xdg-open "$endereco" >/dev/null 2>&1 || true
elif command -v open >/dev/null; then open "$endereco" || true
fi
wait "$servidor"
