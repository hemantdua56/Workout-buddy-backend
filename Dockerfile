FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ app/
RUN mkdir -p temp_uploads

# Expose FastAPI port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "app.api_main:app", "--host", "0.0.0.0", "--port", "8000"]
