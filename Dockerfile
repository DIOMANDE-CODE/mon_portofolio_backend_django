# Utilise une image légère Python
FROM python:3.11-slim

# Évite les interactions dans les scripts Python (affichage immédiat)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Déclare le dossier de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances système utiles (Cloudinary, PostgreSQL, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && apt-get clean

# Copie tout le code source
COPY . .

# Charge les variables d'environnement
# ATTENTION : si tu fais collectstatic ici, il te faut accès à la DB et Cloudinary
# C'est souvent mieux de le faire dans une étape de déploiement/CI

# === Optionnel mais utile en développement ===
# RUN python manage.py collectstatic --noinput || true

# Commande finale : lance Gunicorn
CMD ["gunicorn", "portofolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
