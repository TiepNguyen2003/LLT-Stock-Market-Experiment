import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db

'''
why do we need this again? i think this is an entrypoint for one of the production things
'''
app = create_app()
