FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
RUN mkdir -p temp_uploads

EXPOSE 8000
CMD ["uvicorn", "app.api_main:app", "--host", "0.0.0.0", "--port", "8000"]
