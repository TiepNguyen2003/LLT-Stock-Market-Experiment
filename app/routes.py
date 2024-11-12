from flask import render_template, request
from app import app
from app.questionForm import QuestionForm


'''@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QuestionForm()
    if request.method == 'POST' and form.validate():
        print("Received answer")
    return render_template('form.html', form=form)'''


@app.route('/')
@app.route('/question', methods=['GET', 'POST'])
def question():
    form = QuestionForm(request.form)
    if request.method == 'POST' and form.validate():
       
        print("Received answer")
    return render_template('form.html', form=form)

