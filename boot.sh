#!/bin/bash
# this script is used to boot a Docker container
ls
flask db init
flask db migrate -m "First Migration"
flask db upgrade


exec gunicorn -b :8000 --access-logfile - --error-logfile - appserver:app