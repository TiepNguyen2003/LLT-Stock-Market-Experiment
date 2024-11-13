from flask import render_template, request, flash, make_response, redirect, url_for
from app import app, db
from app.questionForm import QuestionForm
from app.idForm import idForm

'''@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QuestionForm()
    if request.method == 'POST' and form.validate():
        print("Received answer")
    return render_template('form.html', form=form)'''


@app.route('/', methods=['GET', 'POST'])
def idSignup():
    
    form = idForm(request.form)
    resp = make_response(render_template('form.html', form=form, questionContent = "Put in your ID here"))
    
    if request.method == 'POST' and form.validate():

        resp = make_response(redirect(url_for('info')))
        user_id = form.answer.data
        
        user = db.session
        
        resp.set_cookie('user_id', str(user_id), max_age=60*60*3)  # expires after 3 hours
        
        return resp
    else:
        #print("Hello world")
        print(form.errors)

    return resp

@app.route('/info')
def info():
    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    
    if user_id is None:  # If the cookie is not set, handle the case (e.g., redirect or show an error)
        return "User ID not found in cookies.", 400  # Example of handling missing user_id
    
    participantTest = {
        'id': user_id,
        'balance': 2500  # Store balance as an integer
    }

    return render_template('info.html', Participant=participantTest)


@app.route('/question', methods=['GET', 'POST'])
def question():

    user_id = request.cookies.get('user_id')  # Get the user_id from cookies
    
    if user_id is None:
        return redirect(url_for('idSignup'))

    form = QuestionForm(request.form)
    if request.method == 'POST' and form.validate():
       
        print("Received answer")
    return render_template('form.html', form=form, questionContent = "Put in your question response here")

