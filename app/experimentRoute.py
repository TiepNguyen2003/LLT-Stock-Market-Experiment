import csv
import io
from flask import Blueprint, render_template, request, flash, make_response, redirect, send_file, url_for, abort
from app.forms.questionForm import QuestionForm
from app.forms.downloadForm import downloadForm
from app.forms.idForm import idForm
from app.models.models import Participant, Response
from app.models.participantHelper import ParticipantHelper
from app.forms.signoutForm import SignoutForm
from app import db;
from config import Config
import pandas as pd
from io import BytesIO, StringIO


experiment = Blueprint('experiment', __name__, template_folder='templates')


@experiment.route('/download_responses', methods=['GET', 'POST'])
def download_responses():
    '''responses = db.session.query(Response).all()

    response = make_response(df.to_csv(pth))
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    response.headers["Content-type"] = "text/csv"'''
    signoutForm = SignoutForm(request.form)
    form = downloadForm(request.form)

    if signoutForm.validate_on_submit() and request.form['submit'] == "Sign out":
        return _signout()
    
    if form.validate_on_submit():
        contentType = form.content_type.data
        query = None
        if contentType == "responses":
            query = db.session.query(Response).all()
        elif contentType == "participants":
            query = db.session.query(Participant).all()
        else:
            return abort(400, "Invalid content type")
        si = StringIO()
        writer = csv.writer(si)
        if query:
            # Write headers using the first object
            writer.writerow(query[0].__table__.columns.keys())
            for row in query:
                writer.writerow([getattr(row, col) for col in row.__table__.columns.keys()])

        output = BytesIO()
        output.write(si.getvalue().encode('utf-8'))
        output.seek(0)

        return send_file(
            output,
            mimetype='text/csv',
            as_attachment=True,
            download_name=f"{contentType}.csv"
        )


    
    return render_template('download_responses.html',
                           form=form,
                           signout= signoutForm)
    





@experiment.route('/', methods=['GET', 'POST'])
def idSignup():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    if user_id is not None:  # If the cookie is not set, handle the case (e.g., redirect or show an error)
        return redirect(url_for('experiment.question'))
    
    form = idForm(request.form)
    resp = make_response(render_template('signin.html', form=form, questionContent = "Put in your user ID here"))
    
    if request.method == 'POST' and form.validate():

        resp = make_response(redirect(url_for('experiment.submit_success')))
        user_id = form.answer.data
        
        if (ParticipantHelper.getParticipant(user_id) is None):
            print("Adding participant " + str(user_id))
            ParticipantHelper.addParticipant(user_id)
        
        resp.set_cookie('user_id', str(user_id), max_age=60*60*3)  # expires after 3 hours
        
        return resp

    return resp

@experiment.route('/complete', methods = ['GET', 'POST'])
def complete():
    form = SignoutForm(request.form) # form is the signout button
    if form.validate_on_submit():
        return _signout()

    return render_template('complete.html', form = form, url = Config.SURVEY_LINK)

@experiment.route('/submit_success', methods=['GET','POST'])
def submit_success():

    #data = request.json
    #print(request.form)

    if (request.method == 'POST'):
        print("Switching screen")
        return redirect(url_for('experiment.question')) 
    else:
        return render_template('submit_success.html')
    

'''
Switches to the signin page
'''
def _signout():
    resp = make_response(redirect(url_for('experiment.idSignup')))
    resp.set_cookie('user_id', 'none', 0)
    return resp
        

@experiment.route('/question', methods=['GET', 'POST'])
def question():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    
    if user_id is None:
        return redirect(url_for('experiment.idSignup'))

    form = QuestionForm(request.form)
    signoutForm = SignoutForm(request.form)
    user = ParticipantHelper.getParticipant(user_id)
    
    if (user is None):
        return _signout()

    mode = "None"
    balance = -1
    trial = -1
    maxTrials = -1
    if (user.isPractice()):
        mode = "Practice"
        balance = user.practiceBalance
        trial = user.practiceResponseCount + 1
        maxTrials = Config.PRACTICE_QUESTIONS
    else:
        mode = "Experiment"
        balance = user.balance
        trial = user.responseCount + 1
        maxTrials = Config.TOTAL_QUESTIONS
    #print(trials)


    if (user.isPractice() is not True and trial > Config.TOTAL_QUESTIONS):
        return redirect(url_for('experiment.complete'))
    
    if form.validate_on_submit() and request.form['submit'] == "Submit":
        formCost = form.answer.data
        success = ParticipantHelper.addResponse(user_id, formCost)

        if (success):
            print("Switching to submit success")
            return redirect(url_for('experiment.submit_success'))
        else:
            print("Invalid response cost")
        
    if signoutForm.validate_on_submit() and request.form['submit'] == "Sign out":
        return _signout()
        
        

    return render_template('form.html', 
                           form=form, 
                           signout=signoutForm,
                           mode=mode, 
                           questionContent = Config.QUESTION_PROMPT, 
                           currentBalance = balance,
                           trial = trial,
                           maxTrials = maxTrials)
