from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
import json
from app import db

class Participant(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    balance: so.Mapped[int] = so.mapped_column(unique = True)
    responses: so.Mapped[str] = so.mapped_column(unique= True)

    def getResponseDict(self):
        return json.load(self.responses)

    def setResponseDict(self, dictionary):
        self.responses = json.dumps(dictionary)

    def __repr__(self):
        return '<User {}>'.format(self.username)


'''
Represents a response to a question.
'''
class Response(db.Model):
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    question_id: so.Mapped[int] = so.mapped_column
    participant_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Participant.id))