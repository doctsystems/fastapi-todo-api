import peewee

from app.v1.utils.db import db


class User(peewee.Model):
    """docstring for User"""
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    class Meta:
        database = db