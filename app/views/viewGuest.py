__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash, request)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from flask_table import Table, Col
from app.forms import selectGuest as select_guest
import datetime
from datetime import date





# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
viewGuestbp = Blueprint('viewGuestbp', __name__, url_prefix='/viewGuest')


@viewGuestbp.route('/select', methods=['GET', 'POST'])
@login_required
def select():
    # form=select_guest.SelectGuest()
    # number=form.number.data
    # print number
    form = select_guest.SelectGuest()
    if form.validate_on_submit():
        number = form.number.data
        global n
        n = number
        print number

        return redirect("http://127.0.0.1:5000/viewGuest/view")
    return render_template('payment/selectGuest.html', title='Payment', form=form)


@viewGuestbp.route('/view', methods=['GET', 'POST'])
@login_required
def view():
    gnumber = models.Room.query.filter_by(number=n).first()
    b = gnumber.guest_number

    print b

    gnumber.availability = True

    db.session.commit()

    # print availability

    payments = models.Guest.query.get(b)

    if request.method == 'POST':
        # if form.validate_on_submit():
        return redirect("http://127.0.0.1:5000/viewGuest/calculatePayment")
    return render_template('payment/showDetails.html', title='Payment', payments=payments)


@viewGuestbp.route('/calculatePayment', methods=['GET', 'POST'])
@login_required
def calculatePayment():
    payment = models.Room.query.filter_by(number=n).first()
    b = payment.guest_number
    # print b

    time = models.Guest.query.filter_by(number=b).first()
    d = time.checkedInTime
    global name, today
    name = time.name
    print d
    y1 = d[0:-6]
    m1 = d[5:-3]
    d1 = d[8:]
    y3 = int(y1)
    m3 = int(m1)
    d3 = int(d1)

    print y3
    print m3
    print d3

    today = datetime.date.today()
    print today
    e = today.strftime('%Y%m%d')
    print e
    y2 = e[0:-4]
    m2 = e[4:-2]
    d2 = e[6:]
    y4 = int(y2)
    m4 = int(m2)
    d4 = int(d2)
    print y4
    print m4
    print d4

    arrivaldate = date(y3, m3, d3)
    departureDate = date(y4, m4, d4)

    roomTable = models.Room.query.filter_by(number=n).first()
    global pricebasic
    pricebasic = roomTable.roomPrice
    global grossprice, netprice

    guestRow = models.Room.query.filter_by(number=n).first()
    m = guestRow.guest_number
    offerTable = models.Guest.query.filter_by(number=m).first()

    offerid = offerTable.offer_number
    getRate = models.Offers.query.filter_by(offerID=offerid).first()
    global rate, type
    rate = getRate.percentage
    type = getRate.title

    if arrivaldate == departureDate:
        grossprice = pricebasic
        netprice = pricebasic - (pricebasic * rate / 100)

    else:

        duration1 = departureDate - arrivaldate
        print duration1.days
        p = duration1 * pricebasic

        print p

        g = p

        h = str(g)
        grossprice = h[:-13]
        print grossprice

        z = p - (p * rate / 100)
        print z
        y = z
        x = str(y)
        netprice = x[:-13]
        print netprice

    room_type = models.Room.query.filter_by(number=n).first()
    print room_type.type

    if request.method == 'POST':
        payment = models.Payments(
            paidBy=name,
            date=today,
            netprice=netprice,
            grossprice=grossprice
        )
        db.session.add(payment)
        db.session.commit()

        flash('Payment details added successfully.Thank you,Come again.', 'positive')
        return redirect("http://127.0.0.1:5000/user/account")

    return render_template('payment/price.html', title='Payment Details', grossprice=grossprice, netprice=netprice,
                           rate=rate, type=type)
