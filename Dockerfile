FROM python:3.11-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync --frozen

COPY calculator.py .

CMD ["uv", "run", "python", "calculator.py"]