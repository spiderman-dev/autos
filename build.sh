#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input
manage.py createsuperuser --username=uno --email=jheralf09@gmail.com --password=JAHA0109hr --noinput


python manage.py migrate
