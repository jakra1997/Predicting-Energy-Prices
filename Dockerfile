# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for dependency caching
COPY Requirements.txt .

# Install xgboost first (separately because it's large)
RUN pip install --no-cache-dir --default-timeout=100 --retries=5 xgboost

# Then install the rest of the dependencies
RUN pip install --no-cache-dir --default-timeout=100 --retries=5 -r Requirements.txt

# Copy the rest of your project
COPY . .

# Expose API port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
