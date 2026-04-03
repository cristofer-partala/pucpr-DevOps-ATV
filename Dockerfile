# Imagem base
FROM python:3.10

# Pasta dentro do container
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta
EXPOSE 8000

# Rodar aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]