# Usa uma imagem base do Python mais leve
FROM python:3.9-slim-buster

# Define variáveis de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala as dependências do sistema necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Cria um usuário não-root para executar a aplicação
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expõe a porta 5000 (usada pelo Flask)
EXPOSE 5000

# Define o healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Define o comando para rodar o aplicativo
CMD ["python", "main.py"]