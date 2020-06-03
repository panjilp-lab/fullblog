import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SECRET_KEY = 'did you finding bug?'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.sqlite' % APPLICATION_DIR
    SQLALCHEMY_TRACK_MODIFICATION = False
