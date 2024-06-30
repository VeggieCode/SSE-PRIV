#!/bin/sh

set -e

python3 -u manage.py wait_for_db
python3 -u manage.py collectstatic --noinput
python3 -u manage.py makemigrations
python3 -u manage.py migrate

gunicorn --bind :8000 seguimiento_egresados.wsgi:application --reload