import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
class DevelopmentConfig(Config):
    DEBUG = True
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