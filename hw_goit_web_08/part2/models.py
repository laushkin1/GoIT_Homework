from mongoengine import Document
from mongoengine.fields import StringField, BooleanField


class Contact(Document):
    fullname = StringField()
    profession = StringField()
    email = StringField()
    is_send = BooleanField(default=False)
