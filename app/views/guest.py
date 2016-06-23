__author__ = 'Malsha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import guest as guest_details
from flask_table import Table, Col
from datetime import datetime


# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
guestbp = Blueprint('guestbp', __name__, url_prefix='/guest')


@guestbp.route('/addGuest', methods=['GET', 'POST'])
@login_required
def addGuest():
    form = guest_details.Guest()
    availableRooms=[]
    availableRoomsObj= models.Room.query.filter_by(availability=True).all()
    for u in availableRoomsObj:
        aRoomDetails=str(u.number) + '-' + str(u.type)
        availableRooms.append(aRoomDetails)
    print availableRooms
    k=1
    a=[]
    for i in availableRooms:
        a.append((str(k),str(i)))
        k=k+1

    form.room_number.choices=a

    #append offerID column
    availableOffers=[]
    availableOffersObj= models.Offers.query.all()
    for z in availableOffersObj:
        aOfferDetails=str(z.offerID) + '-' + str(z.title)
        availableOffers.append(aOfferDetails)
    print availableOffers
    j=1
    b=[]
    for p in availableOffers:
        b.append((str(j),str(p)))
        j=j+1

    form.offer_number.choices=b

    #form.room_number1.choices[availableRooms]=[(key, availableRooms[key]) for key in availableRooms]
    if form.validate_on_submit():

        checkedInTime=datetime.now().date()
        print checkedInTime
        guest = models.Guest(
            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
            checkedInTime=checkedInTime
        )


        # Insert the guest in the database
        db.session.add(guest)
        db.session.commit()
        index=int(form.room_number.data) - 1
        print index
        roomNumberToMap=availableRooms[index].split('-')[0]
        print roomNumberToMap
        roomToLink = models.Room.query.filter_by(number=roomNumberToMap).first()
        roomToLink.guests.append(guest)
        #roomToLink.guests(guest)
        db.session.commit()


        index1=int(form.offer_number.data) - 1
        print index1
        guestNumberToMap=availableOffers[index1].split('-')[0]
        print guestNumberToMap
        guestToLink = models.Offers.query.filter_by(offerID=guestNumberToMap).first()
        guestToLink.guests.append(guest)
        #roomToLink.guests(guest)
        db.session.commit()

        gnumber1 = models.Room.query.filter_by(number=index).first()

        gnumber1.availability = False

        db.session.commit()



        flash('added guest details sucessfully.', 'positive')
        return redirect(url_for('index'))
    return render_template('guest/details.html', form=form, title='Guest Details',availableRooms='availableRooms')

@guestbp.route('/showRecognizedGuest', methods=['GET', 'POST'])
@login_required
def recogedGuest():

    return render_template('guest/recognizedGuest.html',methods=['GET','POST'])
