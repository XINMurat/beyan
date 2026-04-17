# Use a slim Python image for efficiency
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (git for drift detection)
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies (including pre-built binaries for tiktoken)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install the package in editable mode or standard mode
RUN pip install --no-cache-dir .

# Set default environment variables
ENV PYTHONUNBUFFERED=1
ENV BEYAN_DOCKER=1

# Set entrypoint to run the module directly
ENTRYPOINT ["python", "-m", "analyzer"]

# Default command (help)
CMD ["--help"]
