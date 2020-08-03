import os


basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.split(basedir)[0]


assert 'APP_ENV' in os.environ, 'MAKE SURE TO SET AN ENVIRONMENT'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    BASEDIR = basedir
    LOG_FOLDER = os.path.join(BASEDIR, 'logs')
    LOG_FILENAME = 'app.log'
    LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILENAME)
    SQL_URI = 'sqlite:///app.db'


class TestConfig(Config):
    SQL_URI = 'sqlite:///temp.db'


app_config = TestConfig if os.environ['APP_ENV'].upper() == 'TEST' else Config
