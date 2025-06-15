# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "portofolio_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
