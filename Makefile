.PHONY: run dev
.PHONY: test http wrk/get hey/get hey/post
.PHONY: .fmt .pre-commit
.PHONY: clean .gha .db/create .db/seed run/infra stop/infra

export PYTHONPATH=src
export DB_URI=postgresql+asyncpg://postgres:postgres@localhost:5432/sgerbwd

HOST = 127.0.0.1
PORT = 8000

# --- run server

run:
	./.venv/bin/uvicorn sgerbwd.app:app --port $(PORT) --host 0.0.0.0 --workers 2 --log-level warning

dev:
	./.venv/bin/uvicorn sgerbwd.app:app --port $(PORT) --host $(HOST) --reload --log-level debug

# --- interact with the app

test:
	uv run pytest

http:
	http -b GET http://$(HOST):$(PORT)/users/1

wrk/get:
	wrk -t12 -c500 -d5s --latency "http://$(HOST):$(PORT)/users/1"

hey/get:
	hey -z 10s -c 50 -t 1 http://$(HOST):$(PORT)/users/1

hey/post:
	hey -z 10s -c 100 -t 12 \
       -m POST \
       -H "Content-Type: application/json" \
       -d '{"name":"John","surname":"Hey"}' \
       http://$(HOST):$(PORT)/users

# --- work with code

.fmt:
	uv run ruff format
	uv run ruff check --fix
	uv run mypy --strict --scripts-are-modules --enable-incomplete-feature=NewGenericSyntax src

.pre-commit:
	pre-commit run --all-files

# --- prepare & build

.db/create:
#	rm -f $(DB) || true
	uv run -- alembic upgrade head

run/infra:
	COMPOSE_PROFILES=infra docker compose up -d

stop/infra:
	COMPOSE_PROFILES=infra docker compose down

clean:
	rm -f .docker-data || true

.gha:
	act -W '.github/workflows/ci.yml'
