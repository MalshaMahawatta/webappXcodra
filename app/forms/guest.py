__author__ = 'Malsha'

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, IntegerField, StringField, BooleanField,SelectField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)
from app.models import User


class Unique(object):
    '''
    Custom validator to check an object's attribute
    is unique. For example users should not be able
    to create an account if the account's email
    address is already in the database. This class
    supposes you are using SQLAlchemy to query the
    database.
    '''

    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class Guest(Form):
    ''' add guest details form. '''

    number = IntegerField(validators=[Required()],
                          description='Guest ID')
    name = StringField(validators=[Required()],
                       description='Guest First Name')


    surname = StringField(validators=[Required()],
                   description='Guest Surname')

    phone = IntegerField(validators=[Required()],
                   description='Contact Number')
    email = StringField(validators=[Required()],
                   description='Guest Email')

    # type = StringField(validators=[Required(), Length(min=2)],
    #                description='Room Type')

    #room_number = IntegerField(validators=[Required()],
                   #description='Room Number')
    room_number = SelectField(validators=[Required()],
                   description='Room Number filtered')