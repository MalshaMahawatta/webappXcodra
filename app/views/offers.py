__author__ = 'Dilini'

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db

from app.forms import offers as offers_details
from app.forms import imageOffers as imageOffers_details

# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])


UPLOAD_FOLDER_OFFERS =  'D:/Xcodra/webappXcodra/app/static/img/offers'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



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
            offerID=form.offerID.data,
            percentage =form.percentage.data

        )
        # Insert the offer in the database

        offer = models.Offers.query.filter_by(offerID=form.offerID.data).first()

        offer.title = form.title.data
        offer.description = form.description.data
        offer.OfferID = form.offerID.data
        offers.percentage = form.offerID.data
        db.session.commit()

        global m
        m=form.offerID.data





        print m
        imageNew=str(m)+".jpg"
        print imageNew




        flash('added offer details sucessfully.', 'positive')
        return redirect("http://127.0.0.1:5000/offers/addImage")
    return render_template('offers/addOffers.html', form=form, title='Offers Details')

@offersbp.route('/addImage', methods=['GET', 'POST'])
def upload_file():
   # print 10
    form = imageOffers_details.OffersImage()

    if form.validate_on_submit():
    #if request.method == 'POST':
      #  print 10


        offerID1=form.offerID1.data
        print offerID1
        offerID12=str(offerID1)+".jpg"
        print offerID12


        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            file.filename=str(m)+".jpg"



            print file.filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_OFFERS'], filename))
                return redirect(url_for('offersbp.upload_file',
                                        filename=filename))

            flash('added images sucessfully.', 'positive')
            return redirect("http://127.0.0.1:5000/offers/viewOffers")
    return render_template('offers/addImage.html', title='Upload Images',form=form)


@offersbp.route('/viewOffers',methods=['GET', 'POST'])

def viewOffers():
    offers=models.Offers.query.all()
    return render_template('offers/viewOffers.html', title='Offers',offers=offers)




