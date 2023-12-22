#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py createsuperuser --user="admin" --email="" --password="JAHA0109hr#" --no-input
python manage.py migrate
