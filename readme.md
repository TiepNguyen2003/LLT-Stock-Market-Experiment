# README


## Setup

Requires python 3.12

1. Install the [virtual environment](https://www.arch.jhu.edu/python-virtual-environments/) for python3
2. Run "pip install -r requirements.txt"
3. Copy example.env, rename it to .env and put in your configuration variables.
4. Run startup.sh or the commands listed in it.
5. Deployment can be ran with boot.sh (reccommended for Linux) or for local hosting, run deploy.py

Advanced users can use the provided dockerfiles to host

## Implementation Details
- The experiment website was built with using the Python Flask framework in order to receive information. For the frontend, we used primarily HTML, CSS and Javascript to deliver interactivity. The backend, written with Flask, used SQLAlchemy as a layer over the MySQL database. This website was deployed on a Docker container on a VM hosted in the cloud that used NGINX as a router. No identifiable data was held on 3rd party environments.

## Contact

For programming/deployment questions, contact Tiep Nguyen at tnguyen668@ucmerced.edu


