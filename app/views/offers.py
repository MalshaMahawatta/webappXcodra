__author__ = 'Dilini'

import os

from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import offers as offers_details

# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
offersbp = Blueprint('offersbp', __name__, url_prefix='/offers')


@offersbp.route('/addOffers', methods=['GET', 'POST'])
@login_required
def addOffers():
    form = offers_details.Offers()
    if form.validate_on_submit():

        offers = models.Offers(
            title=form.title.data,
            description=form.description.data,

        )
        # Insert the offer in the database

        db.session.add(offers)
        db.session.commit()

        flash('added offer details sucessfully.', 'positive')
        return redirect(url_for('image'))
    return render_template('offers/addOffers.html', form=form, title='Offers Details')





@offersbp.route('/viewOffers',methods=['GET', 'POST'])
@login_required
def viewOffers():
    offers=models.Offers.query.all()
    return render_template('offers/viewOffers.html', title='Offers',offers=offers)


