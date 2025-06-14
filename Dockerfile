# Dockerfile
FROM python:3.11-slim

# Créer le dossier de l'app
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le projet
COPY . .

# Port d'écoute
EXPOSE 8000

# Lancement avec gunicorn
CMD ["gunicorn", "portofolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
