# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.9

FROM python:${PYTHON_VERSION}-slim-bookworm AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    PATH="/var/www/tasknote/.venv/bin:$PATH"

WORKDIR /var/www/tasknote

RUN apt update && apt upgrade -y \
    && apt install -y curl build-essential default-libmysqlclient-dev pkg-config \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt install -y nodejs \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --compile-bytecode --no-editable

ADD . /var/www/tasknote

RUN mkdir -p /var/www/tasknote/static && chmod -R 777 /var/www/tasknote/static
RUN touch /var/www/tasknote/debug.log && chmod 777 /var/www/tasknote/debug.log

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --compile-bytecode --no-editable

CMD ["uv", "run", "uwsgi", "--ini", "tasknote_uwsgi.ini"]
