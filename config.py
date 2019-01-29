class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'hard to guess string'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = ''


config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
