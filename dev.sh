#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="${PORT:-8080}"

cleanup() {
    kill "${FRONTEND_WATCH_PID:-}" 2>/dev/null || true
    kill "${API_WATCH_PID:-}" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

# start API php Development Server on port 8000
start_api_server() {
    local cmd="cd $ROOT_DIR/api && php -S localhost:8000 -t public"

    if command -v gnome-terminal &>/dev/null; then
        gnome-terminal -- bash -c "$cmd; exec bash" &
    elif command -v konsole &>/dev/null; then
        konsole -e bash -c "$cmd; exec bash" &
    elif command -v xfce4-terminal &>/dev/null; then
        xfce4-terminal -e "bash -c '$cmd; exec bash'" &
    elif command -v xterm &>/dev/null; then
        xterm -hold -e "bash -c '$cmd'" &
    else
        echo "No Terminal found – starting API Server as Background process."
        (
            cd "$ROOT_DIR/api"
            php -S localhost:8000 -t public
        ) &
    fi

    API_WATCH_PID=$!
}   
start_api_server

# TypeScript compiler in watch mode
(
    cd "$ROOT_DIR/frontend"
    npm run watch
) &
FRONTEND_WATCH_PID=$!

# BrowserSync must serve the complete repository,
# because frontend/ imports files from libs/.
cd "$ROOT_DIR"

./frontend/node_modules/.bin/browser-sync start \
    --server . \
    --files \
        "frontend/dist/**/*.js" \
        "frontend/**/*.html" \
        "frontend/styles/**/*.css" \
    --startPath "/frontend/" \
    --port 8080 \
    --logLevel debug