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
- API routes are in experimentroute. We use SQLAlchemy ORM to represent users and responses.

## Contact

For programming/deployment questions, contact Tiep Nguyen at tiep123@trieuvan.com


