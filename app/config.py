import os


class Config:

    def init_app(self, app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/development_data.sqlite'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/test_data.sqlite'


config = {
        'production': ProductionConfig(),
        'development': DevelopmentConfig(),
        'test': TestConfig(),
        'default': DevelopmentConfig()
        }

