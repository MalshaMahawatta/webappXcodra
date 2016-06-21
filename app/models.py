from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    ''' A website user. '''

    __tablename__ = 'users'
    name = db.Column(db.String)
    surname = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email


class Room(db.Model, UserMixin):
    ''' room details. '''

    __tablename__ = 'rooms'

    number = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    availability = db.Column(db.Boolean)
    roomPrice = db.Column(db.Integer)
    guest_number = db.Column(db.Integer, db.ForeignKey('guests.number'))
    guests = db.relationship('Guest', backref=db.backref('rooms', lazy='dynamic'),uselist=True)

    def get_id(self):
        return self.number


class Guest(db.Model, UserMixin):
    ''' room details. '''

    __tablename__ = 'guests'
    number = db.Column(db.Integer, primary_key=True ,autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    type = db.Column(db.String)
    checkedInTime = db.Column(db.String)
    recognized=db.Column(db.Boolean)
    arrivalTime=db.Column(db.String)

    def get_id(self):
        return self.number

    def get_id(self):
        return self.number


class Offers(db.Model, UserMixin):
    ''' offer details. '''

    __tablename__ = 'offers'
    title = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)
    percentage = db.Column(db.Integer)


    def get_id(self):
        return self.title

class Facility(db.Model, UserMixin):

    """ room details. """

    __tablename__ = 'facilities'
    facilityId=db.Column(db.Integer,primary_key=True)
    facility = db.Column(db.String)
    description = db.Column(db.String)
    #availability = db.Column(db.Boolean)
    #creditCard = db.Column(db.Boolean)
   # bookedBy=db.Column(db.String)
   # duration=db.Column(db.String)

    def get_id(self):
        return self.number

