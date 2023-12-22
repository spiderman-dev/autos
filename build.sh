#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt
python manage.py collectstatic --no-input
manage.py createsuperuser 


python manage.py migrate
