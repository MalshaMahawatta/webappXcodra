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

   # number = db.Column(db.Integer,primary_key=True)
   # type = db.Column(db.String)
   # availability = db.Column(db.Boolean)

   # creditCard = db.Column(db.Boolean)
    #bookedBy=db.Column(db.String)
    #duration=db.Column(db.String)





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


    offer_number = db.Column(db.Integer, db.ForeignKey('offers.offerID'))
    offers = db.relationship('Offers', backref=db.backref('guests', lazy='dynamic'),uselist=True)



    def get_id(self):
        return self.number




class Offers(db.Model, UserMixin):
    ''' offer details. '''

    __tablename__ = 'offers'
    offerID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    percentage =db.Column(db.Integer)

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

class FeedBack(db.Model, UserMixin):



    __tablename__ = 'feedBack'
    feedBackId=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    phone=db.Column(db.Integer)
    email=db.Column(db.String)
    country=db.Column(db.String)
    address=db.Column(db.String)
    comment=db.Column(db.String)

    def get_id(self):
        return self.feedBackId


class Payments(db.Model, UserMixin):
    ''' offer details. '''

    __tablename__ = 'payment'
    paymentID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    paidBy = db.Column(db.String)
    date = db.Column(db.String)
    grossprice =db.Column(db.Integer)
    netprice =db.Column(db.Integer)


    def get_id(self):
        return self.title
