import os

class BaseConfig(object):

    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

    #SQLALCHEMY_DATABASE_URI = #'mysql://empirical:state@10.41.71.220:3306/empirical' 
    #SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    #DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    SECRET_KEY = "secret"

    JSON_AS_ASCII = False
 
class DevConfig(BaseConfig):
    pass