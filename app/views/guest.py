__author__ = 'Malsha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import guest as guest_details
from flask_table import Table, Col


# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
guestbp = Blueprint('guestbp', __name__, url_prefix='/guest')


@guestbp.route('/addGuest', methods=['GET', 'POST'])
@login_required
def addGuest():
    form = guest_details.Guest()
    if form.validate_on_submit():
        guest = models.Guest(
            number=form.number.data,
            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
            type=form.type.data,
        )
        # Insert the guest in the database
        db.session.add(guest)
        db.session.commit()

        roomToLink = models.Room.query.filter_by(number=form.room_number.data).first()
        roomToLink.guests.append(guest)
        #roomToLink.guests(guest)
        db.session.commit()

        flash('added guest details sucessfully.', 'positive')
        return redirect(url_for('index'))
    return render_template('guest/details.html', form=form, title='Guest Details')

