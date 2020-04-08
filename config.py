import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEPLOYMENT_ENVIRONMENT = os.environ.get('ENVIRONMENT') or 'dev'
