#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="${PORT:-8080}"

cleanup() {
    kill "${WATCH_PID:-}" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

# TypeScript compiler in watch mode
(
    cd "$ROOT_DIR/frontend"
    npm run watch
) &

WATCH_PID=$!

# BrowserSync must serve the complete repository,
# because frontend/ imports files from libs/.
cd "$ROOT_DIR"

cd ~/workspace/production/CR-DSS

./frontend/node_modules/.bin/browser-sync start \
    --server . \
    --files \
        "frontend/dist/**/*.js" \
        "frontend/**/*.html" \
        "frontend/styles/**/*.css" \
    --startPath "/frontend/" \
    --port 8080 \
    --logLevel debug