__author__ = 'Dilini'

from flask.ext.wtf import Form
from wtforms import TextField, PasswordField,IntegerField,StringField,BooleanField
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

    ''' add offers details form. '''

    number= StringField(validators=[Required()],
                     description='Guest ID')





