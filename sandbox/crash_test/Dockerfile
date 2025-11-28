FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the codebase (for imports)
COPY body/ body/
COPY buds/ buds/
COPY venom/ venom/
COPY sandbox/ sandbox/

# Default command (can be overridden)
CMD ["python", "venom/stress_test_ollama.py"]
