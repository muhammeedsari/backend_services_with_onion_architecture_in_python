from mongoengine import *
from mongoengine.document import DynamicDocument
from mongoengine.fields import BooleanField, DateTimeField, StringField

class PersonMongodbModel(DynamicDocument):
    job = StringField()
    current_location = StringField()
    userId = StringField()
    name = StringField()
    sex = BooleanField()
    birthdate = DateTimeField()
    currency = StringField()
    iban = StringField()
    prefix = StringField()
    race = StringField()

