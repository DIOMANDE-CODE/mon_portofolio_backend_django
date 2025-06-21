# Utilisation d'une image officielle de python
FROM python:3.12-slim

# Creation de dossier de travail du conteneur
WORKDIR /app

# Copie de tous les fichiers du projet
COPY . .

# Installation des dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Collection des fichiers statics du projet
RUN python manage.py collectstatic --noinput || true

# exposer le port de django
EXPOSE 8000

# Lancement du serveur
CMD ["gunicorn","portofolio_backend.wsgi:application","--bind","0.0.0.0:8000"]