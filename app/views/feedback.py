
__author__ = 'Dilini'

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import feedBack as feedBack_details

feedBackbp = Blueprint('feedBackbp', __name__, url_prefix='/contact')
@feedBackbp.route('/addFeedBack', methods=['GET', 'POST'])



def addFeedBack():
    form = feedBack_details.FeedBack()
    if form.validate_on_submit():
        feedBack = models.FeedBack(

            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
            country=form.country.data,
            address=form.address.data,
            comment=form.comment.data


        )

        db.session.add(feedBack)
        db.session.commit()




        flash('added FeedBack sucessfully.', 'positive')
        return redirect('index')
    return render_template('contact.html', form=form, title='feedback Details')
