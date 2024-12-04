from flask import render_template, request, flash, make_response, redirect, url_for, abort
from app import app, db
from app.questionForm import QuestionForm
from app.idForm import idForm
from app.participantHelper import ParticipantHelper
from app.signoutForm import SignoutForm
from app.models import Response, Participant
from settings.questionContent import QuestionContent
from settings.config import Config


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
        return redirect(url_for('question'))
    
    form = idForm(request.form)
    resp = make_response(render_template('signin.html', form=form, questionContent = "Put in your ID here"))
    
    if request.method == 'POST' and form.validate():

        resp = make_response(redirect(url_for('submit_success')))
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

@app.route('/complete', methods = ['GET', 'POST'])
def complete():
    form = SignoutForm(request.form) # form is the signout button
    if form.validate_on_submit():
        return _signout()

    return render_template('complete.html', form = form, url = Config.SURVEY_LINK)

@app.route('/submit_success', methods=['GET','POST'])
def submit_success():

    #data = request.json
    print(request.form)

    if (request.method == 'POST'):
        print("Switching screen")
        return redirect(url_for('question')) 
    else:
        return render_template('submit_success.html')
    

'''
Switches to the signin page
'''
def _signout():
    resp = make_response(redirect(url_for('idSignup')))
    resp.set_cookie('user_id', 'none', 0)
    return resp
        

@app.route('/question', methods=['GET', 'POST'])
def question():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    
    if user_id is None:
        return redirect(url_for('idSignup'))

    form = QuestionForm(request.form)
    signoutForm = SignoutForm(request.form)
    user = ParticipantHelper.getParticipant(user_id)
    
    if (user is None):
        return _signout()

    mode = "None"
    balance = -1
    trials = -1
    if (user.isPractice()):
        mode = "Practice"
        balance = user.practiceBalance
        trials = Config.PRACTICE_QUESTIONS - user.practiceResponseCount
    else:
        mode = "Experiment"
        balance = user.balance
        trials = Config.TOTAL_QUESTIONS - user.responseCount
    #print(trials)


    if (user.isPractice() is not True and trials <= 0):
        return redirect(url_for('complete'))
    
    if form.validate_on_submit() and request.form['submit'] == "Submit":
        formCost = form.answer.data
        success = ParticipantHelper.addResponse(user_id, formCost)

        if (success):
            print("Switching to submit success")
            return redirect(url_for('submit_success'))
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
                           trials = trials)


