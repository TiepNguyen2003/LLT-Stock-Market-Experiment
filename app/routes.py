from flask import render_template, request, flash, make_response, redirect, url_for
from app import app, db
from app.questionForm import QuestionForm
from app.idForm import idForm
from app.participantHelper import ParticipantHelper
from app.signoutForm import SignoutForm
from app.models import Response, Participant


'''@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QuestionForm()
    if request.method == 'POST' and form.validate():
        print("Received answer")
    return render_template('form.html', form=form)'''


@app.route('/', methods=['GET', 'POST'])
def idSignup():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    if user_id is not None:  # If the cookie is not set, handle the case (e.g., redirect or show an error)
        return redirect(url_for('info'))
    
    form = idForm(request.form)
    resp = make_response(render_template('form.html', form=form, questionContent = "Put in your ID here"))
    
    if request.method == 'POST' and form.validate():

        resp = make_response(redirect(url_for('info')))
        user_id = form.answer.data
        
        if (ParticipantHelper.getParticipant(user_id) is None):
            print("Adding participant " + str(user_id))
            ParticipantHelper.addParticipant(user_id)
        
        resp.set_cookie('user_id', str(user_id), max_age=60*60*3)  # expires after 3 hours
        
        return resp
    else:
        #print("Hello world")
        print(form.errors)

    return resp

@app.route('/info', methods=["GET", "POST"])
def info():

    form = SignoutForm(request.form)
    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    

    if user_id is None:  # If the cookie is not set, handle the case (e.g., redirect or show an error)
        return redirect(url_for('idSignup'))
    
    if request.method == 'POST' and form.validate():
        resp = make_response(redirect(url_for('idSignup')))
        resp.set_cookie('user_id', '', expires=0)
        return resp

    participant = ParticipantHelper.getParticipant(user_id)
    

    return render_template('info.html', form = form, Participant=participant)


@app.route('/question', methods=['GET', 'POST'])
def question():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    
    if user_id is None:
        return redirect(url_for('idSignup'))

    form = QuestionForm(request.form)
    if request.method == 'POST' and form.validate():
        formCost = form.answer.data
        success = ParticipantHelper.addResponse(user_id, formCost, -5)

        if (success):
            return redirect(url_for('info'))
        else:
            print("Invalid response cost")
        

    return render_template('form.html', form=form, questionContent = "Put in your question response here")

