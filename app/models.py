from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
import json

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship



from app import db, DEFAULT_BALANCE


class Participant(db.Model):
    __tablename__ = 'participants'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    balance: so.Mapped[int] = so.mapped_column(unique = False)
    responseCount: so.Mapped[int] = so.mapped_column(unique = False)

    
    responses: so.Mapped[List["Response"]] = so.relationship("Response", back_populates="participant")

    def __init__(self, id = None, balance = DEFAULT_BALANCE):
        self.id = id
        self.balance = balance
        self.responseCount = 0
    def __repr__(self):
        return '<User {}>'.format(self.id)

    def addResponse(self, response : 'Response'):
        if (self.validResponse(response) is False):
            raise ValueError("Cost is not valid")
          
        self.responseCount = self.responseCount + 1
        self.responses.append(response)
        self.balance = self.balance - response.cost

        response.index = self.responseCount


        db.session.commit()

    '''
        Checks if a response is able to be added to this object
    '''
    def validResponse(self, response : 'Response'):    
        if (self.balance >= response.cost):
            return True
        else:
            return False

class Response(db.Model):
    __tablename__ = 'responses'
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    questionNumber: so.Mapped[int] = so.mapped_column(unique=False) # question number as assigned by study
    questionContent: so.Mapped[str] = so.mapped_column(unique=False) # content of the question


    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.id", name="fk_responses_participant_id")
    )
    participant: so.Mapped["Participant"] = so.relationship("Participant", back_populates="responses")

    
    # Cost is a positive value that represents how much the participant pent in this response.
    cost: so.Mapped[int] = so.mapped_column(unique= False)
    index: so.Mapped[int] = so.mapped_column(unique = False) # the response order

    def __init__(self, cost, questionNumber, questionContent= "NONE"):
        
        self.cost = cost
        self.questionNumber = questionNumber
        self.questionContent = questionContent
        
    def __repr__(self):
        return f'<Response {self.id}: {self.content}>'