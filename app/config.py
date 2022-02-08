import os
from dotenv import load_dotenv


load_dotenv()

class Config(object):
    SECRET_KEY = os.environ['KEY']
    
class DevelopentConfig(Config):
    DEBUG = True
    
class HostConfig(Config):
    DEBUG = False
    