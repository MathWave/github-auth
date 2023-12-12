import os

from flask_appbuilder.const import AUTH_OAUTH
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP
basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = os.getenv('SECRET_KEY', 'verysecretkey')
ORIGIN = os.getenv('ORIGIN', 'http://0.0.0.0:8080/')

# The MongoEngine connection string.
MONGODB_SETTINGS = {
    'host': os.getenv("MONGO_HOST", 'localhost'),
    'DB': 'github-auth',
    'username': 'mongo',
    'password': os.getenv("MONGO_PASSWORD", "password")
}

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#------------------------------
# GLOBALS FOR APP Builder 
#------------------------------
# Uncomment to setup Your App name
#APP_NAME = "My App Name"

# Uncomment to setup Setup an App icon
#APP_ICON = "static/img/logo.jpg"

#----------------------------------------------------
# AUTHENTICATION CONFIG
#----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_OAUTH

GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', 'githubclientsecret')
APP_CLIENT_SECRET = os.getenv('APP_CLIENT_SECRET', 'randomstring')

OAUTH_PROVIDERS = [
    {
        "name": "github",
        "icon": "fa-github",
        "token_key": "access_token",
        "remote_app": {
            "client_id": '9a9b207b4ed051d99296',
            "client_secret": GITHUB_CLIENT_SECRET,
            "api_base_url": "https://api.github.com/user",
            "request_token_url": None,
            "access_token_url": f"https://github.com/login/oauth/access_token",
            "authorize_url": f"https://github.com/login/oauth/authorize",
        },
    },
    {
        "name": "self",
        "icon": "fa-key",
        "token_key": "access_token",
        "remote_app": {
            "client_id": '9a9b207b4ed051d99296',
            "client_secret": APP_CLIENT_SECRET,
            "api_base_url": ORIGIN,
            "request_token_url": None,
            "access_token_url": f"{ORIGIN}login/oauth/access_token",
            "authorize_url": f"{ORIGIN}auth",
        },
    }
]

# Uncomment to setup Full admin role name
#AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
#AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
#AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
#AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#     {'name': 'Github', 'url': 'https://github.com/<username>'}
# ]
#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    'pt': {'flag':'pt', 'name':'Portuguese'},
    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
    'es': {'flag':'es', 'name':'Spanish'},
    'de': {'flag':'de', 'name':'German'},
    'zh': {'flag':'cn', 'name':'Chinese'},
    'ru': {'flag':'ru', 'name':'Russian'}
}
#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
#APP_THEME = "bootstrap-theme.css"  # default bootstrap
#APP_THEME = "cerulean.css"
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"  
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"   
#APP_THEME = "spacelab.css"
#APP_THEME = "united.css"
#APP_THEME = "yeti.css"
