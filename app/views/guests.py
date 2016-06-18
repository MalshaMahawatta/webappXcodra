__author__ = 'Dilini'
from flask import Flask, render_template
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import guests as guests_details
from flask_table import Table, Col


# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
guestsbp = Blueprint('guestsbp', __name__, url_prefix='/guests')


@guestsbp.route('/selectGuest', methods=['GET', 'POST'])
@login_required
def selectGuest():
    form = guests_details.Guest()
    if form.validate_on_submit():
     guests = models.Guest(
           number=form.number.data,
            )

        #print guests
        # Insert the offer in the database
        #   db.session.add(guests)
        #  db.session.commit()

        #  flash('added offer details sucessfully.', 'positive')
        # return redirect(url_for('image'))
    return render_template('guests/selectGuest.html', form=form, title='Select Guest')


@guestsbp.route('/viewGuest', methods=['GET', 'POST'])
@login_required
def viewGuest():

    guests = models.Guest.query.all()

    class ItemTable(Table):
        classes = ['ui celled table']
        number = Col('number')
        type = Col('type')
        availability = Col('availability ')
        bookedBy = Col('bookedBy')
        duration = Col('duration ')
        rooms=Col('room')
        #guest_number = Col('guest_number ')


    table = ItemTable(guests)
    print(table.__html__())
    return render_template('guests/viewGuest.html', title='Guests', guests=table)
