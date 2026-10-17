# Estágio 1: Build (instala dependências)
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Estágio 2: Runtime (imagem final, mais leve)
FROM python:3.11-slim
WORKDIR /app
# Copia as dependências instaladas do estágio anterior
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
# Copia o código
COPY ./app ./app
EXPOSE 8000
# Roda o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
