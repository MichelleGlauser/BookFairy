web: python manage.py runserver 0:$PORT collectstatic --noinput; venv/bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT proj/prod_settings.py