from app import app, db, DEFAULT_BALANCE
from flask import request
from app.models import Participant, Response


'''
Class that contains methods to add and update the Participants to a database
'''
class ParticipantHelper():

    def getParticipant(id):
        participant = Participant.query.get(id)

        if (participant):
            return participant
        else:
            return None
    
    def addParticipant(id):
        if (ParticipantHelper.getParticipant(id) is not None):
            raise ValueError("Participant " + id + " already exists")
        
        participant = Participant(id)
        db.session.add(participant)
        db.session.commit()
    def addResponse(participantID, responseCost, questionNumber):
        participant = ParticipantHelper.getParticipant(participantID)
        if (participant is None):
            raise ValueError("Participant " + id + " does not exist")

        response = Response(responseCost, questionNumber)
        if (participant.validResponse(response) == False):
            return False

        participant.addResponse(response)


        
    


