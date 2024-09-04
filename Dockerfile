# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de requisitos para o diretório de trabalho
COPY src/requirements.txt requirements.txt

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para o diretório de trabalho
COPY . .

# Expor a porta 8080 para acesso externo
EXPOSE 8080

# Comando para inicializar o banco de dados
RUN python src/create_db.py

# Comando para adicionar usuários a partir do arquivo CSV
RUN python src/adduser.py

# Comando para rodar o servidor Flask
CMD ["python", "src/softdes.py", "--host=0.0.0.0", "--port=8080"]