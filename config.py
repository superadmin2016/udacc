import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SUBJECT_PREFIX = '[UDACC]'
    MAIL_SENDER = 'UDACC Admin <udac.dev@gmail.com>'
        
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'udac.dev@gmail.com'
    MAIL_PASSWORD = 'password_123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password_123@localhost/udacc_dev'        
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password_123@localhost/udacc_testing'
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password_123@localhost/udacc_prod'
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}