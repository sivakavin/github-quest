FROM python:3.11-slim

WORKDIR /app

# Copy uv from the official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "python", "calculator.py"]