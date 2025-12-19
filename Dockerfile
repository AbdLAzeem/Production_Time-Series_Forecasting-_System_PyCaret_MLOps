'''
Build & run"
bash: 
docker build -t ts-forecasting .
docker run -p 8000:8000 ts-forecasting
'''
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
