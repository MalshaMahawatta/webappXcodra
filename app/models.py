from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin


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
    number = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    creditCard = db.Column(db.Boolean)
    bookedBy=db.Column(db.String)
    duration=db.Column(db.String)

    def get_id(self):
        return self.number


class Guest(db.Model, UserMixin):

    ''' room details. '''

    __tablename__ = 'guests'
    number = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String)
    availability = db.Column(db.Boolean)
    bookedBy=db.Column(db.String)
    duration=db.Column(db.String)

    def get_id(self):
        return self.number