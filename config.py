import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'password'
    DB_USER = os.environ.get('DB_USER') or 'user'
    DB_PORT = os.environ.get('DB_PORT') or 3306
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_NAME = os.environ.get('DB_NAME') or 'db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + str(DB_PORT) + '/' + DB_NAME

    DEBUG = True
    DEFAULT_BALANCE = 2400
    PRACTICE_BALANCE = 1000
    PRACTICE_QUESTIONS = 1 # Number of practice questions
    TOTAL_QUESTIONS = 24 # Total questions is the number of non practice questions
    QUESTION_PROMPT = "How much would you invest in this company?"
    SURVEY_LINK = "https://ucmerced.az1.qualtrics.com/jfe/form/SV_eu5zvGfv4ZasnD8"

    PORT = os.environ.get('PORT') or 8000
    HOST = os.environ.get('HOST') or '0.0.0.0'
    URL_SCHEME = os.environ.get('URL_SCHEME', 'http')