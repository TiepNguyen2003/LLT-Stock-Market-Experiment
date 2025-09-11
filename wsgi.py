import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db

'''
Entrypoint for wsgi 
'''
app = create_app()
