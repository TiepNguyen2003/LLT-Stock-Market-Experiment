import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MODE = os.environ.get('MODE') or 'development' # MODE should be development or production
    #DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'password'
    #DB_USER = os.environ.get('DB_USER') or 'user'
    #DB_PORT = os.environ.get('DB_PORT') or 3306
    #DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    #DB_NAME = os.environ.get('DB_NAME') or 'db'
    #SQLALCHEMY_DATABASE_URI = "temp"
    #if (MODE == "production"):
        #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        #'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + str(DB_PORT) + '/' + DB_NAME
    #else:

    os.makedirs(os.path.join(basedir, 'data'), exist_ok=True)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data/app.db')

    DEBUG = True
    DEFAULT_BALANCE = int(os.environ.get('EXPERIMENT_BALANCE',2400) )
    PRACTICE_BALANCE = int(os.environ.get('PRACTICE_BALANCE',300)) 
    PRACTICE_QUESTIONS = int(os.environ.get('PRACTICE_QUESTION_COUNT', 3)) # Number of practice questions
    TOTAL_QUESTIONS = int(os.environ.get('EXPERIMENT_QUESTION_COUNT', 24)) # Total questions is the number of non practice questions
    QUESTION_PROMPT = "How much would you invest in this company?"
    SURVEY_LINK = os.environ.get('SURVEY_LINK')

    PORT = os.environ.get('PORT') or 8000
    HOST = os.environ.get('HOST') or '0.0.0.0'
    URL_SCHEME = os.environ.get('URL_SCHEME', 'http')
    WTF_CSRF_TIME_LIMIT = int(os.environ.get("WTF_CSRF_TIME_LIMIT",86400))   # 24 hours

