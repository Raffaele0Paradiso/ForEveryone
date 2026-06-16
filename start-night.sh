#!/usr/bin/env bash
set -euo pipefail

export SEARXNG_SECRET="${SEARXNG_SECRET:-$(python - <<'PY'
import secrets
print(secrets.token_hex(32))
PY
)}"

mkdir -p data/out

docker compose up -d --build

echo "Stack avviato."
echo "Ollama:   http://localhost:11434"
echo "SearXNG:  http://localhost:8080"
echo "Tor SOCKS: localhost:9050"
echo "Agent white:  http://localhost:8001/health"
echo "Agent gray:   http://localhost:8002/health"
echo "Agent dark:   http://localhost:8003/health"