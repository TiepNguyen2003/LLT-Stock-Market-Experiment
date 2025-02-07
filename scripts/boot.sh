#!/bin/bash
# this script is used to boot a Docker container
flask db init
flask db migrate -m "First Migration"
flask db upgrade