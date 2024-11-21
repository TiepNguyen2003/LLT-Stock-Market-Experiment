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
from settings.config import Config

class Participant(db.Model):
    __tablename__ = 'participants'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    balance: so.Mapped[int] = so.mapped_column(unique = False)
    practiceBalance: so.Mapped[int] = so.mapped_column(unique= False)
    responseCount: so.Mapped[int] = so.mapped_column(unique = False)
    practiceResponseCount: so.Mapped[int] = so.mapped_column(unique = False)
    
    responses: so.Mapped[List["Response"]] = so.relationship("Response", back_populates="participant")

    def __init__(self, id = None, balance = DEFAULT_BALANCE, practiceBalance = Config.PRACTICE_BALANCE):
        self.id = id
        self.balance = balance
        self.practiceBalance = practiceBalance
        self.practiceResponseCount = 0
        self.responseCount = 0
    def __repr__(self):
        return '<User {}>'.format(self.id)

    def addResponse(self, response : 'Response'):
        if (self.validResponse(response) is False):
            raise ValueError("Cost is not valid")
          
        if (self.isPractice()):
            self.practiceResponseCount = self.practiceResponseCount + 1
            self.responses.append(response)
            self.practiceBalance = self.practiceBalance - response.cost

            response.trial = "P" + str(self.practiceResponseCount)
        else:
            self.responseCount = self.responseCount + 1
            self.responses.append(response)
            self.balance = self.balance - response.cost

            response.trial = str(self.responseCount)


        db.session.commit()

    '''
        Checks if a response is able to be added to this object
    '''
    def validResponse(self, response : 'Response'):    
        compVal = -1
        if (self.isPractice() is True):
            compVal = self.practiceBalance
        else:
            compVal = self.balance

        if (compVal >= response.cost):
            return True
        else:
            return False
        
    def isPractice(self):
        if (self.practiceResponseCount >= Config.PRACTICE_QUESTIONS):
            return False
        else:
            return True

class Response(db.Model):
    __tablename__ = 'responses'
    
    response_id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)

    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.id", name="fk_responses_participant_id")
    )
    participant: so.Mapped["Participant"] = so.relationship("Participant", back_populates="responses")

    
    # Cost is a positive value that represents how much the participant pent in this response.
    cost: so.Mapped[int] = so.mapped_column(unique= False)
    trial: so.Mapped[str] = so.mapped_column(unique=False)  # the response order

    def __init__(self, cost):
        
        self.cost = cost
        
    def __repr__(self):
        return f'<Response {self.id}>'