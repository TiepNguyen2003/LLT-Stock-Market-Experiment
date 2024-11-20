import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    DEBUG = True
    DEFAULT_BALANCE = 2400
    PRACTICE_BALANCE = 1000
    PRACTICE_QUESTIONS = 1 # Number of practice questions
    TOTAL_QUESTIONS = 24 # Total questions is the number of non practice questions
    QUESTION_PROMPT = "How much would you invest in this company?"