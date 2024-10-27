# syntax=docker/dockerfile:1

FROM python:3.13.0-alpine3.20 AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


FROM python:3.13.0-alpine3.20

COPY --from=builder --chown=app:app /app /app

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="src"

CMD ["uvicorn", "sgerbwd.app:app", "--port", "8000", "--host", "0.0.0.0", "--log-level", "warning"]
