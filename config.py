class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "hard to guess string"
    # CELERY SETTING
    CELERY_TIMEZONE = "Asia/Shanghai"
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # CELERY SETTING
    CELERY_BROKER_URL = "sqla+sqlite:///:memory:"
    CELERY_RESULT_BACKEND = "db+sqlite:///:memory:"


config = {
    "develop": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
