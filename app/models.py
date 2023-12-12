import mongoengine

"""

Define you MongoEngine Models here

"""


class InternalUser(mongoengine.Document):
    username = mongoengine.StringField(unique=True)
    access_token = mongoengine.StringField(unique=True, null=True)
    state = mongoengine.StringField(null=True)
    password_hash = mongoengine.StringField()
