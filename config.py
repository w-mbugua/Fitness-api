import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://name:password@localhost/test_db_name'


class StagingConfig(Config):
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://name:password@localhost/db_name'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'staging': StagingConfig,
    'production': ProdConfig,
    'test': TestConfig
}