from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
import json


from app import db, DEFAULT_BALANCE


class Participant(db.Model):
    __tablename__ = 'participants'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    balance: so.Mapped[int] = so.mapped_column(unique = False)
  
    first_response_id: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey('responses.id'), nullable=True)
    first_response = so.relationship("Response", uselist=False, foreign_keys=[first_response_id], lazy = "joined")

    def __init__(self, id = None, balance = DEFAULT_BALANCE):
        self.id = id
        self.balance = balance
    def __repr__(self):
        return '<User {}>'.format(self.id)

    def addResponse(self, response : 'Response'):
        if (self.validResponse(response) is False):
            raise ValueError("Cost is not valid")


        if (self.first_response_id is None):
            self.first_response_id = response.id
            self.first_response = response
            self.balance -= response.cost

            #response.participant = self
            response.participant_id = self.id

           

        else:
            cur = self.first_response
            while(cur.next_response_id is not None):
                cur = cur.next_response

            cur.addResponse(response)
        
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
    questionNumber: so.Mapped[int] = so.mapped_column(unique=False)
    # Cost is a positive value that represents how much the participant pent in this response.
    cost: so.Mapped[int] = so.mapped_column(nullable=False)
    
    # Foreign key to the participant, for the first response
    participant_id: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey('participants.id'), nullable=True)
    #participant = so.relationship("Participant", foreign_keys=[participant_id], lazy="joined")
    
    # Foreign key to the next response in the chain (self-referencing)
    #next_response_id: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey('responses.id'), nullable=True)
    next_response = so.relationship("Response", foreign_keys=[id])

    def __init__(self, cost, questionNumber):
        
        self.cost = cost
        self.questionNumber = questionNumber
        


    def addResponse(self, response):
        if (self.next_response_id is not None):
            raise ValueError("Response already has a next response!")

        #response.participant = self.participant
        response.participant_id = self.id   
        response.next_response = self.next_response
        #response.next_response_id = self.next_response_id

        db.session.commit()

    def __repr__(self):
        return f'<Response {self.id}: {self.content}>'