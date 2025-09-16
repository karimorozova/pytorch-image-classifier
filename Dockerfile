FROM python:3.11-slim

WORKDIR /app

# Copy model, code, requirements
COPY model/ /app/model/
COPY app/ /app/app/
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
