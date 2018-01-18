class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECURITY_PASSWORD_SALT = 'test_this_is_a_test_please_change_me'
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    WEBAPP_BASE_URL = "http://localhost:8080"


class TestingConfig(Config):
    TESTING = True
