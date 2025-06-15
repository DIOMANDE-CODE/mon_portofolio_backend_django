# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le projet avant toute commande utilisant manage.py
COPY . .

# Collecte des fichiers statiques
RUN python manage.py collectstatic --noinput

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "portofolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
