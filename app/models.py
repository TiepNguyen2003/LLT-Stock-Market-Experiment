from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Participant(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
'''
Represents a response to a question.
'''
class Response(db.Model):
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    question_id: so.Mapped[int] = so.mapped_column
    participant_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Participant.id))