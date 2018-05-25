from peewee import *
from flask_login import UserMixin

db = SqliteDatabase('linguaclassifier.db')


class Users(Model, UserMixin):
    name = CharField(default='')
    email = CharField()
    password = CharField(default='')
    is_activate = BooleanField(default=False)

    class Meta:
        database = db


class Researches(Model):
    owner = ForeignKeyField(Users)
    name = CharField()
    material = CharField()
    task = CharField()
    fields = CharField()

    class Meta:
        database = db


class Respondents(Model):
    owner = ForeignKeyField(Researches)
    field1 = CharField()
    field2 = CharField(null=True)
    field3 = CharField(null=True)
    field4 = CharField(null=True)
    field5 = CharField(null=True)
    filled_all = BooleanField(default=False)

    class Meta:
        database = db


class Groups(Model):
    owner = ForeignKeyField(Respondents)
    name = CharField()
    elements = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Users, Researches, Respondents, Groups], safe=True)
