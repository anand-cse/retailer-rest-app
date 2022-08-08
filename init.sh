#!/bin/bash

set +e
export FLASK_APP=manage.py
flask db init
flask db migrate
set -e
flask db upgrade
exec python manage.py run