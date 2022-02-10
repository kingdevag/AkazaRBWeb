from urllib import parse
from dotenv import load_dotenv


load_dotenv()

TOKEN = "OTMzODYwNDczMDY4MTk1OTAw.YenrVw.t_R4fD3hT0FztIJZh4pPJC-wQhM"
CLIENT_SECRET = "jtEnY66MmtUY4Z5lNS-waLqQvfwQFyB5"
REDIREC_URI = "http://192.168.1.73:8101/login"
OAUTH_URL = f"https://discord.com/api/oauth2/authorize?client_id=933860473068195900&redirect_uri={parse.quote(REDIREC_URI)}&response_type=code&scope=identify"

class Config(object):
    SECRET_KEY = "XD"
    
class DevelopentConfig(Config):
    DEBUG = True
    
class HostConfig(Config):
    DEBUG = False
    