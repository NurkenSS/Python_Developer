from peewee import Model, CharField, TextField, DateTimeField
from db.db_connection import db
import datetime

class SearchHistory(Model):
    user_id = CharField()
    query = TextField()
    result = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
