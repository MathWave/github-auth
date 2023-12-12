import logging
from typing import Dict, Any

from flask import Flask
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder import AppBuilder
from flask_mongoengine import MongoEngine

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)


class AppSecurityManager(SecurityManager):
    oauth_whitelists = {
        'github': ['*']
    }


app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)
appbuilder = AppBuilder(app, security_manager_class=SecurityManager)


@appbuilder.sm.oauth_user_info_getter
def my_user_info_getter(
    sm: SecurityManager,
    provider: str,
    response: Dict[str, Any]
) -> Dict[str, Any]:
    if provider == 'self':
        me = sm.oauth_remotes[provider].get("get_user")
        if not me.ok:
            return {}
        user = me.json()
        return {
            "username": "self_" + user['username'],
            "email": "",
        }
    return sm.get_oauth_user_info(provider, response)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    

from app import views
