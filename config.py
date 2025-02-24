import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'trestigrestristescomeramtrigo'

    def init_app(self, app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data', 'development_data.sqlite')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data', 'test_data.sqlite')


config = {
        'production': ProductionConfig(),
        'development': DevelopmentConfig(),
        'test': TestConfig(),
        'default': DevelopmentConfig()
        }

