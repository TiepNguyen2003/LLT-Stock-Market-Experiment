#!/bin/bash
# this script is used to boot a Docker container
while true; do
    #flask db init
    #flask db migrate -m "First Migration"
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
exec waitress-serve --host 0.0.0.0 --port=8000 --call app:create_app