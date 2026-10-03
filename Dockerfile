FROM python:3.11-slim

WORKDIR /app

# Copy uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency/project metadata
COPY pyproject.toml uv.lock README.md ./

# Copy source before uv sync
COPY src ./src

# Install dependencies and project
RUN uv sync --frozen

# Copy application files
COPY calculator.py .

CMD ["uv", "run", "python", "calculator.py"]