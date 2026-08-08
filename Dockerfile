FROM python:3.12.13-slim-bookworm AS builder

WORKDIR /opt/prefect/vienna-data-platform

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen --no-install-project

COPY . .

RUN uv sync --frozen


FROM python:3.12.13-slim-bookworm AS runtime

WORKDIR /opt/prefect/vienna-data-platform

COPY --from=builder /opt/prefect/vienna-data-platform/.venv /opt/prefect/vienna-data-platform/.venv

ENV PATH="/opt/prefect/vienna-data-platform/.venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /opt/prefect/vienna-data-platform ./

RUN useradd --create-home appuser
USER appuser