#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py createsuperuser --no-input --username=dos --email=jheralf09@gmail.com --password=JAHA0109


python manage.py migrate
