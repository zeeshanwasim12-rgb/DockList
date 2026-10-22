# Install dependencies in an isolated stage so runtime contains no compiler or pip cache.
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN python -m pip install --no-cache-dir --prefix=/install -r requirements.txt

# Test target shares the application dependencies but is excluded from runtime.
FROM builder AS test
COPY requirements-dev.txt .
RUN python -m pip install --no-cache-dir --prefix=/install -r requirements-dev.txt
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/install/lib/python3.12/site-packages \
    TODO_DB_PATH=/tmp/tasks.db
WORKDIR /app
COPY app.py .
COPY templates ./templates
COPY static ./static
COPY tests ./tests
CMD ["python", "-m", "pytest", "-q"]

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TODO_DB_PATH=/data/tasks.db \
    PYTHONPATH=/install/lib/python3.12/site-packages
WORKDIR /app
COPY --from=builder /install /install
COPY app.py .
COPY templates ./templates
COPY static ./static
RUN mkdir -p /data && useradd --system --uid 10001 --home-dir /app appuser \
    && chown appuser:appuser /data
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:5000/health', timeout=2)"
CMD ["python", "app.py"]
